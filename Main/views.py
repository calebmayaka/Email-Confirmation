from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login

def home(request):
    return render(request, 'Main/home.html')

def signup(request):
    if request.method == 'POST':
        # Take all the fields and assign them to the users
        username = request.POST['username']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        emailaddress = request.POST['email']
        Password = request.POST['pass1']
        Password2 = request.POST['pass2']
        
        myUser = User.objects.create_user(username, emailaddress, Password)
        myUser.first_name = firstname
        myUser.last_name = lastname
        
        myUser.save()
        
        messages.success(request, "Your Account has been sucessfully created")
        return redirect('signin')
    return render(request, 'Main/Signup.html')

def signin(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['pass1']
        
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return render(request, "Main/home.html")
        else: 
            messages.error(request, 'Wrong Username or password')
            return redirect('signup.html')
    
    return render(request, 'Main/signin.html')

def signout(request):
    pass
