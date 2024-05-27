from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.models import User

# Create your views here.
def hello(request):
    #Query Data From Model
    data=Post.objects.all()
    return render(request,'index.html',{'posts':data})

def page1(request):
    return render(request,'page1.html')

def createForm(request):
    return render(request,'form.html')

def addUser(request):
    username=request.POST['username']
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    email=request.POST['email']
    password=request.POST['password']
    repassword=request.POST['repassword']

    if password==repassword :
        if User.objects.filter(username=username).exists():
            print("UserName นี้มีคนใช้แล้ว")
            return redirect('/createForm')
        elif User.objects.filter(email=email).exists():
            print("Email นี้เคยลงทะเบียนแล้ว")
            return redirect('/createForm')
        else :
            user=User.objects.create_user(
        username=username,
        password=password,
        email=email,
        first_name=firstname,
        last_name=lastname
        )
        user.save()
        return redirect('/')
    else :
        return redirect('/createForm')