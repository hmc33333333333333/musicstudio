from django.shortcuts import render, redirect


# HOMEPAGE
def index(request = "POST"):
    return render(request,'index.html')

def location(request = "POST"):
    return render(request,'location.html')

def register(request= "POST"):
    return render(request,'register.html')
def profile(request= "POST"):
    return render(request,'profile.html')

def login(request= "POST"):
    return render(request,'login.html')

def contact(request="POST"):
    return render(request,'contact.html')

def about(request="POST"):
    return render(request,'about.html')

def video(request="POST"):
    return render(request,'video.html')

