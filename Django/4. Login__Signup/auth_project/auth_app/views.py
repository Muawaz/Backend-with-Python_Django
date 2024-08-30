from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request):
    return render(request, 'home.html')

def log_in_view(request):
    return render(request, 'log_in.html')

def sign_up_view(request):
    return render(request, 'sign_up.html')
