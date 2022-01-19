from django.shortcuts import render,redirect
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


# Create your views here.


def homepage(request):
    return render(request,'home/homepage.html')



def seecollege(request):
    return render(request,'home/seecollege.html')
