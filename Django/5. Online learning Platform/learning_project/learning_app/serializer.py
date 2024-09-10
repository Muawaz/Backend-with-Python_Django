from rest_framework import serializers
from .models import course_table, student_table

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = course_table
        fields = ['title', 'description', 'instructor', 'duration']

class CourseSerializer(serializers.Serializer):
    course_id = serializers.CharField(max_length=10)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    instructor = serializers.CharField(max_length=255)
    duration = serializers.DurationField()

class StudentSerializer(serializers.Serializer):
    rollNo = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255)

class EnrollmentSerializer(serializers.Serializer):
    student = serializers.PrimaryKeyRelatedField(queryset = student_table.objects.all())
    course = serializers.PrimaryKeyRelatedField(queryset = course_table.objects.all())
    enrollment_date = serializers.DateField(read_only=True)