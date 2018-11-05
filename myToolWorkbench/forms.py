from django import forms
from .models import User
# https://docs.djangoproject.com/en/1.8/ref/forms/fields/


class RegisterForm(forms.Form):
    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last Name", required=True)
    email_address = forms.EmailField(label="Email Address", required=True)
    username = forms.CharField(label="Username", required=True)
    password = forms.CharField(label="Password", required=True)
    password_conf = forms.CharField(label="Confirm Password", required=True)
