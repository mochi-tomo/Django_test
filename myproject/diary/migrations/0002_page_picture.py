# Generated by Django 5.1 on 2024-08-22 07:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("diary", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="page",
            name="picture",
            field=models.ImageField(
                blank=True, null=True, upload_to="diary/picture/", verbose_name="写真"
            ),
        ),
    ]