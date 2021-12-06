from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .models import Crud,User
from django.contrib import messages
from django.contrib.sessions.models import Session

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

def profile(request):
   if request.session.has_key('is_logged'):
     return render(request,'profile.html')
   else:
     return redirect('login')

def login(request):
    if request.session.has_key('is_logged'):
        return redirect('profile')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # SELECT * from user where username = username and password = password
        count = User.objects.filter(username=username,password=password).count()
        if count >0:
            # return HttpResponse("you are authenticated successfully.........")
            request.session['is_logged'] = True
            return redirect('profile')
        else:
            # return HttpResponse("invalid credential")
            messages.error(request,'Email Address Or Password Are Invalid')
            return redirect('login')    

    return render(request,'login.html') 

def signup(request):
    if request.session.has_key('is_logged'):
        return redirect('profile')
    if request.method =='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        data = User(username=username,email=email,password=password)
        data.save()
        messages.success(request,'Registration Successfull')
    return render(request,'signup.html')       


def logout(request):
    del request.session['is_logged']
    return redirect('login')
# def addshow(request):
#     if request.method =='POST':
#         Page_name=request.POST['Page_name']
#         Page_cat=request.POST['Page_cat']
#         page_publish_date=request.POST['page_publish_date']
#         Page.objects.create(Page_name=Page_name,Page_cat=Page_cat,page_publish_date=page_publish_date)
#         messages.success(request,'Data Has Been Added into database')
#     return render(request,'onetoone.html')
