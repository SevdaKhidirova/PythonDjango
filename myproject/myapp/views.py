from django.shortcuts import render, redirect,reverse
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Services
from  django import *

def simple_middleware(get_response):
    def middleware(request):
        response = get_response(request)
        return response

    return middleware

def index(request):
    servicels = Services.objects.all()

    return render(request, 'index.html', {'servicels': servicels})


def portfolio_details(request):
    return render(request, 'portfolio_details.html')


def counter(request):
    return render(request, 'counter.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        reppassword = request.POST['repeat_pass']

        if password==reppassword:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email already used")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username is already exists')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Passwords does not match')
            return redirect('register')
    else:
        messages.info(request,'yene burdasan')
        return render(request, 'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Credientails invalid')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def post(request,pk):
    return render(request,'post.html',{'pk':pk})







def page404(request):
    return render(request, '404.html')


def notfound(request,exception):
    data = {}
    return render(request,'notfound.html', data)