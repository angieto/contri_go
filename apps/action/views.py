from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def offer_help(request):
    return render(request, 'action/offer_help.html')

def request_help(request):
    return render(request, 'action/request_help.html')