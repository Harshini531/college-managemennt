from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

from studentapp.models import Student, Place


# Create your# views here
def home(request):
    return render(request,'base.html')
def login_fun(request):
    if request.method=="POST":
        name=request.POST["txtname"]
        password=request.POST["txtpassword"]
        User=authenticate(username=name,password=password)
        if User is not None:   #creditials = not none
            if User.is_superuser:
              return render(request,'home.html')
            else:
                return render(request, 'login.html', {'msg': True})
        else:
            return render(request,'login.html',{'msg':True})
        pass
    else:
         return render(request,'login.html',{'msg':False})
def sign_fun(request):
    if request.method=="POST":
        name=request.POST["txtname"]
        email=request.POST["txtemail"]
        password=request.POST["txtpassword"]
        if User.objects.filter(Q(username=name)|Q(email=email)|Q(password=password)).exists():
            data={'msg':True}
            return render(request,'sign page.html',data)
        else:
             user=User.objects.create_superuser(username=name,password=password,email=email)
             user.save()
             return redirect('log')

    return render(request,'sign page.html',{'msg':False})


def home_fun(request):
    return render(request,'home.html')


def display(request):
    d1=Student.objects.all()
    return render(request,'display.html',{"data":d1})


def logout(request):
    return render(request,'base.html')


def update_fun(request,id):
    c1 = Place.objects.all()
    s1 = Student.objects.get(id=id)
    if request.method == "POST":
        s1.Name = request.POST['txtName']
        s1.Place = Place.objects.get(city=request.POST['ddlplace'])
        s1.MobileNumber = request.POST['txtPhno']
        s1.Age = request.POST['txtAge']
        s1.Email = request.POST['txtEmail']
        s1.Gender = request.POST['txtGen']
        s1.save()
        return redirect('display')
    return render(request, 'update.html', {"d_data": s1,"data":c1})
def add_fun(request):
    c1 = Place.objects.all()
    if request.method == 'POST':
        s1 = Student()
        s1.Name = request.POST['txtName']
        s1.Place =Place.objects.get(city = request.POST['ddlplace'])
        s1.MobileNumber = request.POST['txtPhno']
        s1.Age = request.POST['txtAge']
        s1.Email = request.POST['txtEmail']
        s1.Gender = request.POST['txtGen']
        s1.save()
        return redirect('display')
    return render(request,'add.html',{'place':c1})


def delete_fun(request,id):
    c1 = Student.objects.get(id=id)
    c1.delete()
    return redirect('display')