from django.core.mail import send_mail
from django.conf import settings
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken

def send_verfication_email(email):
    try:
        subject = 'Account Verification'
        user = User.objects.get(email=email)
        token = RefreshToken.for_user(user).access_token
        verification_link = f"http://127.0.0.1:8000/verifyAccount/?token={token}"

        #Email message
        message = verification_link = f"Click the link below to verify your account:\n{verification_link}"
        from_email = settings.DEFAULT_FROM_EMAIL
        send_mail(subject, message, from_email, [email])

        return True
    except Exception as e:
        print(f"Error sending verification email to {email}: {e}")
        return False