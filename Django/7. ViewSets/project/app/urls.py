from django.urls import path
# from .views import StudentModelViewSet
from .views import *

urlpatterns = [
    path('', home_view, name='home_view'),
    path('sign_up/', sign_up_view, name='sign_up_view'),
    path('register/', RegisterApi.as_view(), name='register_api'),
    path ('verifyAccount/',VerifyAccount.as_view()),
    path('log_in/', log_in_view, name='log_in_view'),
    path('api/login/', LoginApi.as_view(), name='login_api'),
    path('dashboard/', dashboard_view, name='dashboard_view'),
    # path('check_sign_up/', views.check_sign_up, name='check_sign_up'),
    # path('details/', views.details_view, name='details_view'),
    # path('check_log_in/', views.check_log_in, name='check_log_in'),
]