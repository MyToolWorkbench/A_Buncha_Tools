from django import forms

# https://docs.djangoproject.com/en/1.8/ref/forms/fields/


class RegisterForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
