from django.shortcuts import render,redirect
from .models import Crud
from django.contrib import messages

# Create your views here.
def home(request):
    data = Crud.objects.all()
    return render(request,'home.html',{'data':data})

def add(request):
    return render(request,'add.html')

def about(request):
    return render(request,'about.html')

def insert(request):
    if request.method =='POST':
        name=request.POST['name']
        email=request.POST['email']
        address=request.POST['address']
        Crud.objects.create(name=name,email=email,address=address)
        messages.success(request,'Data Has Been Added into database')
    return render(request,'add.html')  


def update(request,id):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        address=request.POST['address']
        Crud.objects.filter(id=id).update(name=name,email=email,address=address)
        messages.success(request,'Data Has Been Updated into database')
    data=Crud.objects.get(id=id)
    return render(request,'update.html',{'data':data})


def delete(request,id):
    Crud.objects.filter(id=id).delete()
    return redirect('/')