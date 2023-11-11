# Generated by Django 4.2.3 on 2023-11-06 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("emails", "0004_alter_email_body"),
    ]

    operations = [
        migrations.CreateModel(
            name="EmailTracking",
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
                ("unique_id", models.CharField(max_length=255, unique=True)),
                ("opened_at", models.DateTimeField(blank=True, null=True)),
                ("clicked_at", models.DateTimeField(blank=True, null=True)),
                (
                    "email",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="emails.email",
                    ),
                ),
                (
                    "subscriber",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="emails.subscriber",
                    ),
                ),
            ],
        ),
    ]
