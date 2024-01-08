from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PDFGeneratorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pdf_generator'
    verbose_name = _('چاپ')
