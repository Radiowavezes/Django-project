from django.contrib import admin
from .models import OrderItem, Order, CheckoutAddress

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'ordered_date', 'ordered')

class CheckoutAddressAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'zip', 'payment_option')

admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(CheckoutAddress, CheckoutAddressAdmin)