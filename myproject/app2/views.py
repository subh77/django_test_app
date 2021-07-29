from os import name
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.urls import reverse
from .models import Features

# Create your views here.
def index(request):
    feature = Features.objects.all()
    return render(request, "index.html", {"feature": feature})


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Exists")
                return HttpResponseRedirect("register")
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Used")
                return HttpResponseRedirect("register")
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password
                )
                user.save()
                return HttpResponseRedirect("login")
        else:
            messages.info(request, "Password is not same")
            return HttpResponseRedirect("register")
    else:
        return render(request, "register.html")

    # return render(request, "register.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect("/app2")
        else:
            messages.info(request, "Credential Invalid")
            return HttpResponseRedirect("login")
    else:
        return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/app2")


def counter(request):
    words = request.POST["words"]
    word_counter = len(words.split())
    return render(request, "counter.html", {"count": word_counter})
