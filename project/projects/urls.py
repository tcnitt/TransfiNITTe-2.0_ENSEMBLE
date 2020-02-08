from django.urls import path
from django.views.generic import TemplateView

from .views import *

app_name = 'projects'

urlpatterns = [
    path('',ListProjectsView.as_view(),name='list-projects'),
    path('add-project/',AddNewProjectView,name='add-project'),
    path('search/',SearchResultsView.as_view(),name='search-projects'),
]