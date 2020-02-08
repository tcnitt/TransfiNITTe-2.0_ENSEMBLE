from django.shortcuts import render
from django.views.generic.list import ListView
# Create your views here.
from .models import faq

class ListFAQsView(ListView):
    model = faq
    paginate_by = 10