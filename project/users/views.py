from django.shortcuts import render,redirect,get_object_or_404
from .forms import UserForm
from .models import user 

# Create your views here.
def RegisterUserView(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home-page')
    else:
        form = UserForm()
    return render(request,'users/user_registration.html',{'form':form})


def UserProfileView(request,id):
    user_profile = get_object_or_404(user,id=id)
    context = {'user':user_profile}
    return render(request,'users/profile.html',context)
