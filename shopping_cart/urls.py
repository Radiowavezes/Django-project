from django.urls import path
from . import views
from .components import cart

urlpatterns = [
    path('', views.cart, name='cart'),
]
