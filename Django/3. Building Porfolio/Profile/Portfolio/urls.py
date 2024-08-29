from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home_page, name='Home_page'),
    path('contact_us/', views.Contact_us_form, name='Contact_us_form'),
    path('submit/', views.form_submission, name='form_submission')
]