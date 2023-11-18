from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import MyUser
from django.forms import ModelForm, TextInput, CharField, ValidationError, Form

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = MyUser
        fields = ['username', 'email', 'password1', 'password2']
        

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta(UserCreationForm):
        model = MyUser
        fields = ['old_password', 'new_password1', 'new_password2']