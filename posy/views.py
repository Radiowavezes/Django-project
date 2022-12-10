from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, UserRegistrationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Posy, Categories, Feedback
from django.urls import reverse
import logging
from datetime import datetime
from django.utils import timezone

# posy views

def home(request):
    goods = Posy.objects.all().order_by('-price')[:6]
    feedbacks = Feedback.objects.all()
    template = loader.get_template('home.html')
    context = {
        'goods': goods,
        'feedbacks': feedbacks,
    }
    return HttpResponse(template.render(context, request))

def shop(request):
    goods = Posy.objects.all()
    categories = Categories.objects.all()
    template = loader.get_template('shop.html')
    context = {
        'goods': goods,
        'categories': categories,
    }
    return HttpResponse(template.render(context, request))

# authentication views

@login_required
def index(request):
    return render(request, 'home.html', {})
    
def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password =  request.POST['password']
        user = authenticate(
    		    request, 
    		    username=username, 
    		    password=password
        )
        if user is None:
            return HttpResponse("Invalid credentials.")
        
        login(request, user)
        return redirect('/')
    
    else:
        form = UserForm()
        return render(request, 'login.html', {'form':form})
        
def signout(request):
        logout(request)
        return redirect('/')
        
def signup(request):
        if request.method=="POST":
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            newuser = User.objects.create_user(
                first_name=first_name, 
                last_name=last_name,
                username=username,
                password=password,
                email=email
            )
            try:
                newuser.save()
                login(request, authenticate(username=username, password=password))
                return HttpResponseRedirect(reverse('index'))
            except Exception as error:
                logging(error)
                return HttpResponse("Something went wrong.")
        else:
            form = UserRegistrationForm()
        return render(request, 'signup.html', {'form':form})  
           
# Feedback views
def leave_feedback(request):
    if request.method=="POST":
        full_name = request.POST['full_name']
        sender = request.POST['sender']
        phone = request.POST['phone']
        message = request.POST['message']
        now = datetime.now()
        daytime = now.strftime("%Y-%m-%d, %H:%M")
        new_feedback = Feedback(
            full_name=full_name, 
            sender=sender, 
            phone=phone, 
            message=message,
            daytime = daytime
        )
        new_feedback.save()
        return HttpResponseRedirect(reverse('home'))
