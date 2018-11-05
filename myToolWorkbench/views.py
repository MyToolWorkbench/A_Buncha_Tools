from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.models import User

from myToolWorkbench.forms import RegisterForm
from myToolWorkbench.models import UserAccount


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
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email_address')
            pass1 = form.cleaned_data.get('password')
            pass2 = form.cleaned_data.get('password_conf')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')

            if User.objects.filter(username=username).exists():
                print("User " + username + " already exists")
            elif pass1 != pass2:
                print("Entered passwords do not match")
            else:
                user = User.objects.create_user(username, email, pass1)
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                user_account = UserAccount.objects.create(user=user)
                user_account
                user_account.save()


    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {
        'form': form
    })
