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



class Hotel(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)

class User(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.nom
    

class Reservation_Suite(models.Model):
    suite = models.ForeignKey(Suite, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_arrivee = models.DateField()
    date_depart = models.DateField()
    
    # Ajoutez d'autres champs selon vos besoins

    def __str__(self):
        return f"Reservation {self.id}"



class Resto(models.Model):
    emplacement = models.CharField(max_length=100)
    type_table = models.CharField(max_length=100)
    couleur_nappe = models.CharField(max_length=100)






# import requests
# import json
# import mysql.connector

# # Informations de connexion à la base de données MySQL
# host = '127.0.0.1'
# database = 'gestion_reservation'
# user = 'khalil'
# password = 'Kh@lil6c'

# # Connexion à la base de données MySQL
# cnx = mysql.connector.connect(host=host, database=database, user=user, password=password)
# cursor = cnx.cursor()

# # Définition de l'URL de l'API et du token
# url = 'https://test.api.amadeus.com/v1/reference-data/locations/hotels/by-city?cityCode=dkr&radius=300&radiusUnit=KM&hotelSource=ALL'
# token = 's6wA5ozyK7zqLRrUVb6qFzA5xl9F'

# # Ajout du token à l'en-tête de la requête
# headers = {
#     'Authorization': f'Bearer {token}'
# }

# # Envoi de la requête GET à l'API
# response = requests.get(url, headers=headers)

# # Vérification du statut de la réponse
# if response.status_code == 200:
#     # Conversion de la réponse en JSON
#     data = response.json()

#     # Récupération des données de l'API
#     hotels = data.get('data', [])

#     # Insertion des données dans la table de la base de données
#     for hotel in hotels:
#         hotel_name = hotel['name']
#         hotel_address = hotel['iataCode']

#         query = "INSERT INTO site_reservation_hotel (nom, adresse) VALUES (%s, %s)"
#         values = (hotel_name, json.dumps(hotel_address))

#         cursor.execute(query, values)

#     cnx.commit()
#     print("Données insérées avec succès dans la base de données.")
# else:
#     print(f"Erreur lors de la requête : {response.status_code}")

# # Fermeture de la connexion à la base de données
# cursor.close()
# cnx.close()
