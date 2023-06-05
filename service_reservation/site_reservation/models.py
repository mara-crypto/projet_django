from django.db import models

# Create your models here.


# from django.db import models

# class Voiture(models.Model):
#     marque = models.CharField(max_length=100)
#     modele = models.CharField(max_length=100)
#     nombre_places = models.IntegerField()
#     boite_vitesse = models.CharField(max_length=100)
#     carburant = models.CharField(max_length=100)
#     climatisation = models.BooleanField(default=False)
#     couleur = models.CharField(max_length=100)
#     annee_production = models.IntegerField()
#     cout_journalier_location = models.IntegerField()




class Hotel(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)




# import requests
# import json
# import mysql.connector

# # Informations de connexion à la base de données MySQL
# host = '127.0.0.1'
# database = 'gestion_reservation'
# user = 'modou'
# password = 'modou'

# # Connexion à la base de données MySQL
# cnx = mysql.connector.connect(host=host, database=database, user=user, password=password)
# cursor = cnx.cursor()

# # Définition de l'URL de l'API et du token
# url = 'https://test.api.amadeus.com/v1/reference-data/locations/hotels/by-city?cityCode=dkr&radius=300&radiusUnit=KM&hotelSource=ALL'
# token = '1APIACkDG5CnxvjQ9qO3hlL6GsUH'

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
