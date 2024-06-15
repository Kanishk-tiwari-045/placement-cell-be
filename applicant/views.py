from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import login
from django.http import HttpResponse
from .models import UserProfile

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            return HttpResponse("Redirected from applicant")
    else:
        form = UserRegisterForm()
    return render(request, 'applicant/register.html', {'form': form})


def index(request):
    return render(request, 'applicant/index.html')

def app(request):
    return render(request, 'applicant/app.html')

def organization_page(request):
    return HttpResponse("Welcome to organisarion")
