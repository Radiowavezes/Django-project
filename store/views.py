from django.contrib import messages
from django.contrib.auth.models import User
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
from bot import send_message_to_telegram

class HomeView(ListView):
    model = Product
    paginate_by = 9
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
            messages.error(self.request, "Ви ще нічого не замовили")
            return redirect("/")


class CheckoutView(View):
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        order = Order.objects.get(user=self.request.user, ordered=False)
        context = {
            'form': form,
            'order': order,
            'order_items': order.items.all(),
            'ammount': len(order.items.all()),
        }
        return render(self.request, 'checkout.html', context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                zip = form.cleaned_data.get('zip')
                payment_option = form.cleaned_data.get('payment_option')

                checkout_address = CheckoutAddress(
                    user=self.request.user,
                    zip=zip,
                    payment_option=payment_option,
                )
                checkout_address.save()
                order.checkout_address = checkout_address
                order.ordered = True
                order.save()
                # name = User.objects.get(pk=order.user.pk)
                send_message_to_telegram(order, checkout_address, User.objects.get(pk=order.user.pk))
                # sold = ''
                # check = 0
                # for item in order.items.all():
                #     cost = item.quantity * item.item.price
                #     sold += str(item) + '-' + str(cost)
                #     check += item.get_final_price()
                # sold += f'. Всього {check}'
                # pay = 'готівкою' if checkout_address == 'C' else 'на картку'
                # name = User.objects.get(pk=order.user.pk)
                # bot.bot_message(f'{checkout_address.zip}, {name.first_name}, оплата {pay}: {sold}')
                
                return redirect('posy:home')
            messages.warning(self.request, "Помилка підтвердження замовлення")
            return redirect('store:checkout')

        except ObjectDoesNotExist:
            messages.error(self.request, "Ви ще нічого не замовили")
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
            messages.info(request, f"Збільшена кількість {order_item.item.title}")
            return redirect("store:order-summary")
        else:
            order.items.add(order_item)
            messages.info(request, f"{order_item.item.title} доданий в кошик")
            return redirect("store:order-summary")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, f"{order_item.item.title} доданий в кошик")
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
            messages.info(request, f"{order_item.item.title} видалений з кошика")
            return redirect("store:order-summary")
        else:
            messages.info(request, "Цього товару немає в кошику")
            return redirect("store:product", pk=pk)
    else:
        messages.info(request, "Ви ще нічого не замовили")
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
            messages.info(request, f"Кількість {order_item.item.title} змінена")
            return redirect("store:order-summary")
        else:
            messages.info(request, "Цього товару немає в кошику")
            return redirect("store:order-summary")
    else:
        #add message doesnt have order
        messages.info(request, "Ви ще нічого не замовили")
        return redirect("store:order-summary")