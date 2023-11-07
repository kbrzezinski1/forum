from django.contrib.auth.forms import UserCreationForm
from .models import MyUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = MyUser
        fields = ['username', 'email', 'password1', 'password2']