from django.urls import path
from store.views.home import HomeView
from store.views.product import ProductView
from store.views.composition import CreateComposition
from store.views.ordersummary import OrderSummaryView
from store.views.checkout import CheckoutView
from store.views.add_to_cart import add_to_cart
from store.views.remove_from_cart import remove_from_cart
from store.views.reduce_quantity_item import reduce_quantity_item


app_name = "store"
urlpatterns = [
    path("", HomeView.as_view(), name="store"),
    path("product/<pk>/", ProductView.as_view(), name="product"),
    path("create_composition", CreateComposition.as_view(), name="create_composition"),
    path("order_summary", OrderSummaryView.as_view(), name="order-summary"),
    path("checkout", CheckoutView.as_view(), name="checkout"),
    path("add-to-cart/<pk>/", add_to_cart, name="add-to-cart"),
    path("remove-from-cart/<pk>/", remove_from_cart, name="remove-from-cart"),
    path("reduce-quantity-item/<pk>/", reduce_quantity_item, name="reduce-quantity-item"),
]
