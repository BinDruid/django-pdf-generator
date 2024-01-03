import logging
import os
from subprocess import PIPE, run, CalledProcessError
from tempfile import mkdtemp, mkstemp

from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.utils.encoding import smart_str
from django.views.generic.base import TemplateView

logger = logging.getLogger(__name__)


class PDFResponse(HttpResponse):
    def __init__(self, content=b"", *args, **kwargs):
        kwargs['content_type'] = 'application/pdf'
        super().__init__(content=content, *args, **kwargs)


class LatexCompiler:
    build_engine = 'xelatex'

    def __init__(self, raw_latex_string):
        self.raw_latex_string = raw_latex_string
        self.temporary_build_folder = None
        self.temporary_build_file = None

    def clean_raw_latex(self):
        clean_latex = self.raw_latex_string.replace("ـ", "-")
        clean_latex = clean_latex.replace('"', '\\"')
        clean_latex = clean_latex.replace('ي', 'ی')
        return clean_latex

    def build(self):
        clean_latex = self.clean_raw_latex()
        self.temporary_build_folder = mkdtemp()
        temp_file, self.temporary_build_file = mkstemp(dir=self.temporary_build_folder)
        os.write(temp_file, str.encode(clean_latex))
        os.close(temp_file)

    def compile(self):
        self.build()

        cmd = f'{self.build_engine} -halt-on-error -output-directory={self.temporary_build_folder} {self.temporary_build_file}'
        try:
            run(cmd, shell=True, stdout=PIPE, stderr=PIPE, check=True)

        except CalledProcessError as called_process_error:
            logger.error('Failed compiling the pdf with error: %s', called_process_error)

        return self.read()

    def read(self):
        pdf_contents = ''
        try:
            with open (self.temporary_build_file + '.pdf', 'rb') as f:
                pdf_contents = f.read()

        except FileNotFoundError as err:
            logger.error('Failed reading pdf file %s', err)
        return pdf_contents


class LatexView(TemplateView):
    response_class = PDFResponse
    compiler_class = LatexCompiler

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_pdf(context)

    def render_to_pdf(self, context):
        raw_latex = self.render_latex_template(context)
        pdf_file = self.compiler_class(raw_latex).compile()
        return self.response_class(pdf_file)

    def render_latex_template(self, context):
        template_content = self._read_template_file()
        build_context = Context(context)
        build_template = Template(template_content).render(build_context)
        return smart_str(build_template)

    def _read_template_file(self):
        template = get_template(self.template_name)
        template_path = template.origin.name
        with open(template_path) as f:
            content = f.read()
            return content
