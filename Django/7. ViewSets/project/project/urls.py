"""
URL configuration for project project.

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
from app import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

# router = DefaultRouter()
# router.register('Student_API', views.StudentModelViewSet, basename='Student')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    path('', include('app.urls')),
    # path('gettoken/', obtain_auth_token),
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify', TokenVerifyView.as_view(), name='token_verify'),
]

# http POST http://127.0.0.1:8000/obtain_token/ username="bilal" password="pakistan000"

# http POST http://127.0.0.1:8000/verify_token/ token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI3MzY3Mjk3LCJpYXQiOjE3MjczNjY2OTcsImp0aSI6IjA2N2MxMWIwYTQwNTRmOWVhNjQyNTVjNzE0YjgxY2QxIiwidXNlcl9pZCI6Mn0._GCAtps9jlrvARaCLQjpjTiiAQUWYtpmQoJIHyrTMk8