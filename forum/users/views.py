from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import CustomUserCreationForm
from django.contrib import messages

def register(request):
    if request.method == "GET":
        return render(
            request, "register.html", {"form": CustomUserCreationForm}
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
                request, "register.html", {"form": CustomUserCreationForm}
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
        return render(request, "login.html", {})
