from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Transportation


class TransportationForm(forms.ModelForm):
    class Meta:
        model = Transportation
        fields = ['weight', 'current_location', 'destination']


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
