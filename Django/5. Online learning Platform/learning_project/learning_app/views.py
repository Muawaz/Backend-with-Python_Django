from django.shortcuts import render
import json

from .models import course_table, student_table, enrollment_table
from .serializer import CourseSerializer, StudentSerializer, EnrollmentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import io

from django.views.generic import View
from django.utils.decorators import method_decorator


# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class OnlineCourseApi(View):
    def get(self, request, *args, **kwargs):
        course_id = kwargs.get('id')
        if course_id:
            try:
                course = course_table.objects.get(course_id=kwargs.get('id'))
                serializer = CourseSerializer(course)
                return JsonResponse(serializer.data)
            except course_table.DoesNotExist:
                return JsonResponse({'error': 'Course not found'}, status=404)
        
        else:
            course = course_table.objects.all()
            serializer = CourseSerializer(course, many= True)
            return JsonResponse(serializer.data, safe=False)
        
    
    def post(self, request, *args, **kwargs):
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            serializer = CourseSerializer(data = python_data)
            if serializer.is_valid():
                serializer.save()
                res = {'msg': 'Course Data created'}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data, content_type='application/json')
            json_data = JSONRenderer().render(serializer.error_messages)
            return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def update_student(request, student_roll):
    if request.method == 'PUT':
        try:
            student = student_table.objects.get(roll = student_roll)
        except student_table.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)
        
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
        serializer = StudentSerializer(student, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Student updated successfully'}, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)

    
@csrf_exempt
def student_create_view(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Student Data created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.error_messages)
        return HttpResponse(json_data, content_type='application/json')
    
@csrf_exempt
def enrollment_create_view(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = enrollment_table(data = python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Enrollment Data created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.error_messages)
        return HttpResponse(json_data, content_type='application/json')
    



def get_all_students(request):
    if request.method == 'GET':
        students = student_table.objects.all()
        serializer = StudentSerializer(students, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
    else:
        return HttpResponse(status=405)
    
def get_students_by_course(request, course_id):
    print(course_id)
    if request.method == 'GET':
        try:
            course = course_table.objects.get(course_id=course_id)
        except course_table.DoesNotExist:
            return HttpResponse(JSONRenderer().render({ 'error': 'Course not found'}), content_type='application/json')
        enrollments = enrollment_table.objects.filter(course=course)
        students = [enrollment_table.student for enrollment in enrollments]
        serializer = StudentSerializer(students, many=True)
        json_data = JSONRenderer(). render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
    else:
        return HttpResponse(status=405)
    

def get_specific_student_in_course(request, course_id, student_roll):
    if request.method == 'GET':
        try:
            course = course_table.objects.get(course_id=course_id)
            student = student_table.objects.get(rollNo=student_roll)
            enrollment = enrollment_table.objects.get(course=course, student=student)
        except course_table.DoesNotExist:
            return HttpResponse(JSONRenderer().render({ 'error': 'Course not found'}), content_type='application/json')
        except student_table.DoesNotExist:
            return HttpResponse(JSONRenderer().render({ 'error': 'Student not found'}), content_type='application/json')
        except enrollment_table.DoesNotExist:
            return HttpResponse(JSONRenderer().render({ 'error': 'Student is not enrolled in the course'}), content_type='application/json')
        
        serializer = StudentSerializer(student)
        json_data = JSONRenderer(). render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
    else:
        return HttpResponse(status=405)
    