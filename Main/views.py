from django.shortcuts import render, redirect, HttpResponse

def home(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')

def signout(request):
    pass
