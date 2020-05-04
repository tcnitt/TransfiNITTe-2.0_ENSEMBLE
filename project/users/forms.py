from django import forms

from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from .models import Student,Professor

class StudentCreationForm(UserCreationForm):

    class Meta:
        model = Student
        fields = ('username','email','first_name','last_name','email','year','department','cgpa','github_link','linkedin_link','resume_link','transcript_link','areas_of_interest')


class StudentChangeForm(UserChangeForm):

    class Meta:
        model = Student
        fields = ('username','email','first_name','last_name','email','year','department','cgpa','github_link','linkedin_link','resume_link','transcript_link','areas_of_interest')


class ProfessorCreationForm(UserCreationForm):

    class Meta:
        model = Professor
        fields = ('username','email','first_name','last_name','department','research_areas')


class ProfessorChangeForm(UserChangeForm):

    class Meta:
        model = Professor
        fields = ('username','email','first_name','last_name','department','research_areas')