from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Todo
from . import models
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required




# Create your views here.
def signup(request):
    if request.method == "POST":
        fnm = request.POST.get("fnm")
        emailid = request.POST.get("emailid")
        pwd = request.POST.get("pwd")

        if User.objects.filter(username=fnm).exists():
            messages.error(request, "Username already taken. Please choose another.")
            return render(request, 'signup.html')
        
        if User.objects.filter(email=emailid).exists():
            messages.error(request, "email already taken. Please choose another.")
            return render(request, 'signup.html')
        
        try:
            my_user = User.objects.create_user(username=fnm, email=emailid, password=pwd)
            my_user.save()

            messages.success(request, "Registration successful! You can now log in.")
            return redirect('/login')  # Redirect to the login page or home page
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
    return render (request, 'signup.html')




def loginn(request):
    if request.method=="POST":
        fnm=request.POST.get("fnm")
        pwd=request.POST.get("pwd")
        userr= authenticate(username=fnm, password=pwd)
        if userr is not None:
            login(request, userr)
            return redirect('/todopage')
        else:
            messages.success(request, "Username or Password  is invalid.")
            return redirect('/login')

    return render (request, 'loginn.html')

@login_required(login_url='/loginn')
def todo(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        print(title)
        obj=models.Todo(title=title,user=request.user)
        obj.save()
        user=request.user        
        res=models.Todo.objects.filter(user=user).order_by('-date')
        return redirect('/todopage',{'res':res})
        
    
    res=models.Todo.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html',{'res':res,})



def delete_todo(request,seno):
    obj=models.Todo.objects.get(seno=seno)
    obj.delete()
    return redirect('/todopage')

@login_required(login_url='/loginn')
def edit_todo(request, seno):
    if request.method == 'POST':
        title = request.POST.get('title')
        obj = models.Todo.objects.get(seno=seno)
        obj.title = title
        obj.save()
        return redirect('/todopage')

    obj = models.Todo.objects.get(seno=seno)
    return render(request, 'edit_todo.html', {'obj': obj})



def signout(request):
    logout(request)
    return redirect('/loginn')