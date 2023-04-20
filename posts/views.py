from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Post,profile
from datetime import datetime

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post(request,pk):
    post = Post.objects.get(id=pk)
    return render(request, 'post.html', {'post':post})

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['confirmPassword']
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Passwords do not match')
            return redirect('signup')

    return render(request,'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if User is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Username not registered')
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def profile(request,name):
    posts = Post.objects.all()
    profile = User.objects.get(username=name)
    return render(request,'profile.html',{'posts': posts,'user': profile})


def edit(request,name):
    user = User.objects.get(username=name)
    if request.method == 'POST':
        return redirect('/')
    return render(request,'edit.html',{'user': user})

def new(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = User.objects.get(username=request.user.username)
        post_time = datetime.now()
        post = Post.objects.create(title=title,content=content,author=author,post_time=post_time)
        post.save()
        return redirect('index')
    return render(request,'new.html')

def delete(request,id):
    if request.method == 'POST':
        post = Post.objects.get(id=id)
        post.delete()
        return redirect('index')
    return render(request,'delete.html',{'id':id})

def cancel(request):
    if request.method == 'POST':
        return redirect('index')
    return render(request,'cancel.html')