# Generated by Django 4.2.5 on 2023-09-13 14:36

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=250)),
                ("subtitle", models.CharField(max_length=250)),
                ("anchor", models.CharField(max_length=100)),
                ("isbn", models.CharField(max_length=13)),
            ],
        ),
    ]