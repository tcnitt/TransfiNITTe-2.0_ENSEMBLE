from django.urls import path
from django.views.generic import TemplateView
from .views import *

app_name = 'faq'

urlpatterns = [
    path('',ListFAQsView.as_view(),name='list-faqs'),
    # path('',TemplateView.as_view(template_name='home/index.html'),name='home-page'),
]