"""
URL configuration for learning_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from learning_app import views
from learning_app.views import OnlineCourseApi, OnlineStudentApi

urlpatterns = [
    path('admin/', admin.site.urls),

    path('course-create/', OnlineCourseApi.as_view(), name='course_create' ),
    path('courses/', OnlineCourseApi.as_view(), name='course_list'),
    path('courses/<int:id>', OnlineCourseApi.as_view(), name='course_by_id' ),

    path('student-create/', OnlineStudentApi.as_view(), name='student_create' ),
    path('students/', OnlineStudentApi.as_view(), name='student_create' ),
    path('students/<int:id>', OnlineStudentApi.as_view(), name='student_create' ),
    path('student-update/<int:id>', OnlineStudentApi.as_view(), name='student_create' ),
]
