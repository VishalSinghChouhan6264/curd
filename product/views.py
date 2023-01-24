from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'page-index-1.html')
def login(request):
    return render(request,'page-user-login.html')
def register(request):
    return render(request,'navbar.html')