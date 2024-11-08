from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from ..forms import UserLoginForm
from ..models import User

def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            
            user = authenticate(request, name=name, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, "Login failed")
                return redirect('user_session_create')
    else:
        form = UserLoginForm()
    
    return render(request, "user_sessions/new.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect('index')

