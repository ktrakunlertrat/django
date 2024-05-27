# Generated by Django 4.2.11 on 2024-05-27 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("testdb", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("name", models.CharField(max_length=200)),
                ("desc", models.TextField()),
            ],
        ),
    ]
