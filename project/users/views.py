from django.shortcuts import render,redirect
from .forms import UserForm

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