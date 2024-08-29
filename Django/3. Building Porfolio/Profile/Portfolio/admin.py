from django.contrib import admin
from .models import Portfolio_model

# Register your models here.
# class Portfolio_Admin(admin.ModelAdmin):
#     list_display = ("name", "email")

# admin.site.register(Portfolio_model, Portfolio_Admin)

admin.site.register(Portfolio_model)