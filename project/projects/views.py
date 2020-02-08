from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q
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



class SearchResultsView(ListView):
    model = projects
    template_name = 'projects/projects_list.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        return projects.objects.filter(
            Q(title__icontains=query) | 
            Q(domain__icontains=query) |
            Q(body__icontains=query) | 
            Q(description__icontains=query)
            )


