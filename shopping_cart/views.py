from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from posy.models import Product, Categories
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

def cart(request):
    products = Product.objects.all()
    categories = Categories.objects.all()
    context = {
        "products": products,
        'categories': categories,
    }
    return render(request, "cart.html", context)
