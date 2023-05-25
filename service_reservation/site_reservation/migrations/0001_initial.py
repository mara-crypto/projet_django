# Generated by Django 4.2.1 on 2023-05-24 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Hotel",
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
                ("nom", models.CharField(max_length=100)),
                ("adresse", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Voiture",
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
                ("marque", models.CharField(max_length=100)),
                ("modele", models.CharField(max_length=100)),
                ("nombre_places", models.IntegerField()),
                ("boite_vitesse", models.CharField(max_length=100)),
                ("carburant", models.CharField(max_length=100)),
                ("climatisation", models.BooleanField(default=False)),
                ("couleur", models.CharField(max_length=100)),
                ("annee_production", models.IntegerField()),
                ("cout_journalier_location", models.IntegerField()),
            ],
        ),
    ]
