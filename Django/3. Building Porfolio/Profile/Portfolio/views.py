from django.shortcuts import render
from django.http import HttpResponse
from .models import Portfolio_model

# Create your views here.

def Home_page(request):
    # return HttpResponse("Hello World !")
    return render(request, 'home.html')


def Contact_us_form(request):
    return render(request, 'contact.html')

def form_submission(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contact = Portfolio_model(name = name, email = email, phone = phone, message = message)
        contact.save()

        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print(f"Message: {message}")

        return render(request, 'success.html')
    else:
        return HttpResponse("Invalid request.")
    
