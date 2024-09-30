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
