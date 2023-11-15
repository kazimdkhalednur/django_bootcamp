from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


def signup(request):
    form = CustomUserCreationForm()
    context = {
        "form": form
    }
    
    if request.method == "POST":
        form = CustomUserCreationForm(data=request.POST)
        if User.objects.filter(username=request.POST["username"]).exists():
            # messages.error(request, "Username Already exists")
            return render(request, "accounts/signup.html", context)
        
        if User.objects.filter(email=request.POST["email"]).exists():
            messages.error(request, "Email address Already exists")
            return render(request, "accounts/signup.html", context)

        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return render(request, "accounts/success.html")
        return render(request, "accounts/signup.html", context)
    else:
        context = {
            "form": form
        }
        return render(request, "accounts/signup.html", context)
    

def login(request):
    form = AuthenticationForm()
    context = {
            "form": form
        }
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("index")
        messages.error(request, "Invalid User")

    return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("index")

def index(request):
    context = {
        "message": "User Is unauthenticated"
    }
    if request.user.is_authenticated:
        context["message"] = "User Is authenticated"

    return render(request, "accounts/index.html", context)

