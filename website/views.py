from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse(request, "website/index.html")

def register(request):
    return render(request, "website/register.html")

def login(request):
    return render(request, "website/login.html")

def logout(request):
    pass
  

