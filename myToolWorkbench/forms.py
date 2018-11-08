from django import forms
# from .models import User
from myToolWorkbench.models import Business
# https://docs.djangoproject.com/en/1.8/ref/forms/fields/
DAYS = (
    ('Mon', 'Monday'),
    ('Tue', 'Tuesday'),
    ('Wed', 'Wednesday'),
    ('Thu', 'Thursday'),
    ('Fri', 'Friday'),
    ('Sat', 'Saturday'),
    ('Sun', 'Sunday'),
)

# This will only run on runserver, need to pull the values some other way.....
def generate_business_list():
    b = []
    for i in Business.objects.all():
        print(i)
        b.append((str(i), str(i)))
    return b


class RegisterForm(forms.Form):
    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last Name", required=True)
    email_address = forms.EmailField(label="Email Address", required=True)
    username = forms.CharField(label="Username", required=True)
    password = forms.CharField(label="Password", required=True)
    password_conf = forms.CharField(label="Confirm Password", required=True)


class BusinessForm(forms.Form):
    name = forms.CharField(label='Business Name', required=True)
    address = forms.CharField(label='Address', required=True)
    owner_first = forms.CharField(label='Owner First Name', required=True)
    owner_last = forms.CharField(label='Owner Last Name', required=True)
    phone = forms.CharField(label='Phone Number', required=False)
    day = forms.CharField(label='Day Visited', widget=forms.Select(choices=DAYS), required=True)
    # day = forms.ChoiceField(label='Day Visited', choices=DAYS, widget=forms.RadioSelect, required=True)
    # day = forms.CharField(label='Day Visited', required=True)


class CustomerForm(forms.Form):
    first_name = forms.CharField(label='First Name', required=True)
    last_name = forms.CharField(label='Last Name', required=True)
    phone = forms.CharField(label='Phone Number', required=True)
    email = forms.EmailField(label='Email Address', required=True)
    # business = forms.CharField(label='Business Name', required=True)
    business = forms.CharField(label='Business Name', required=True, widget=forms.Select(choices=generate_business_list()))
