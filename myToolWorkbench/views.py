from datetime import date
import calendar

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.models import User
from django.views import generic
from django.http import HttpResponseRedirect

from myToolWorkbench.forms import RegisterForm, BusinessForm, CustomerForm
from myToolWorkbench.models import UserAccount, Business, Person


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
                return HttpResponseRedirect('/myToolWorkbench/login')
        else:
            print(form.errors)

    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {
        'form': form
    })


class DashboardView(generic.ListView):
    template_name = 'dashboard.html'
    context_object_name = 'today_business_list'

    def get_queryset(self):
        today = date.today()
        today_str = calendar.day_name[today.weekday()]
        return Business.objects.filter(day_visited=today_str[:3])


class BusinessView(generic.ListView):
    template_name = 'people.html'
    context_object_name = 'business_list'

    def get_queryset(self):
        return Business.objects.all()


class BusinessDetailView(generic.DetailView):
    model = Business
    template_name = 'business-details.html'

    def get_queryset(self):
        return Business.objects.all()


def create_business(request):
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            address = form.cleaned_data.get('address')
            owner_first = form.cleaned_data.get('owner_first')
            owner_last = form.cleaned_data.get('owner_last')
            phone = form.cleaned_data.get('phone')
            day = form.cleaned_data.get('day')

            if Business.objects.filter(name=name).exists():
                print("Business " + name + " already exists")
            else:
                business = Business.objects.create()
                business.name = name
                business.address = address
                business.owner_first=owner_first
                business.owner_last = owner_last
                business.phone_number = phone
                business.day_visited = day
                business.save()
    else:
        form = BusinessForm()
    return render(request, 'add-business.html', {
        'form': form
    })


def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            phone = form.cleaned_data.get('phone')
            email = form.cleaned_data.get('email')
            business = form.cleaned_data.get('business')

            person = Person.objects.create()
            person.first_name = first_name
            person.last_name = last_name
            person.phone_number = phone
            person.email_address = email
            person.save()

            if Business.objects.filter(name=business).exists():
                b1 = Business.objects.get(name=business)
                e1 = Employed(person=person, business=b1)
                e1.save()
            else:
                print("Business " + business + "does not exist yet. Please create the business first.")
    else:
        form = CustomerForm()
    return render(request, 'add-customer.html', {
        'form': form
    })
