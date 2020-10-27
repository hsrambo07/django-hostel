from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponseRedirect
from django.template import loader, Context
from django.contrib import messages
from .forms import *
from .models import *
# Create your views here.
# Create your views here.


def home(request):
    return render(request,'home.html')


  
def student(request):  
    form = StuForm(request.POST)
    if form.is_valid():
        p = form.save()
        return render(request,'success.html')       
        
        # redirect to a new URL:
  # if a GET (or any other method) we'll create a blank form    

    return render(request, 'student.html', {'form': form})

def warden(request):  
    form = WardenForm(request.POST)
    if form.is_valid():
        p = form.save()
        return render(request,'success.html')       
        
        # redirect to a new URL:
  # if a GET (or any other method) we'll create a blank form    

    return render(request, 'warden.html', {'form': form})

def mess(request):  
    form = MessForm(request.POST)
    if form.is_valid():
        p = form.save()
        return render(request,'success.html')       
       
        # redirect to a new URL:
  # if a GET (or any other method) we'll create a blank form    

    return render(request, 'mess.html', {'form': form})

def block(request):  
    form = BlockForm(request.POST)
    if form.is_valid():
        p = form.save()
        return render(request,'success.html')       
        
        # redirect to a new URL:
  # if a GET (or any other method) we'll create a blank form    

    return render(request, 'block.html', {'form': form})

def parent(request):  
    form = PtForm(request.POST)
    if form.is_valid():
        p = form.save()
        return render(request,'success.html')       
        
        # redirect to a new URL:
  # if a GET (or any other method) we'll create a blank form    

    return render(request, 'parent.html', {'form': form})

def room(request):  
    form = RoomForm(request.POST)
    if form.is_valid():
        p = form.save()
        return render(request,'success.html')       
        
        # redirect to a new URL:
  # if a GET (or any other method) we'll create a blank form    

    return render(request, 'room.html', {'form': form})


def retrieve(request):
    student = Student.objects.all()
    reg = request.GET.get('reg','none')
    queryset = Student.objects.filter(reg_no__icontains=reg)
    data = { "detail" : student, "datas" : queryset,"error":"Enter correct values" }
    return render(request, 'retrieve.html', data)


        
