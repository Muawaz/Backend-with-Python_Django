from django.db import models

class Users(models.Model):
  firstname = models.CharField(max_length=254)
  lastname = models.CharField(max_length=254)
  email = models.EmailField(max_length = 254)
  phone = models.CharField(max_length=254)