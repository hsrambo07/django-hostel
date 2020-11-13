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
    id1 = request.GET.get('del','none')
    print(reg)
    print(id1)
    Student.objects.filter(reg_no = id1).delete()
    queryset = Student.objects.filter(reg_no__icontains=reg)
    data = { "detail" : student, "datas" : queryset,"error":"Enter correct values" }
    return render(request, 'retrieve.html', data)

def delete(request):
    id1 = request.GET.get('del','none')
    Student.objects.filter(reg_no = id1).delete()
    return HttpResponseRedirect('/info/retrieve')

'''def update(request):
    model=Student

    if request.method=='POST':
        
        form = UpdateStudentForm(data=request.POST)
        id1 = '19BCT0048'
        #The user wants to signup                
        if form.is_valid():
            cd=form.cleaned_data
            new_item=form.save(commit=False)
            new_item.name=Student.objects.filter(reg_no = id1)
            new_item.save()
            form.save()
            messages.success(request,'Successfully uploaded')
            return HttpResponseRedirect('/info/retrieve')

    else:
        form=UpdateStudentForm(data=request.GET)
    return render(request,'edit.html',{'form':form})
'''
def update(request):
    reg = request.GET.get('update')
    queryset = Student.objects.filter(reg_no = reg)
    id1 = request.GET.get('reg')
    print(id1)
    name = request.GET.get('name')
    print(request.GET.get('name'))
    student = Student.objects.filter(reg_no=id1).update(s_name=name)
    print(student)
    return render(request,'edit.html',{'reg' : reg, 'name' : queryset})
