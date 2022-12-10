from django.db import models
import datetime
from datetime import datetime
from django.contrib.auth.models import User

class Categories(models.Model):
    category = models.CharField(max_length=50)
    
    @staticmethod
    def get_all_categories():
        return Categories.objects.all()
    
    def __str__(self):
        return self.category

class Posy(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    inventory = models.TextField(max_length=2000, null=True, blank=True, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image = models.ImageField(upload_to='images', null=True, blank=True, default='images/no_image.png')
    category = models.ManyToManyField(Categories)
    
    @staticmethod
    def get_goods_by_id(id):
        return Posy.objects.filter(id=id)
  
    @staticmethod
    def get_all_goods():
        return Posy.objects.all()
  
    @staticmethod
    def get_all_goods_by_category_id(category_id):
        if category_id:
            return Posy.objects.filter(category=category_id)
        else:
            return Posy.get_all_goods()
        
    def __str__(self):
        return f"{self.title}{self.description} - {self.price}"

class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    
    def register(self):
        self.save()
    
    def is_exist(self):
        return Client.objects.filter(email=self.email)
    
    @staticmethod
    def get_client_by_email(email):
        try:
            return Client.objects.get(email=email)
        except ValueError:
            return False

class Order(models.Model):
    product = models.ForeignKey(Posy, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=10, default='', blank=True)
    date = models.DateField(default=datetime.today)
    status = models.BooleanField(default=False)
    
    def place_order(self):
        self.save()
        
    @staticmethod
    def get_orders_by_client_id(client_id):
        return Order.objects.filter(customer=client_id).order_by('-date')
    
class Feedback(models.Model):
    full_name = models.CharField(max_length=100)
    sender = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField(max_length=2000)
    daytime = models.DateTimeField('Time published: ', auto_now_add=True, editable=True)
    
    @staticmethod
    def get_client_by_email(email):
        try:
            return Feedback.objects.get(sender=email)
        except Feedback.DoesNotExist:
            return False
    
    def __str__(self):
        return f"{self.full_name}{self.sender} - {self.message} {self.daytime}"