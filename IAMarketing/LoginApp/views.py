from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from .forms import CustomUserCreationForm
# Create your views here.

def loginView(request):
    return render(request,'registration/login.html')

def registerView(request):
    data = {
        'form' : CustomUserCreationForm()
    }
    return render(request, 'register.html',data)


