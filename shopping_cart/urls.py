from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('confirm/', views.confirm, name='confirm'),
]
