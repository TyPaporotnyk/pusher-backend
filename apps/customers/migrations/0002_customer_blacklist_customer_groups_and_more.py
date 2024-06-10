# Generated by Django 5.0.4 on 2024-06-09 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0001_initial"),
        ("customers", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="blacklist",
            field=models.ManyToManyField(blank=True, related_name="blacklist", to="common.blacklist"),
        ),
        migrations.AddField(
            model_name="customer",
            name="groups",
            field=models.ManyToManyField(blank=True, to="common.group"),
        ),
        migrations.AddField(
            model_name="customer",
            name="groups_keywords",
            field=models.ManyToManyField(blank=True, related_name="groups_keywords", to="common.keyword"),
        ),
        migrations.AddField(
            model_name="customer",
            name="keywords",
            field=models.ManyToManyField(blank=True, related_name="keywords", to="common.keyword"),
        ),
    ]