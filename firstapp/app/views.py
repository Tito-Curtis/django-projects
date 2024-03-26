from django import forms
from django.shortcuts import render, get_object_or_404,redirect,HttpResponse
from .models import meetings, room,All_Users
from django.forms import ValidationError, modelform_factory
from .forms import SignupForm, LoginForm
from django.contrib.auth.hashers import make_password, get_hasher,check_password
from django.contrib import messages
from django.contrib.auth import authenticate,login


# Create your views here.
MeetingForm = modelform_factory(meetings, exclude=[])

def index(request):
    meeting = meetings.objects.all()
    return render(request,'index.html',{'meeting':meeting})

def details(request,id):
    meeting = meetings.objects.get(pk=id)

    return render(request,'details.html',{'meeting':meeting})
def all_room(request):
    rooms = room.objects.all()
    return render(request,'room.html',{'rooms':rooms})
def new(request):
    if request.method == "POST":
        return HttpResponse('form is on method post')
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    
    else:  
        form=MeetingForm()
    return render(request,'form.html',{'form':form})

def signUp_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid(): #p
            form.save()
            return redirect('index')    
    else:
        form = SignupForm()
    return render(request,'sign_up.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            email = email.lower()
            print("Email:", email) 
            print("Password:", password)
            user = authenticate(request,email=email,password=password) 
            print("user:", user)                     
            if user is not None:         
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, 'invalid username or password')
       
            
    else:
        
        form = LoginForm()
      
    return render(request,'login.html', {'form':form})