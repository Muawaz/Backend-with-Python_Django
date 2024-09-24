from django.db import models

# Create your models here.
class Student(models.Model):
    rollNo = models.IntegerField(primary_key=True,default="101")
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
