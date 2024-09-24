from django.db import models

# Create your models here.
class Student(models.Model):
    rollNo = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

