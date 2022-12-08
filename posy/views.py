from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Posy, Categories
from django.views import View

def home(request):
    goods = Posy.objects.all().order_by('-price')[:6]
    template = loader.get_template('home.html')
    context = {
        'goods': goods
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
           
