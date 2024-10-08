from rest_framework import serializers
from .models import course_table, student_table, enrollment_table

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = course_table
        fields = ['title', 'description', 'instructor', 'duration']

class StudentSerializer(serializers.Serializer):
    class Meta:
        model: student_table
        fields = ['rollNo', 'name,' 'city']

class EnrollmentSerializer(serializers.Serializer):
    class Meta:
        model = enrollment_table
        fields = ['student', 'course', 'enrollment_date']

def validate_instructor_name(name):
    if not name.isalpha():
        raise serializers.ValidationError("Instructor name must only contain alphabets")
    return name

class CourseSerializer(serializers.Serializer):
    course_id = serializers.CharField(max_length=10)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    instructor = serializers.CharField(max_length=255, validators=[validate_instructor_name])
    duration = serializers.DurationField()

    def create(self, validate_data):
        return course_table.objects.create(**validate_data)

class StudentSerializer(serializers.Serializer):
    rollNo = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255)

    def create(self, validate_data):
        return student_table.objects.create(**validate_data)
    
    def update(self, instance, validate_data):
        instance.rollNo = validate_data.get('rollNo', instance.rollNo)
        instance.name = validate_data.get('name', instance.name)
        instance.city = validate_data.get('city', instance.city)
        instance.save()
        return instance
    
    def validate_rollNo(self, rollNo):
        if rollNo < 100:
            raise serializers.ValidationError("Roll no should be greater than 100")
        return rollNo

class EnrollmentSerializer(serializers.Serializer):
    student = serializers.PrimaryKeyRelatedField(queryset = student_table.objects.all())
    course = serializers.PrimaryKeyRelatedField(queryset = course_table.objects.all())
    enrollment_date = serializers.DateField(read_only=True)

    def create(self, validate_data):
        return enrollment_table.objects.create(**validate_data)