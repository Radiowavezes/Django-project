from django.contrib import admin
from .models import Posy, Categories

# Register your models here.
class PosyAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price')

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('category',)

admin.site.register(Posy, PosyAdmin)
admin.site.register(Categories, CategoriesAdmin)