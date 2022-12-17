from django.contrib import admin
from store.models.order import Order
from store.models.order_item import OrderItem
from store.models.checkout_adress import CheckoutAddress
from store.models.composition import CreateComposition


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'ordered_date', 'ordered')

class CheckoutAddressAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'zip', 'payment_option')

class CreateCompositionAdmin(admin.ModelAdmin):
    list_display = ('zip', 'name', 'created')

admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(CreateComposition, CreateCompositionAdmin)
admin.site.register(CheckoutAddress, CheckoutAddressAdmin)