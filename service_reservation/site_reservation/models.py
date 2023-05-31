from django.db import models

# Create your models here.


class Resto(models.Model):
    emplacement = models.CharField(max_length=100)
    type_table = models.CharField(max_length=100)
    couleur_nappe = models.CharField(max_length=100)
    cout_reservation = models.DecimalField(max_digits=10, decimal_places=2)
    imgs = models.TextField()
