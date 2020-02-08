from django.urls import path
from django.views.generic import TemplateView
from .views import *

app_name = 'users'

urlpatterns = [
    path('register-user/',RegisterUserView,name='register-user'),
    # path('',TemplateView.as_view(template_name='home/index.html'),name='home-page'),
]