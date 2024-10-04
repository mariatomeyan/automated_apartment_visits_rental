# Generated by Django 5.1.1 on 2024-10-04 18:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PotentialTenant",
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
                ("name", models.CharField(max_length=100)),
                ("offer", models.CharField(max_length=100)),
                ("contact_info", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Runner",
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
                ("name", models.CharField(max_length=100)),
                ("availability", models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name="Zone",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Apartment",
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
                ("address", models.CharField(max_length=255)),
                ("availability", models.JSONField()),
                (
                    "runner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="apartments",
                        to="scheduling.runner",
                    ),
                ),
                (
                    "zone",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="apartments",
                        to="scheduling.zone",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Visit",
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
                ("date", models.DateField()),
                ("time_slot", models.TimeField()),
                ("visit_order", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "apartment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="visits",
                        to="scheduling.apartment",
                    ),
                ),
                (
                    "runner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="visits",
                        to="scheduling.runner",
                    ),
                ),
                (
                    "tenants",
                    models.ManyToManyField(
                        related_name="visits", to="scheduling.potentialtenant"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="runner",
            name="zones",
            field=models.ManyToManyField(related_name="runners", to="scheduling.zone"),
        ),
    ]
