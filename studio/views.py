from django.shortcuts import render, redirect


# HOMEPAGE
def index(request = "POST"):
    return render(request,'index.html')

def location(request = "POST"):
    return render(request,'location.html')

def register(request= "POST"):
    return render(request,'location.html')
def profile(request= "POST"):
    return render(request,'location.html')

def login(request= "POST"):
    return render(request,'location.html')

def contact(request="POST"):
    return render(request,'contact.html') 

