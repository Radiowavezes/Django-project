from django.contrib import admin
from .models import OrderItem, Order, CheckoutAddress

admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(CheckoutAddress)