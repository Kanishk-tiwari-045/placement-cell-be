# urls.py

from django.urls import path
from .views import OrganizationRegisterView, VerifyOTPView

urlpatterns = [
    path('register/', OrganizationRegisterView.as_view(), name='organization-register'),
    path('verify/', VerifyOTPView.as_view(), name='verify-otp'),
]
