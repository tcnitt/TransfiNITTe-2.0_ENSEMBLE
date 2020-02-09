from django.urls import path
from django.views.generic import TemplateView

from .views import *

app_name = 'stats'


urlpatterns = [
    path('',TemplateView.as_view(template_name='stats/stats_home.html'),name='stats-home'),
    path('departments/',DepartmentStatsView,name='department-stats'),
    path('compare-departments/',TemplateView.as_view(template_name='stats/compare.html'),name='compare-departments'),
    path('compare-colleges/',TemplateView.as_view(template_name='stats/other_colleges.html'),name='compare-colleges'),

]