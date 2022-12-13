from django.db import models
from django.core.validators import MinValueValidator


class Categories(models.Model):
    category = models.CharField(max_length=50)
    
    @staticmethod
    def get_all_categories():
        return Categories.objects.all()
    
    def __str__(self):
        return self.category

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    inventory = models.TextField(max_length=2000, null=True, blank=True, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to='images', null=True, blank=True, default='images/no_image.png')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, default=0)
    
    @staticmethod
    def get_goods_by_id(id):
        return Product.objects.filter(id=id)
  
    @staticmethod
    def get_all_goods():
        return Product.objects.all()
  
    @staticmethod
    def get_all_goods_by_category_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_goods()
        
    def __str__(self):
        return f"{self.title}{self.description} - {self.price}"
  
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