"""Defines the url patterns for the OR_web_GUI"""

from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

from . import views

app_name = 'OR_web_GUI'

urlpatterns = [
    # Basic Pages
    path('', views.index, name='index'),
    path('rules/', views.rules, name='rules'),
    path('inputs/', views.inputs, name='inputs'),
    path('outputs/', views.outputs, name='outputs'),

    # Configuration Pages
    path('new_output/', views.new_output, name='new_output'),
    # Function 'Pages'
    path('relay_toggle/<int:output_id>/', views.relay_toggle, name='relay_toggle'),
    path('relaystatus/<int:output_id>/', views.relay_state, name='relay_state'),

    # Other urls
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('OR_web_GUI/img/favicon.ico'), permanent=False), name='favicon'),
]
