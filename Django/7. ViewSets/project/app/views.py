from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializer import StudentSerializer
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
        # subject = 'Account Verification'
        # txt_ = f'Click the link below to verify your account:\n'
        # from_email = settings.DEFAULT_FROM_EMAIL
        # # recipient_list = self.request.GET.get('recipient_list')
        # json_data = request.body
        # stream = io.BytesIO(json_data)
        # python_data = JSONParser().parse(stream)
        # recipient_list = python_data
        # print("txt_ : ", txt_)
        # print("from_email : ", from_email)
        # print("recipient_list : ", recipient_list)
        



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
