from django.db import models

class Suite(models.Model):
    numero = models.IntegerField()
    nom_suite = models.CharField(max_length=100)
    etage = models.IntegerField()
    nombre_lit = models.IntegerField()
    salle_bain = models.IntegerField()
    hotel = models.CharField(max_length=100)
    prix = models.FloatField()
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='media_suite/')  # Spécifiez le dossier de destination pour les images

    def __str__(self):
        return self.nom_suite
class Image(models.Model):
    image = models.ImageField(upload_to='media_suite')

    def __str__(self):
        return str(self.image)
