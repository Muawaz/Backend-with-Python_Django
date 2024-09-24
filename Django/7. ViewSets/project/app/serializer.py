from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    class Meta:
        model: Student
        fields = ['rollNo', 'name,' 'city']