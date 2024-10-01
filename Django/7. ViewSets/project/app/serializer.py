from rest_framework import serializers
from .models import Student, User

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['rollNo', 'name', 'city']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'is_verified']

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user