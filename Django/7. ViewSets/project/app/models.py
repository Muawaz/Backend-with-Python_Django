from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Create your models here.
class Student(models.Model):
    rollNo = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"
    
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    def name(self):
        return self.first_name + " " + self.last_name
    def __str__(self):
        return self.email
    
    # Set related_name for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Change this to whatever you prefer
        blank=True,
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # Change this as well
        blank=True,
    )
