from django.shortcuts import render,redirect,get_object_or_404
from .forms import UserForm,ProfForm
from .models import user,professor
from django.contrib.auth.hashers import make_password
# Create your views here.
def RegisterUserView(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.password = make_password(form.cleaned_data["password"])
            data.save()
            return redirect('home:home-page')
    else:
        form = UserForm()
    return render(request,'users/user_registration.html',{'form':form})


def UserProfileView(request,id):
    user_profile = get_object_or_404(user,id=id)
    context = {'user':user_profile}
    return render(request,'users/profile.html',context)

def ProfRegisterView(request):
    if request.method == 'POST':
        form = ProfForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.password = make_password(form.cleaned_data["password"])
            data.save()
            return redirect('home:home-page')
    else:
        form = ProfForm()
    return render(request,'users/prof_registration.html',{'form':form})



def ProfLoginView(request):
    pass

def ProfProfileView(request):
    user_profile = get_object_or_404(professor,id=1)
    context = {'user':user_profile}
    return render(request,'users/prof_profile.html',context)