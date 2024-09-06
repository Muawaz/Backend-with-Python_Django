from django.contrib import admin
from .models import course_table

class course_admin(admin.ModelAdmin):
    list_display = ( 'title', 'description')
# Register your models here.
admin.site.register(course_table, course_admin)