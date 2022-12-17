from store.forms.checkout import CheckoutForm
from store.models.order import Order
from django.contrib.auth.models import User
from django.views.generic import View
from django.shortcuts import render, redirect
from store.models.checkout_adress import CheckoutAddress
from telegram.bot import send_order_to_telegram
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


class CheckoutView(View):
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        order = Order.objects.get(user=self.request.user, ordered=False)
        context = {
            "form": form,
            "order": order,
            "order_items": order.items.all(),
            "ammount": len(order.items.all()),
        }
        return render(self.request, "checkout.html", context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)

        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                zip = form.cleaned_data.get("zip")
                payment_option = form.cleaned_data.get("payment_option")

                checkout_address = CheckoutAddress(
                    user=self.request.user,
                    zip=zip,
                    payment_option=payment_option,
                )
                checkout_address.save()
                order.checkout_address = checkout_address
                order.ordered = True
                order.save()
                send_order_to_telegram(
                    order, checkout_address, User.objects.get(pk=order.user.pk)
                )
                return redirect("posy:home")
            messages.warning(self.request, "Помилка підтвердження замовлення")
            return redirect("store:checkout")

        except ObjectDoesNotExist:
            messages.error(self.request, "Ви ще нічого не замовили")
            return redirect("store:order-summary")
