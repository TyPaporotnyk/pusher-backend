# Generated by Django 5.0.6 on 2024-06-11 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0003_post_group_link_post_group_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="group_link",
            new_name="group_url",
        ),
    ]
