from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic. list import ListView
from .models import User
# Create your views here.


class loginpage(ListView):
    model = User
