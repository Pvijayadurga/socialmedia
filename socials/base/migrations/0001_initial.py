# Generated by Django 4.1.1 on 2022-09-16 17:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("1", "Male"),
                            ("2", "Female"),
                            ("3", "Dont want to specify"),
                        ],
                        default="1",
                        max_length=1,
                    ),
                ),
                ("phone", models.CharField(blank=True, default="", max_length=10)),
                ("DOB", models.DateField(null=True)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="images/user"),
                ),
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]