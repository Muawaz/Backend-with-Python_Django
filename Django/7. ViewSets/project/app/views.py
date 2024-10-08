from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializer import StudentSerializer, UserSerializer
from rest_framework.authentication import (SessionAuthentication, BasicAuthentication, TokenAuthentication)
from rest_framework.permissions import (AllowAny, IsAuthenticated, IsAdminUser)
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
import io
from rest_framework.parsers import JSONParser
# ------email imports
from django.core.mail import send_mail
from django.conf import settings
from .emails import send_verfication_email
from rest_framework import status
from rest_framework_simplejwt.tokens import UntypedToken, TokenError
from django.shortcuts import redirect


def home_view(request):
    return render(request, 'home.html')

def sign_up_view(request):
    return render(request, 'sign_up.html')

def log_in_view(request):
    return render(request, 'log_in.html')

def details_view(request):
    return render(request, 'details.html')

from django.contrib.auth.decorators import login_required  # Import login_required

@login_required  # Ensure the user is logged in
def dashboard_view(request):
    return render(request, 'dashboard.html', {'user': request.user})

from django.contrib.auth import authenticate

class LoginApi(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            return Response({'status': 200, 'message': 'Login successful.'}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 400, 'message': 'Invalid username or password.'}, status=status.HTTP_400_BAD_REQUEST)
        
class RegisterApi(APIView):
    def post(self, request):
        try:
            data = request.data
            print("data is : ", data)
            serializer = UserSerializer(data = data)
            if serializer.is_valid():
                user = serializer.save()
                print(user)
                print(user.email)
                send_verfication_email(user.email)
                return Response({
                    'status': 200,
                    'message': 'Registration successfully. Check email.',
                    'data': serializer.data,
                }, status=status.HTTP_201_CREATED)
            return Response({
                    'status': 400,
                    'message': 'Invalid data. Please try again.',
                    'error': serializer.errors,
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({
                    'status': 500,
                    'message': 'Internal Server Error',
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class EmailAPI(APIView):
    def get(self, request):
        subject = self.request.GET.get('subject')
        txt_ = self.request.GET.get('text')
        html_ = self.request.GET.get('html')
        recipient_list = self.request.GET.get('recipient_list')
        from_email = settings.DEFAULT_FROM_EMAIL

        if subject is None and txt_ is None and html_ is None and recipient_list is None:
            return Response({'msg': 'There must be a subject, a recipient list, and either HTML or Text.'}, status=200)
        elif html_ is not None and txt_ is not None:
            return Response({'msg': 'You can either use HTML or Text.'}, status=200)
        elif html_ is None and txt_ is None:
            return Response({'msg': 'Either HTML or Text is required.'}, status=200)
        elif recipient_list is None:
            return Response({'msg': 'Recipient List required.'}, status=200)
        elif subject is None:
            return Response({'msg': 'Subject required.'}, status=200)
        else:
            sent_mail = send_mail(
            subject,
            txt_,
            from_email,
            recipient_list.split(','),
            html_message=html_,
            fail_silently=False,
            )
            return Response({'msg': sent_mail}, status=200)
        

class VerifyAccount(APIView):
    def get(self, request):
        token = request.query_params.get('token')
        try:
            # Validate the token
            UntypedToken(token)
            # If valid, redirect to the login page
            return redirect('log_in_view')  # Ensure this matches your URL name for the login page

        except TokenError:
            # If invalid, redirect to the signup page
            return redirect('sign_up_view')  # Ensure this matches your URL name for the signup page

        except Exception as e:
            return Response({
                'status': 500,
                'message': 'INTERNAL SERVER ERROR',
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Create your views here.

class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, World !'}
        return Response(content)


# class StudentModelViewSet (viewsets.ModelViewSet):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     # permission_classes = [IsAdminUser]
#     # permission_classes = [IsAuthenticated]

    # def get(self, request):
    #     # course = Student.objects.all()
    #     # serializer = StudentSerializer(course, many= True)
    #     # return JsonResponse(serializer.data, safe=False)
    #     content = {'message': 'Hello, World !'}
    #     return Response(content)
