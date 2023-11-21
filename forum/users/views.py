from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import CustomUserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from forums.models import Post, Topic
def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html", {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect(reverse("dashboard"))
        else:
            for error in form.errors:
                messages.error(request, form.errors[error])
            return render(
                request, "users/register.html", {"form": CustomUserCreationForm}
            )
        
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.success(request, ("There was an error in your login form. Please try again"))
            return redirect('login')

    else: 
        return render(request, "users/login.html", {})
    
def profile(request):
    posts = Post.objects.filter(user_id=request.user)
    topics = Topic.objects.filter(user_id=request.user)
    return render(request, "users/profile.html", {"topics": topics, "posts" : posts})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('dashboard')
        else:
            for error in form.errors:
                messages.error(request, form.errors[error])
            return redirect('change_password')
    
    return render(request, "users/password_change_form.html", {'form' : PasswordChangeForm})

