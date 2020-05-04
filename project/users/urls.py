from django.urls import path
from django.views.generic import TemplateView
from .views import *

app_name = 'users'

urlpatterns = [
    path('auth',TemplateView.as_view(template_name='users/auth.html'),name='auth'),
    path('student-login/',StudentLogin,name='student-login'),
    path('student-signup/',StudentSignup,name='student-signup'),
    path('prof-login/',ProfLogin,name='prof-login'),
    path('prof-signup/',ProfSignup,name='prof-signup'),
    path('student-profile/<str:username>',StudentProfileView,name='student-profile'),
    path('prof-profile/<str:username>',ProfProfileView,name='prof-profile'),
]