from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register-page'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('index/', views.index, name='index'),
    path('index/organization/', views.organization_page, name='organization_page'),
    # path('choose-user-type/', views.user_type, name='choose_user_type'),
    # path('create-user/', views.create_user, name='create_user'),
]
