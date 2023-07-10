from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(req):
    #Check to see if logging in
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        #Authenticate 
        user = authenticate(req, username=username, password=password)
       
        if user is not None:
            login(req, user)
            messages.success(req, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.success(req, "There was an error logging in, please try again..")
            return redirect('home')
    else: 
        return render(req, 'home.html', {})


def logout_user(req):
    logout(req)
    messages.success(req, "You Have Been Logged Out...")
    return redirect('home')

def register_user(req):
    return render(req, 'register.html', {})

