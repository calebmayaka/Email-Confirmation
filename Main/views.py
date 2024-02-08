from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.contrib.models import user

def home(request):
    if request.method == 'POST':
        # Take all the fields and assign them to the users
        username = request.POST['username']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        emailaddress = request.POST['email']
        Password = request.POST['pass1']
        Password2 = request.POST['pass2']
        
        
        
        
    
    
    
    
    
        return render(request, 'Main/home.html')

def signup(request):
    return render(request, 'Main/signup.html')

def signin(request):
    return render(request, 'Main/signin.html')

def signout(request):
    pass
