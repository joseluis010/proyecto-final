from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
        }


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
        }



from django import forms
from .models import Pais, Ciudad

class AgregarInformacionForm(forms.Form):
    pais = forms.CharField(label='País', max_length=100)
    ciudad = forms.CharField(label='Ciudad', max_length=100)
    calle = forms.CharField(label='Calle', max_length=100)

class BuscarForm(forms.Form):
    pais = forms.CharField(label='País', max_length=100)
    ciudad = forms.CharField(label='Ciudad', max_length=100)
