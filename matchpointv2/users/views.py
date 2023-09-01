from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def login_view(request):
    show_modal = False

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse("core:home"))

        else:
            show_modal = True

    return render(
        request,
        "users/login.html",
        {
            "active_nav": "login",
            "show_modal": show_modal,
        },
    )


def logout_view(request):
    logout(request)

    return redirect(reverse("core:index"))


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("core:home"))
    else:
        form = UserCreationForm()

    return render(request, "users/register.html", {"form": form})
