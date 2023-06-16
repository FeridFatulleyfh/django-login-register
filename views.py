
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'signuperror.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('signup')
        else:
            return render (request,'signuperror.html', {'error':'Password does not match!'})
    else:
        return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password1'])
        if user is not None:
            auth.login(request,user)
            return redirect('blog')
        else:
            return render (request,'signuperror.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('')


def files(request):
    return render(request,"error.html")

def admin(request):
    return render(request,"error.html")

def index(request):
    return render(request,"index.html")

def index2(request):
    return render(request,"index.html")

def blog(request):
    return render(request,"blog.html")

def about(request):
    return render(request,"about.html")


def index1(request):
    return render(request,"index1.html")

def portfolio(request):
    return render(request,"portfolio.html")

def singleblog(request):
    return render(request,"single-blog.html")

def singleportfolio(request):
    return render(request,"single-portfolio.html")

def error(request):
    return render(request,"error.html")

def contact(request):
    return render(request,"contact.html")
