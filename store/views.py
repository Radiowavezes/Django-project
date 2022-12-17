from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from .forms import CheckoutForm, CreateCompositionForm
from posy.models import Product, Categories
from telegram.bot import send_order_to_telegram, send_composition_to_telegram
from django.core.paginator import Paginator
from .models import (
    Order,
    OrderItem,
    CheckoutAddress,
)


class HomeView(ListView):
    model = Product
    paginate_by = 9
    context_object_name = 'goods'
    template_name = "store.html"
    
    def get_queryset(self):
        if 'choice' in self.request.GET:
            choice = self.request.GET['choice']
            return Product.objects.filter(category_id=choice)
        else:
            return Product.objects.all()
        
    def get_context_data(self,**kwargs):
        context = super(HomeView,self).get_context_data(**kwargs)
        context['categories']=Categories.objects.all()
        return context


class ProductView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = "product.html"


class CreateComposition(View):
    def get(self, *args, **kwargs):
        form = CreateCompositionForm()
        context = {
            'form': form,
        }
        return render(self.request, 'create_composition.html', context)

    def post(self, *args, **kwargs):
        form = CreateCompositionForm(self.request.POST or None)
        if form.is_valid():
            form.save()
            send_composition_to_telegram(form)
            return redirect('posy:home')
        messages.warning(self.request, "Помилка відправки форми")
        return redirect('store:create_composition')
    

class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):

        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'order' : order
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
                send_order_to_telegram(order, checkout_address, User.objects.get(pk=order.user.pk))
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
    