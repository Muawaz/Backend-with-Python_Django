from django.contrib import admin
from .models import course_table, student_table, enrollment_table

# class course_admin(admin.ModelAdmin):
#     list_display = ( 'title', 'description')
# # Register your models here.
# admin.site.register(course_table, course_admin)

@admin.register(student_table)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('rollNo', 'name', 'city')
    search_fields = ('rollNo', 'name', 'city')
    ordering = ('rollNo',)

@admin.register(course_table)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'duration')
    search_fields = ('title', 'instructor')
    ordering = ('title',)

@admin.register(enrollment_table)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrollment_date')
    search_fields = ('student__name', 'course__title')
    list_filter = ('course',)
    ordering = ('enrollment_date',)