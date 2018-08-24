from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *

def dashboard(request):
    return render(request, 'community/dashboard.html')

def logout(request):
    request.session.clear()
    return redirect('main_page')
