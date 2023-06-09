# Generated by Django 4.1.6 on 2023-06-20 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("profiles", "0001_initial"),
        ("products", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="WishLineItem",
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
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
                (
                    "user_profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lineitems",
                        to="profiles.userprofile",
                    ),
                ),
            ],
        ),
    ]
