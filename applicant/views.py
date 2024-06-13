from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserProfileForm
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


@login_required
def profile(request):
    if request.method == 'POST':
        p_form = UserProfileForm(request.POST, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            return HttpResponse("Redirected from applicant")
    else:
        p_form = UserProfileForm(instance=request.user.profile)
    
    context = {
        'p_form': p_form
    }
    return render(request, 'applicant/profile.html', context)


def index(request):
    return render(request, 'applicant/index.html')

def app(request):
    return render(request, 'applicant/app.html')

def organization_page(request):
    return HttpResponse("Welcome to organisarion")
