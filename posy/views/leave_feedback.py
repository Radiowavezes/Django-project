from posy.models.feedback import Feedback
from datetime import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect


def leave_feedback(request):
    if request.method == "POST":
        full_name = request.POST["full_name"]
        sender = request.POST["sender"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        now = datetime.now()
        daytime = now.strftime("%Y-%m-%d, %H:%M")
        new_feedback = Feedback(
            full_name=full_name,
            sender=sender,
            phone=phone,
            message=message,
            daytime=daytime,
        )
        new_feedback.save()
        return HttpResponseRedirect(reverse("home"))
