# Generated by Django 4.1 on 2022-08-10 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CatsModel",
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
                ("imie", models.CharField(max_length=200)),
                ("rok_urodzenia", models.IntegerField(blank=True)),
                ("rasa", models.CharField(max_length=200)),
                ("opis", models.TextField(blank=True)),
            ],
        ),
    ]
