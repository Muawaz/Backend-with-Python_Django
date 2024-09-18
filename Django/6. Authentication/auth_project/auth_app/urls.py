from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('sign_up/', views.sign_up_view, name='sign_up_view'),
    path('log_in/', views.log_in_view, name='log_in_view'),
    path('check_sign_up/', views.check_sign_up, name='check_sign_up'),
    path('details/', views.details_view, name='details_view'),
    path('check_log_in/', views.check_log_in, name='check_log_in'),
]