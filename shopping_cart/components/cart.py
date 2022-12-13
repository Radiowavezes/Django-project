from django_unicorn.components import UnicornView, QuerySetType
from django.db.models import F
from shopping_cart.models import UserItem
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User

class CartView(UnicornView):
    user_products: QuerySetType[UserItem] = None
    user_pk: int
    total: float = 0
    
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.user_pk = kwargs.get('user')
        self.user_products = UserItem.objects.filter(user=self.user_pk)
        self.get_total()
    
    def add_item(self, product_pk):
        item, created = UserItem.objects.get_or_create(
            user_id=self.user_pk, 
            product_id=product_pk,
            )
        if not created:
            item.quantity = F('quantity') + 1
            item.save()
        self.user_products = UserItem.objects.filter(user=self.user_pk)
        self.get_total()
    
    def get_total(self):
        self.total = sum(
            product.total_price for product in self.user_products
            )
    
    def delete_item(self, product_pk):
        item = UserItem.objects.filter(pk=product_pk)
        item.delete()
        self.user_products = self.user_products.exclude(pk=product_pk)
        self.get_total()
        
    def increase_quantity(self, product_pk):
        item = UserItem.objects.get(pk=product_pk)
        item.quantity = F('quantity') + 1
        item.save()
        self.user_products = UserItem.objects.filter(user=self.user_pk) #?????
        self.get_total()
        
    def decrease_quantity(self, product_pk):
        item = UserItem.objects.get(pk=product_pk)
        if item.quantity > 1:
            item.quantity = F('quantity') - 1
            item.save()
            self.user_products = UserItem.objects.filter(user=self.user_pk) #?????
            self.get_total()
        else:
            self.delete_item(product_pk)

    