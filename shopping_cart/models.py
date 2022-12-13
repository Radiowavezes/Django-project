from django.db import models
from django.contrib.auth.models import User
from posy.models import Product

class UserItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product.title
    
    @property
    def total_price(self):
        return self.quantity * self.product.price