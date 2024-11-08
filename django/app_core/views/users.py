from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import User
from ..forms import UserForm

def user_list(request):
    users = User.objects.all()
    return render(request, 'users/index.html', {'users': users})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created successfully")
            return redirect('user_list')
        else:
            messages.error(request, "User not created")
    else:
        form = UserForm()
    
    return render(request, 'users/new.html', {'form': form})
