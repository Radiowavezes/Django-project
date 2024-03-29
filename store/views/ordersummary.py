from store.models.order import Order
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):

        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {"order": order}
            return render(self.request, "order_summary.html", context)
        
        except ObjectDoesNotExist:
            return render(self.request, "emptycart.html")