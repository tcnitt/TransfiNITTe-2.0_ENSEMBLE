from django.urls import path
from django.views.generic import TemplateView
from .views import *

app_name = 'users'

urlpatterns = [
    path('register-user/',RegisterUserView,name='register-user'),
    path('profile/<int:id>',UserProfileView,name='profile'),
    path('prof/register',ProfRegisterView,name='prof-register'),
    path('prof/login',ProfLoginView,name='prof-login'),
    path('prof/profile',ProfProfileView,name='prof-profile'),
    # path('',TemplateView.as_view(template_name='home/index.html'),name='home-page'),
]