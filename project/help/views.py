from django.shortcuts import render
from django.views.generic import ListView

from .models import help
# Create your views here.


class HelpListView(ListView):
    model = help
    template_name = 'help/help_list.html'