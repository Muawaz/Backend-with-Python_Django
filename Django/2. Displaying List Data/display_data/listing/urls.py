from django.urls import path
from . import views

urlpatterns = [
    path('', views.listing_view, name='listing_view'),
    path('post/<int:post_id>/', views.listing_detail_view, name='listing_detail_view')
]