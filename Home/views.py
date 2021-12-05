from django.shortcuts import render,redirect
from .models import Crud,Page
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

def addshow(request):
    if request.method =='POST':
        Page_name=request.POST['Page_name']
        Page_cat=request.POST['Page_cat']
        page_publish_date=request.POST['page_publish_date']
        Page.objects.create(Page_name=Page_name,Page_cat=Page_cat,page_publish_date=page_publish_date)
        messages.success(request,'Data Has Been Added into database')
    return render(request,'onetoone.html')
