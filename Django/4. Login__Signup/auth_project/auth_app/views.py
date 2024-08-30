from django.shortcuts import render
from .models import app_model
from django.http import HttpResponse
import re

# Create your views here.

def home_view(request):
    return render(request, 'home.html')

def log_in_view(request):
    return render(request, 'log_in.html')

def sign_up_view(request):
    return render(request, 'sign_up.html')

def check_sign_up(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not re.match("^[A-Za-z]+$", first_name):
            message = "First name should only contain alphabets"
            return render(request, 'error.html', {"message": message})
        
        elif not re.match("^[A-Za-z]+$", last_name):
            message = "Last name should only contain alphabets"
            return render(request, 'error.html', {"message": message})
        
        elif not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
            message = "Please enter a valid email address"
            return render(request, 'error.html', {'message': message})
        
        elif len(password) < 8 or not re.match(r"^[A-Z]", password):
            message = "Password must be at least 8 characters long and start with a capital letter."
            return render(request, 'error.html', {'message': message})
        
        if app_model.objects.filter(email == email).exists():
            message = "An account with this email already exists."
            return render(request, 'error.html', {'message': message})
        




        user = app_model(first_name=first_name, last_name=last_name, email=email, password=password)
        user.save()

        print("First Name:", first_name)
        print("Last Name:", last_name)
        print("Email:", email)
        print("Password:", password)

    return render(request, 'home.html')
