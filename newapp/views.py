from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Features

# Create your views here.
def index(request):
    features=Features.objects.all()
    return render(request,'index.html',{'features':features})

def counter(request):   
    posts = [1,2,3,'curtis','latte','godiva']
    return render(request,'counter.html',{'posts':posts})
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid username or email')
            return redirect('login')
    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def post(request, pk):
    return render(request,'post.html', {'pk':pk})

def register(request):
    if request.method == 'POST': 
        username = request.POST['username']
        password = request.POST['password']
        email    = request.POST['email']
        confirm_password    = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Email already exist')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password does not match')
            return redirect('register')
    else:
        return render(request,'register.html') 

