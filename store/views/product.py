from django.views.generic import DetailView
from posy.models.product import Product


class ProductView(DetailView):
    model = Product
    context_object_name = "product"
    template_name = "product.html"
