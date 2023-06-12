from django.db import models

class Suite(models.Model):
    id = models.AutoField(primary_key=True)
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
    



class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.nom
    
from django.db import models
from django.contrib.auth.models import User

class Reservation_Suite(models.Model):
    suite = models.ForeignKey(Suite, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_arrivee = models.DateField()
    date_depart = models.DateField()
    
    # Ajoutez d'autres champs selon vos besoins

    def __str__(self):
        return f"Reservation {self.id}"


