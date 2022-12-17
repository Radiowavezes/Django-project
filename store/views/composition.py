from store.forms.composition import CreateCompositionForm
from django.views.generic import View
from django.contrib import messages
from django.shortcuts import render, redirect
from telegram.bot import send_composition_to_telegram


class CreateComposition(View):
    def get(self, *args, **kwargs):
        form = CreateCompositionForm()
        context = {
            "form": form,
        }
        return render(self.request, "create_composition.html", context)

    def post(self, *args, **kwargs):
        form = CreateCompositionForm(self.request.POST or None)
        if form.is_valid():
            form.save()
            send_composition_to_telegram(form)
            return redirect("posy:home")
        messages.warning(self.request, "Помилка відправки форми")
        return redirect("store:create_composition")
