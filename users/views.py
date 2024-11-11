from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import User
from django.contrib.auth import login as django_login, authenticate

from django.shortcuts import render, redirect

def sign_up(request):
    username = request.POST['username']
    password1 = request.POST['password1']
    password2 = request.POST['password2']

    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(settings.LOGIN_URL)

    context = {
        'form': form
    }
    return render(request, 'registration/signup.html', context)

def login(request):
    form = AuthenticationForm(request, request.post or None)
    if form.is_valid():
        django_login(request, form.get_user())
        return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'registration/login.html', context)
