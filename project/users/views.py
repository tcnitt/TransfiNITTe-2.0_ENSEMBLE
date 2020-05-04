from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.forms import AuthenticationForm

from .forms import (
    StudentCreationForm,StudentChangeForm,
    ProfessorCreationForm,ProfessorChangeForm,
)
from .models import Users,Student,Professor
from django.contrib.auth.hashers import make_password

def StudentLogin(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'users/student_login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'users/student_login.html', {'form': form})
    pass 



def StudentSignup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/')
        else:
            return render(request, 'users/student_signup.html', {'form': form})
    else:
        form = StudentCreationForm()
        return render(request, 'users/student_signup.html', {'form': form})
    pass


def ProfLogin(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'users/prof_login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'users/prof_login.html', {'form': form})
    pass 



def ProfSignup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = ProfessorCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/')
        else:
            return render(request, 'users/prof_signup.html', {'form': form})
    else:
        form = ProfessorCreationForm()
        return render(request, 'users/prof_signup.html', {'form': form})
    pass


def StudentProfileView(request,username):

    user = get_object_or_404(Student,username=username)

    context = {
        'user' : user
    }
    
    return render(request,'users/student_profile.html',context)

def ProfProfileView(request,username):

    user = get_object_or_404(Professor,username=username)

    context = {
        'user' : user
    }
    
    return render(request,'users/prof_profile.html',context)