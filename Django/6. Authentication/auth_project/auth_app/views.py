from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import auth_model
import re

# Create your views here.

def home_view(request):
    return render(request, 'home.html')

def sign_up_view(request):
    return render(request, 'sign_up.html')

def log_in_view(request):
    return render(request, 'log_in.html')


def check_sign_up(request):
    save_item = True
    message = ''

    if request.method == 'POST':
        userName = request.POST.get('username')
        firstName = request.POST.get('first_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not re.match("^[A-Za-z]+$", userName):
            save_item = False
            message += " username_error"
        
        elif not re.match("^[A-Za-z]+$", firstName):
            save_item = False
            message += " first"
        
        elif not re.match(r"^[\w\.-]+@[\w\.-]+\.com$", email):
            save_item = False
        
        elif len(password) < 8 or not re.match(r"^[A-Z]", password):
            save_item = False
        
        # if auth_model.objects.filter(email = email).exists():
        #     message = "An account with this email already exists."
        #     return render(request, 'error.html', {'message': message})
        
        if save_item == True:
            user = auth_model(userName=userName, firstName=firstName, email=email, password=password)
            user.save()
            return render(request, 'home.html')

        print("First Name:", userName)
        print("Last Name:", firstName)
        print("Email:", email)
        print("Password:", password)

        message = "An account with this email already exists."
        return render(request, 'error.html', {'message': message})



