# Generated by Django 5.0.6 on 2024-06-23 15:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0002_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="blacklist",
            constraint=models.UniqueConstraint(fields=("name", "customer"), name="unique_black_list_name_customer"),
        ),
    ]
