# Generated by Django 4.1.7 on 2023-03-01 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="League",
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
                ("icao_code", models.CharField(max_length=254)),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
            ],
            options={
                "verbose_name_plural": "Airport Details",
            },
        ),
    ]