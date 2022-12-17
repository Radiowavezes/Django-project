from django.contrib import admin
from posy.models.product import Product
from posy.models.categories import Categories
from posy.models.feedback import Feedback
from posy.models.callback import Callback


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "price",
    )


class CategoriesAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "category",
    )


class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "phone",
        "sender",
        "daytime",
    )


class CallbackAdmin(admin.ModelAdmin):
    list_display = (
        "phone_number",
        "created",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Callback, CallbackAdmin)
