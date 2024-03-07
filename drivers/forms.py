from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Driver

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)
   
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        labels = {
            'username': 'Логин',
            'email': 'Почта',
            'password1': 'пароль',
            'password2': 'пароль еще раз',
        }
        help_texts = { 
            "username": '',
            "password1": '',
         }

class DriverForm(forms.ModelForm):
    birthday = forms.DateField(label='День рождения', widget=forms.DateInput(format='%d.%m.%Y'), input_formats=['%d.%m.%Y'])
    class Meta:
        model = Driver
        exclude = ["user", "is_available"]
