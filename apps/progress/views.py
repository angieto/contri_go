from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *

def show_record(request):
    return render(request, 'progress/record.html')

def show_schedule(request):
    return render(request, 'progress/schedule.html')
