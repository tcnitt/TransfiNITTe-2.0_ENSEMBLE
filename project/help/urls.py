from django.urls import path
from django.views.generic import TemplateView
from .views import *

app_name = 'help'


urlpatterns = [
    path('',HelpListView.as_view(),name='help-list'),
]