# Generated by Django 4.1.4 on 2022-12-15 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posy", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Callback",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("phone_number", models.CharField(max_length=10)),
            ],
        ),
    ]
