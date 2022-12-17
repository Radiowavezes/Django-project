from posy.models.product import Product
from store.models.order_item import OrderItem
from store.models.order import Order
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages


@login_required
def reduce_quantity_item(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__pk=item.pk).exists():
            order_item = OrderItem.objects.filter(
                item=item, user=request.user, ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order_item.delete()
            messages.info(request, f"Кількість {order_item.item.title} змінена")
            return redirect("store:order-summary")
        else:
            messages.info(request, "Цього товару немає в кошику")
            return redirect("store:order-summary")
    else:
        messages.info(request, "Ви ще нічого не замовили")
        return redirect("store:order-summary")
