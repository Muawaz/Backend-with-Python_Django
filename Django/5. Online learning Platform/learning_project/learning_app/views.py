from django.shortcuts import render

from .models import course_table
from .serializer import course_serializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


# Create your views here.

def serializer_details(request):
    course = course_table.objects.all()
    serializer = course_serializer(course)
    json_data = JSONRenderer().render(serializer.data)
    
    return HttpResponse(json_data, content_type='application/json')
