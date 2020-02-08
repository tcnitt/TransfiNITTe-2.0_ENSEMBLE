from django.urls import path
from django.views.generic import TemplateView


app_name = 'home'

urlpatterns = [
    path('',TemplateView.as_view(template_name='home/index.html'),name='home-page'),
    path('tc/',TemplateView.as_view(template_name='home/terms.html'),name='terms-and-conditions'),
    path('aboutus/',TemplateView.as_view(template_name='home/aboutus.html'),name='about-us'),

]