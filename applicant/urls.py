from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register-page'),
    path('profile/', views.profile, name='profile-page'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('index/', views.index, name='index'),
    path('index/app/', views.app, name='applicant_page'),
    path('index/organization/', views.organization_page, name='organization_page'),
]
