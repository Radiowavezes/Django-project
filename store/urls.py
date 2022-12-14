from django.urls import path
from . import views
from store.views import ( 
    remove_from_cart, 
    reduce_quantity_item,
    add_to_cart, 
    ProductView, 
    HomeView, 
    CheckoutView,
    OrderSummaryView
)

app_name = 'store'

urlpatterns = [
    path('', HomeView.as_view(), name='store'),
    path('product/<pk>/', ProductView.as_view(), name='product'),
    path('order-summary', OrderSummaryView.as_view(), name='order-summary'),
    path('checkout', CheckoutView.as_view(), name='checkout'),
    path('add-to-cart/<pk>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<pk>/', remove_from_cart, name='remove-from-cart'),
    path('reduce-quantity-item/<pk>/', reduce_quantity_item, name='reduce-quantity-item')
]