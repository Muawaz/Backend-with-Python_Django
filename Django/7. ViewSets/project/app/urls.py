from django.urls import path
# from .views import StudentModelViewSet
from .views import Home

urlpatterns = [
    # path('', StudentModelViewSet.as_view()),
    path('', Home.as_view()),
]