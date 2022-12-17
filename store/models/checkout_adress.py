from django.db import models
from django.conf import settings


PAYMENT = (
    ("C", "Готівкова"),
    ("B", "Безготівкова"),
)


class CheckoutAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    zip = models.CharField(max_length=10, default="")
    payment_option = models.CharField(
        max_length=2,
        choices=PAYMENT,
        default="C",
    )

    def __str__(self):
        return self.user.username, self.zip
