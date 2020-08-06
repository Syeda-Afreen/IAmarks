from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def handleLogin(request):
    return render(request,'login.html')

def handleSignup(request):
    return render(request,'signup.html')