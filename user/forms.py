from django import forms
from .models import CustomUserModel
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = ('username','email','image')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63,widget=forms.PasswordInput)