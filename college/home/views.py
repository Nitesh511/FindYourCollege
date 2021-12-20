from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import Loginform,createUserForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def homepage(request):
    return render(request,'home/homepage.html')


def logout_user(request):
    logout(request)
    return redirect('/login')



def login_user(request):
    if request.method =="POST":
        form = Loginform(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username = data['username'], password = data['password'])
            if user is not None:
                if user.is_staff:
                    login(request, user)
                    return redirect('/admins/dashboard')
                elif not user.is_staff:
                    login(request,user)
                    return redirect('/products/homepage')

            else:
                messages.add_message(request,messages.ERROR,'invalid User credintials')
                return render(request,'account/login.html',{'form_login':form})
    context ={
        'form_login':Loginform,
        'activate_login':'active'
    }
    return render(request,'account/login.html',context)


def register_user(request):
    if request.method =="POST":
        form = createUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'User Registred SUcesfully')
            return redirect('/login')
        else:
            messages.add_message(request,messages.ERROR,'Unable To Register User')
            return render(request,'account/register.html',{'form_register':form})
    context = {
        'form_register': createUserForm,
        'activate_register': 'active'
    }
    return render(request, 'account/register.html', context)
