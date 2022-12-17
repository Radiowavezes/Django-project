from django.shortcuts import redirect
from posy.forms.callback import CallbackForm
from django.http import HttpResponse
from django.template import loader
from posy.models.product import Product
from posy.models.feedback import Feedback
from posy.models.callback import Callback
from telegram.bot import send_callback_number_to_telegram


def home(request):
    products = Product.objects.all().order_by("-price")[:6]
    feedbacks = Feedback.objects.all()
    template = loader.get_template("home.html")
    form = CallbackForm()
    context = {"products": products, "feedbacks": feedbacks, "form": form}
    if request.method == "POST":
        phone_number = request.POST["phone_number"]
        callback = Callback(phone_number=phone_number)
        callback.save()
        send_callback_number_to_telegram(callback.phone_number)
        return redirect("posy:home")

    return HttpResponse(template.render(context, request))
