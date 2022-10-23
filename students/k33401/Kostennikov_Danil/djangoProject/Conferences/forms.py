from django import forms
from django.core.exceptions import ValidationError

from Conferences.models import User, Сonference


class RegistrUser(forms.ModelForm):
    email = forms.CharField(max_length=50)
    password = forms.CharField(max_length=60)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ["email", "password", "first_name", "last_name"]


class LoginUser(forms.ModelForm):
    email = forms.CharField(max_length=50)
    password = forms.CharField(max_length=60)

    class Meta:
        model = User
        fields = ["email", "password"]


class ConferenceApply(forms.ModelForm):
    email = forms.CharField(max_length=50)
    password = forms.CharField(max_length=60)

    class Meta:
        model = Сonference
        fields = ["email", "password"]
