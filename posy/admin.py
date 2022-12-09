from django.contrib import admin
from .models import Posy, Categories, Feedback

# Register your models here.
class PosyAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price')

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('category',)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('full_name','phone', 'sender')

admin.site.register(Posy, PosyAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Feedback, FeedbackAdmin)