from django.db import models
from .categories import Categories
from django.core.validators import MinValueValidator
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    inventory = models.TextField(max_length=2000, null=True, blank=True, default="")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )
    image = models.ImageField(
        upload_to="images", null=True, blank=True, default="images/no_image.png"
    )
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("store:product", kwargs={"pk": self.pk})

    def get_add_to_cart_url(self):
        return reverse("store:add-to-cart", kwargs={"pk": self.pk})

    def get_remove_from_cart_url(self):
        return reverse("store:remove-from-cart", kwargs={"pk": self.pk})
