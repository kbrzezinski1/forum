from django.contrib.auth.forms import UserCreationForm
from .models import MyUser
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = MyUser
        fields = ['username', 'email', 'password1', 'password2']
