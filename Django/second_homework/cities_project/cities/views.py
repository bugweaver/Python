from django.shortcuts import render, redirect
from .models import Cities
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError


def index(request):
    cities = Cities.objects.all()
    return render(request, 'cities/index.html', {'cities': cities})


def signupuser(request):
    if request.method == "GET":
        return render(request, 'cities/signupuser.html', {'form': UserCreationForm()})

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'cities/signupuser.html',
                              {'form': UserCreationForm(), 'error': "Такое имя пользователя уже существует"})

        else:
            return render(request, 'cities/signupuser.html',
                          {'form': UserCreationForm(), 'error': "Пароли не совпадают"})
