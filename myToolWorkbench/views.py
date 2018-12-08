from datetime import date
import calendar

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.models import User
from django.views import generic
from django.http import HttpResponseRedirect

from myToolWorkbench.forms import RegisterForm, BusinessForm, CustomerForm, InventoryForm
from myToolWorkbench.models import UserAccount, Business, Person, ToolInstance, Tool, Workbench


# Runs when user logs in, authenticates user and reroutes to dashboard
def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'myToolWorkbench/')
    else:
        return render(request, AccessMixin.get_login_url())


# Ends user's myToolWorkbench session
def logout_view(request):
    logout(request)


# Serves up registration form on GET request
# Validates and processes registration information on POST request
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
            # Return error if username exists or password confirmation does not match
            if User.objects.filter(username=username).exists():
                print("User " + username + " already exists")
            elif pass1 != pass2:
                print("Entered passwords do not match")
            else:
                user = User.objects.create_user(username, email, pass1)
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                # Create UserAccount object to link with authenticated user object
                user_account = UserAccount.objects.create(user=user)
                # Create user inventory/workbench
                workbench = Workbench.objects.create(user=user)
                workbench.save()
                user_account
                user_account.save()
                # Reroute to login page after successful account creation
                return HttpResponseRedirect('/myToolWorkbench/login')
        else:
            print(form.errors)

    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {
        'form': form
    })


# Serves dashboard view's businesses for the current day
class DashboardView(generic.ListView):
    template_name = 'dashboard.html'
    context_object_name = 'today_business_list'

    def get_queryset(self):
        today = date.today()
        today_str = calendar.day_name[today.weekday()]
        user = self.request.user
        return Business.objects.filter(day_visited=today_str[:3]).filter(created_by=user)


# Serves list of all businesses created by user
class BusinessView(generic.ListView):
    template_name = 'people.html'
    context_object_name = 'business_list'

    def get_queryset(self):
        user = self.request.user
        return Business.objects.filter(created_by=user)


# Serves details of business objects
class BusinessDetailView(generic.DetailView):
    model = Business
    template_name = 'business-details.html'

    def get_queryset(self):

        return Business.objects.all()


# Return all tools in the workbench belonging to current user
class InventoryView(generic.ListView):
    template_name = 'inventory.html'
    context_object_name = 'inventory'

    def get_queryset(self):
        workbench = Workbench.objects.filter(user=self.request.user)[:1].get()
        tools = ToolInstance.objects.filter(inventory=workbench)

        print("Bench id: " + str(workbench))
        print("# tools: " + str(len(tools)))
        return tools


# Request handler for creating new business
# Returns business create form on GET request
# Processes business create form on POST request
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
            # Make sure business with same name has not already been created by user
            if Business.objects.filter(name=name).filter(created_by=request.user).exists():
                print("Business " + name + " already exists")
            else:
                business = Business.objects.create()
                business.name = name
                business.address = address
                business.owner_first=owner_first
                business.owner_last = owner_last
                business.phone_number = phone
                business.day_visited = day
                business.created_by = request.user
                business.save()
                return HttpResponseRedirect('/myToolWorkbench/people')
    else:
        form = BusinessForm()
    return render(request, 'add-business.html', {
        'form': form
    })


# Request handler for creating new business customer
# Returns customer create form on GET request
# Processes customer create form on POST request
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

            # Create link between new customer(models.Person) and Business object
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

# Request handler for creating new tool item
# Returns tool item create form on GET request
# Processes tool item create form on POST request
def add_inventory(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            part_number = form.cleaned_data.get('part_number')

            if ToolInstance.objects.filter(tool_id= Tool.objects.get(part_number=part_number)).exists():
                # Currently ignoring this case
                pass
                #ToolInstance.objects.filter(tool_id= Tool.objects.get(part_number=part_number)).inventory += 1
            else:
                # Create tool instance based on part data and add to user's workbench
                tool = ToolInstance.objects.create()
                tool.tool_id = Tool.objects.get(part_number=part_number)
                tool.inventory = Workbench.objects.filter(user=request.user)[:1].get()
                tool.save()
        return HttpResponseRedirect('/myToolWorkbench/inventory')
    else:
        form = InventoryForm()
    return render(request, 'add-inventory.html', {
        'form': form
    })
