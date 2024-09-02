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
    email_list = []
    for i in app_model.objects.values():
        email_list.append(i['email'])

    print (email_list)


    return render(request, 'sign_up.html', {'email_list': email_list})

def check_sign_up(request):
    save_item = True

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not re.match("^[A-Za-z]+$", first_name):
            save_item = False
            # message = "First name should only contain alphabets"
            # return render(request, 'error.html', {"message": message})
        
        elif not re.match("^[A-Za-z]+$", last_name):
            save_item = False
            # message = "Last name should only contain alphabets"
            # return render(request, 'error.html', {"message": message})
        
        elif not re.match(r"^[\w\.-]+@[\w\.-]+\.com$", email):
            save_item = False
            # message = "Please enter a valid email address"
            # return render(request, 'error.html', {'message': message})
        
        elif len(password) < 8 or not re.match(r"^[A-Z]", password):
            save_item = False
            # message = "Password must be at least 8 characters long and start with a capital letter."
            # return render(request, 'error.html', {'message': message})
        
        if app_model.objects.filter(email = email).exists():
            message = "An account with this email already exists."
            return render(request, 'error.html', {'message': message})
        
        if save_item == True:
            user = app_model(first_name=first_name, last_name=last_name, email=email, password=password)
            user.save()
            return render(request, 'home.html')

        print("First Name:", first_name)
        print("Last Name:", last_name)
        print("Email:", email)
        print("Password:", password)

    
