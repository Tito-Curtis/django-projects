from django.shortcuts import render, get_object_or_404,redirect,HttpResponse
from .models import meetings, room,All_Users
from django.forms import modelform_factory
from .forms import SignupForm
from django.contrib.auth.hashers import make_password, get_hasher
from django.contrib import messages


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
            for field,error in form.errors.items():
                error
                break
     
    else:
        form = SignupForm()
    return render(request,'sign_up.html', {'form':form})