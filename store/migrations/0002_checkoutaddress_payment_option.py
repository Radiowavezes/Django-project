# Generated by Django 4.1.4 on 2022-12-14 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="checkoutaddress",
            name="payment_option",
            field=models.CharField(
                choices=[("C", "Готівкова"), ("B", "Безготівкова")],
                default="C",
                max_length=2,
            ),
        ),
    ]
