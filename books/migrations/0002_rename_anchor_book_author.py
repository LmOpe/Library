# Generated by Django 4.2.5 on 2023-09-13 14:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="book",
            old_name="anchor",
            new_name="author",
        ),
    ]
