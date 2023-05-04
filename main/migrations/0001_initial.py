# Generated by Django 4.2 on 2023-05-03 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "is_checked",
                    models.BooleanField(default=False, verbose_name="Checked?"),
                ),
                ("name", models.CharField(max_length=60)),
                ("description", models.CharField(max_length=255)),
                ("price", models.FloatField(default=0.0)),
                ("stock", models.IntegerField(default=0)),
            ],
            options={
                "managed": True,
            },
        ),
    ]