from pdf_generator.views import ChromPDFTemplateView, LatexPDFTemplateView
from .models import Staff

class StaffHTMLPrint(ChromPDFTemplateView):
    template_name = 'staff.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['staffs'] = Staff.objects.all()
        return context


class StaffLatexPrint(LatexPDFTemplateView):
    template_name = 'staff.tex'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['staffs'] = Staff.objects.all()
        return context
