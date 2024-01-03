from django.urls import path
from . import views

urlpatterns = [
    path("", views.LatexDemoView.as_view(), name="home"),
]
