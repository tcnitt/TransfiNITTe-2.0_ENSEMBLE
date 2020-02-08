from django import forms

from .models import projects

class ProjectForm(forms.ModelForm):
    class Meta:
        model = projects
        fields = '__all__'
