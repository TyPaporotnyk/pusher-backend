# Generated by Django 5.0.4 on 2024-06-08 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="post_url",
            new_name="url",
        ),
    ]
