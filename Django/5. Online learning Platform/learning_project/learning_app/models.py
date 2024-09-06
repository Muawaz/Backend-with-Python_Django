from django.db import models

# Create your models here.

class course_table(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    instructor = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
