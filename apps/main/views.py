from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
import bcrypt

def main_page(request):
    return render(request, 'main/main_page.html')

def login_page(request):
    return render(request, 'main/login.html')

def create_user(request):
    errors = User.objects.registration_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('index')
    else:
        user_password = bcrypt.hashpw(request.POST['password'].encode('utf8'), bcrypt.gensalt(10))
        user_password = user_password.decode('utf8')
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=user_password)
        request.session['user'] = user.id
        return redirect('dashboard')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('index') 
    else:   
        user = User.objects.get(email=request.POST['email'])
        request.session['user'] = user.id
        return redirect('dashboard')

def logout(request):
    request.session.clear()
    return redirect('index')

def dashboard(request):
    return render(request, 'main/dashboard.html')