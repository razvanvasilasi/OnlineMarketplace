from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'type': 'text',
        'class': 'form-control'
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Email',
        'type': 'email',
        'class': 'form-control'
    }))

    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Password',
        'type': 'password',
        'class': 'form-control'
    }))

    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Confirm Password',
        'type': 'password',
        'class': 'form-control'
    }))

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'type': 'text',
        'class': 'form-control'
    }))

    password = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Password',
        'type': 'password',
        'class': 'form-control'
    }))