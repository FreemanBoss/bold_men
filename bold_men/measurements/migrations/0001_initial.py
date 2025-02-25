# Generated by Django 5.0.5 on 2024-05-14 20:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Measurement",
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
                    "chest",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="The chest measurement of the user.",
                        max_digits=4,
                    ),
                ),
                (
                    "waist",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="The waist measurement of the user.",
                        max_digits=4,
                    ),
                ),
                (
                    "hip",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="The hip measurement of the user.",
                        max_digits=4,
                    ),
                ),
                (
                    "length",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="The length measurement of the user.",
                        max_digits=4,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="The date and time when the measurement was created.",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="The date and time when the measurement was last updated.",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        help_text="The user associated with the measurement.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Measurement",
                "verbose_name_plural": "Measurements",
            },
        ),
    ]
