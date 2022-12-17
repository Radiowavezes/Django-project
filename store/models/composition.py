from django.db import models


class CreateComposition(models.Model):
    name = models.CharField(max_length=20, default="", verbose_name="Ім'я")
    zip = models.CharField(
        max_length=10, default="", verbose_name="+380", null=False, blank=False
    )
    color = models.CharField(max_length=20, default="", verbose_name="Кольорова гамма")
    fruit = models.BooleanField(default=False, verbose_name="Фрукти")
    candies = models.BooleanField(default=False, verbose_name="Цукерки")
    vegitables = models.BooleanField(default=False, verbose_name="Овочі")
    cheese = models.BooleanField(default=False, verbose_name="Сири")
    sausages = models.BooleanField(default=False, verbose_name="Ковбаси")
    alcohol = models.BooleanField(default=False, verbose_name="Алкоголь")
    snacks = models.BooleanField(default=False, verbose_name="Снеки")
    cones = models.BooleanField(default=False, verbose_name="Шишки")
    needles = models.BooleanField(default=False, verbose_name="Хвоя")
    christmas_decorations = models.BooleanField(
        default=False, verbose_name="Новорічні прикраси"
    )
    joke_decorations = models.BooleanField(
        default=False, verbose_name="Штучні прикраси"
    )
    handmade_decorations = models.BooleanField(
        default=False, verbose_name="Прикраси ручної роботи"
    )
    flowers = models.BooleanField(default=False, verbose_name="Живі квіти або листя")
    fake_flowers = models.BooleanField(default=False, verbose_name="Штучні квіти")
    message = models.TextField(
        max_length=2000, default="", verbose_name="Інші побажання"
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name, self.zip, self.created
