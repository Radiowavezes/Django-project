from django.contrib import admin
from .models import Product, Categories, Feedback

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price')

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('category',)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('full_name','phone', 'sender', 'daytime')

admin.site.register(Product, ProductAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Feedback, FeedbackAdmin)