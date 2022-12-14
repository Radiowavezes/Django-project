from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from .forms import CheckoutForm
from .models import (
    Order,
    OrderItem,
    CheckoutAddress
)
from posy.models import Product
# Create your views here.
class HomeView(ListView):
    model = Product
    paginate_by = 6
    template_name = "store.html"


class ProductView(DetailView):
    model = Product
    template_name = "product.html"
    

class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):

        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object' : order
            }
            return render(self.request, 'order_summary.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an order")
            return redirect("/")

class CheckoutView(View):
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        context = {
            'form': form
        }
        return render(self.request, 'checkout.html', context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                phone = form.cleaned_data.get('street_address')
                payment_option = form.cleaned_data.get('payment_option')

                checkout_address = CheckoutAddress(
                    user=self.request.user,
                    phone=phone,
                )
                checkout_address.save()
                order.checkout_address = checkout_address
                order.save()
                return redirect('store:checkout')
            messages.warning(self.request, "Failed Chekout")
            return redirect('store:checkout')

        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an order")
            return redirect("store:order-summary")

        

@login_required
def add_to_cart(request, pk):
    item = get_object_or_404(Product, pk=pk )
    order_item, created = OrderItem.objects.get_or_create(
        item = item,
        user = request.user,
        ordered = False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]

        if order.items.filter(item__pk=item.pk).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "Added quantity Product")
            return redirect("store:order-summary")
        else:
            order.items.add(order_item)
            messages.info(request, "Product added to your cart")
            return redirect("store:order-summary")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "Product added to your cart")
        return redirect("store:order-summary")

@login_required
def remove_from_cart(request, pk):
    item = get_object_or_404(Product, pk=pk )
    order_qs = Order.objects.filter(
        user=request.user, 
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__pk=item.pk).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order_item.delete()
            messages.info(request, "Product \""+order_item.item.title + "\" remove from your cart")
            return redirect("store:order-summary")
        else:
            messages.info(request, "This Product not in your cart")
            return redirect("store:product", pk=pk)
    else:
        #add message doesnt have order
        messages.info(request, "You do not have an Order")
        return redirect("store:product", pk = pk)


@login_required
def reduce_quantity_item(request, pk):
    item = get_object_or_404(Product, pk=pk )
    order_qs = Order.objects.filter(
        user = request.user, 
        ordered = False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__pk=item.pk).exists() :
            order_item = OrderItem.objects.filter(
                item = item,
                user = request.user,
                ordered = False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order_item.delete()
            messages.info(request, "Product quantity was updated")
            return redirect("store:order-summary")
        else:
            messages.info(request, "This Product not in your cart")
            return redirect("store:order-summary")
    else:
        #add message doesnt have order
        messages.info(request, "You do not have an Order")
        return redirect("store:order-summary")