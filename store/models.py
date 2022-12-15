from django.db import models
from django.conf import settings
from posy.models import Product

PAYMENT = (
    ('C', 'Готівкова'),
    ('B', 'Безготівкова')
)
        
class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_final_price(self):
        return self.get_total_item_price()
    

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    checkout_address = models.ForeignKey(
        'CheckoutAddress', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.user.username
    
    def get_total_price(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total


class CheckoutAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    zip = models.CharField(max_length=10, default='')
    payment_option = models.CharField(
        max_length=2,
        choices=PAYMENT,
        default='C',
    )

    def __str__(self):
        return self.user.username


class CreateComposition(models.Model):
    name = models.CharField(max_length=20, default='', verbose_name='Ім\'я')
    zip = models.CharField(max_length=10, default='', verbose_name='+380', null=False, blank=False)
    color = models.CharField(max_length=20, default='', verbose_name='Кольорова гамма')
    fruit = models.BooleanField(default=False, verbose_name='Фрукти')
    candies = models.BooleanField(default=False, verbose_name='Цукерки')
    vegitables = models.BooleanField(default=False, verbose_name='Овочі')
    cheese = models.BooleanField(default=False, verbose_name='Сири')
    sausages = models.BooleanField(default=False, verbose_name='Ковбаси')
    alcohol = models.BooleanField(default=False, verbose_name='Алкоголь')
    snacks = models.BooleanField(default=False, verbose_name='Снеки')
    cones = models.BooleanField(default=False, verbose_name='Шишки')
    needles = models.BooleanField(default=False, verbose_name='Хвоя')
    christmas_decorations = models.BooleanField(default=False, verbose_name='Новорічні прикраси')
    joke_decorations = models.BooleanField(default=False, verbose_name='Штучні прикраси')
    handmade_decorations = models.BooleanField(default=False, verbose_name='Прикраси ручної роботи')
    flowers = models.BooleanField(default=False, verbose_name='Живі квіти або листя')
    fake_flowers = models.BooleanField(default=False, verbose_name='Штучні квіти')
    message = models.TextField(max_length=2000, default='', verbose_name='Інші побажання')
    created = models.DateTimeField(auto_now_add=True)
    
