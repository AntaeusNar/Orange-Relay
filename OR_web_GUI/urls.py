"""Defines the url patterns for the OR_web_GUI"""

from django.urls import path

from . import views

app_name = 'OR_web_GUI'

urlpatterns = [
    # Home page
    path('', views.index, name='index')
]