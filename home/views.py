from django.shortcuts import render,redirect
from home.models import Data

def home(request):
    # return HttpResponse(" This is my Home page.")
    return render(request,'home.html')

def about(request):
    # return HttpResponse(" This is my about page.")
    return render(request,'about.html')

def projects(request):
    # return HttpResponse(" This is my projects page.")
    context = {'title':'Projects'}
    return render(request,'projects.html',context)

def contact(request):
    return render(request,'contact.html')

def contactA(request):
    x=request.POST['fname']
    y=request.POST['email']
    z=request.POST['message']
    mem = Data(fullname=x, email=y, message=z)
    mem.save()
    print("data saved")
    return redirect("/contact")

