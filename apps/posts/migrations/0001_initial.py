# Generated by Django 5.0.6 on 2024-06-16 12:41

import apps.posts.utils.upload
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Дата обновления")),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("description", models.TextField()),
                ("url", models.URLField(max_length=500)),
                ("group_name", models.CharField(blank=True, max_length=500, null=True)),
                ("group_url", models.URLField(blank=True, max_length=500, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PostImage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Дата обновления")),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to=apps.posts.utils.upload.get_post_image_path),
                ),
                ("original_image_url", models.URLField(blank=True, max_length=2000, null=True)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="images", to="posts.post"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
