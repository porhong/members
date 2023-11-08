from django.shortcuts import render

# Create your views here.


def login(response):
    return render(response, "users/login.html", {})


def register(response):
    return render(response, "users/register.html", {})
