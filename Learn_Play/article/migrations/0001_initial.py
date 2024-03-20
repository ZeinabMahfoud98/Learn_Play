# Generated by Django 4.2.5 on 2024-03-20 11:55

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
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
                ("title", models.CharField(max_length=100)),
                ("body", models.TextField(blank=True)),
                ("content", models.TextField(blank=True)),
                (
                    "photo",
                    models.ImageField(
                        blank=True, null=True, upload_to="article_photos/"
                    ),
                ),
            ],
        ),
    ]
