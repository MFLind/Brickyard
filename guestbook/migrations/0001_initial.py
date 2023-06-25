# Generated by Django 4.1.6 on 2023-06-21 20:43

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GalleryItem",
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
                ("name", models.CharField(max_length=254)),
                ("description", models.TextField()),
                (
                    "image_url",
                    models.URLField(blank=True, max_length=1024, null=True),
                ),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to=""),
                ),
            ],
        ),
    ]
