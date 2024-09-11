from django.db import models

# Create your models here.

class course_table(models.Model):
    course_id = models.IntegerField(primary_key=True,default="101")
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.CharField(max_length=255)
    duration = models.DurationField()

    def __str__(self):
        return self.title

class student_table(models.Model):
    rollNo = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def create(self, validate_data):
        return student_table.objects.create(**validate_data)

class enrollment_table(models.Model):
    student = models.ForeignKey(student_table, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(course_table, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateField()

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self) -> str:
        return f"{self.student.name} enrolled in {self.course.title}"    