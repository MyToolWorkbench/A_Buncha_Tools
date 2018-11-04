from django import forms

# https://docs.djangoproject.com/en/1.8/ref/forms/fields/


class RegisterForm(forms.Form):
    name = forms.CharField(label="Name", required=True)
    email_address = forms.EmailField(label="Email Address", required=True)
    username = forms.CharField(label="Username",required=True)
    password = forms.CharField(label="Password")
    password_conf = forms.CharField(label="Confirm Password")
