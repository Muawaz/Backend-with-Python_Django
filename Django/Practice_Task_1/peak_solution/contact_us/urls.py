from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_view, name='user_view'),
    path('details/<int:id>/', views.user_details, name='user_details')
]