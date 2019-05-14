from django.contrib.auth.forms import UserCreationForm, UsernameField
from django import forms

from wykop.accounts.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}


class ConfirmTosForm(forms.Form):
    confirm = forms.BooleanField(required=True)
