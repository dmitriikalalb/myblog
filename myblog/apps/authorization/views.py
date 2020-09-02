from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreateUserForm
from django.core.paginator import Paginator


def index(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    else:
        return render(request, 'index.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    else:
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('authorization:login')
        else:
            form = CreateUserForm()
    return render(request, 'registration/register.html', {'form': form})


def login_user(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            userr = authenticate(request, username=username, password=password)
            if userr is not None:
                login(request, userr)
                return redirect('articles:index')
            else:
                messages.info(request, 'Неправильный логин или пароль')
        context = {}
        return render(request, 'registration/login.html', context)
