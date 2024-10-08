from django.db import models

# Create your models here.
class auth_model(models.Model):
    userName = models.CharField(max_length=255)
    firstName = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.firstName}"