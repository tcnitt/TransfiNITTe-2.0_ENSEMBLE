from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import projects
from .forms import ProjectForm

class ListProjectsView(ListView):
    model = projects
    paginate_by = 10


def AddNewProjectView(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects:list-projects')
    else:
        form = ProjectForm()
    return render(request,'projects/add_project.html',{'form':form})