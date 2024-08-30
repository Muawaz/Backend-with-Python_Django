from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('log_in/', views.log_in_view, name='log_in_view'),
    path('sign_up/', views.sign_up_view, name='sign_up_view')
]