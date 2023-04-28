from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Post,Profile
from datetime import datetime
from django.contrib.auth.decorators import login_required


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
                profile = Profile.objects.create(user=user)
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
    first_name = profile.first_name
    last_name = profile.last_name
    return render(request,'profile.html',{'posts': posts,'user': profile,'logged_in_user': request.user,'first':first_name,'last':last_name})

@login_required
def edit(request):
    user = request.user
    if request.method == 'POST':
        user.first_name = request.POST.get('firstName')
        user.last_name = request.POST.get('lastName')
        user.profile.bio = request.POST.get('bio')
        user.save()
        user.profile.save()
        return redirect('/')
    return render(request,'edit.html',{'user': user,'profile': profile,'name': user.username})

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