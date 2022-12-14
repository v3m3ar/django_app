from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput


class RegisterForm(UserCreationForm):

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={'class': 'p-2 border-b-2', 'placeholder': 'Введите пароль', "autocomplete": "new-password"}),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'class': 'p-2 rounded-b-xl border-b-2', 'placeholder': 'Повторите пароль',
                                          "autocomplete": "new-password"}),
        strip=False,
    )

    class Meta:
        model = User
        fields = ["username", 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            "username": TextInput(attrs={
                'class': 'p-2 rounded-t-xl border-b-2',
                'required': True,
                'placeholder': 'Введите логин',
            }),
            "first_name": TextInput(attrs={
                'class': 'p-2 border-b-2',
                'required': True,
                'placeholder': 'Введите имя',
            }),
            "last_name": TextInput(attrs={
                'class': 'p-2 border-b-2',
                'required': True,
                'placeholder': 'Введите фамилию',
            }),
            "email": EmailInput(attrs={
                'class': 'p-2 border-b-2',
                'required': True,
                'placeholder': 'Введите почту',
            })
        }
