from django.urls import path

from . import demo

app_name = 'pdf_generator'

urlpatterns = [
    path('chrome/', demo.StaffChromePrint.as_view(), name='print-chrome'),
    path('latex/', demo.StaffLatexPrint.as_view(), name='print-latex'),
]
