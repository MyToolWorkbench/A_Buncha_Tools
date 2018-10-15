from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import AccessMixin

from myToolWorkbench.forms import RegisterForm


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'myToolWorkbench/')
    else:
        return render(request, AccessMixin.get_login_url())


def logout_view(request):
    logout(request)


def register(request):
    form_class = RegisterForm

    return render(request, 'register.html', {
        'form': form_class,
    })