# Generated by Django 5.0.4 on 2024-06-10 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customers", "0003_alter_customer_first_name_alter_customer_last_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="max_pack",
            field=models.PositiveIntegerField(default=0),
        ),
    ]