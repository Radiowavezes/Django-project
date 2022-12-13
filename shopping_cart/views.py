from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from posy.models import Product, Categories
from .components.cart import CartView

def cart(request):
    products = Product.objects.all()
    categories = Categories.objects.all()
    context = {
        "products": products,
        'categories': categories,
    }
    return render(request, "cart.html", context)

def confirm(request):
    basket = CartView.user_products
    context = {
        'basket': basket
    }
    return render(request, "confirm.html", context)
