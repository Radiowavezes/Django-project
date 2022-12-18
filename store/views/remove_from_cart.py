from posy.models.product import Product
from store.models.order_item import OrderItem
from store.models.order import Order
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect


@login_required
def remove_from_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__pk=item.pk).exists():
            order_item = OrderItem.objects.filter(
                item=item, user=request.user, ordered=False
            )[0]
            order_item.delete()
            return redirect("store:order-summary")
        else:
            return redirect("store:product", pk=pk)
    else:
        return redirect("store:product", pk=pk)
