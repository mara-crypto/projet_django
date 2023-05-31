import random
import json
import os

def generer_fichier_json():
    descriptions = [
        "Suite spacieuse avec vue sur la mer",
        "Suite luxueuse avec jacuzzi privé",
        "Suite moderne avec balcon",
        "Suite élégante avec vue panoramique",
        "Suite confortable avec cheminée"
        # Ajoutez d'autres descriptions ici
    ]
    
    noms_suites = [
        "Aldiana",
        "Dallou",
        "Obama",
        "Présidentielle",
        "Noflaye",
        "Albar",
        "Dalliana",
        "Obamiana",
        "Présidentielle Royale",
        "Noflayenne",
        "Almeida",
        "Dallouise",
        "Obamienne",
        "Impériale",
        "Noflayenne Deluxe",
        "Aldecoa",
        "Dallouna",
        "Obamic",
        "Impériale Royale",
        "Noflayenne Prestige",
        "Aldiano",
        "Dallouni",
        "Obamalia",
        "Royale",
        "Noflaye Plus"
    ]

    suites = []
    hotels = ["Radisson Blu", "Terrou Bi", "Pullman"]

    for hotel in hotels:
        images_utilisees = []  # Liste pour stocker les images déjà attribuées à l'hôtel
        
        for numero_suite in range(1, 26):
            etage = random.randint(1, 10)
            nombre_lit = random.randint(1, 3)
            salle_bain = random.randint(1, 2)
            prix = round(random.uniform(100, 300), 2)
            description = random.choice(descriptions)
            nom_suite = hotel + " - " + random.choice(noms_suites)  # Nom unique pour chaque suite
            
            images_dir = "service_reservation/site_reservation/static/reservation/image/media_suite"
            images = os.listdir(images_dir)
            
            image = random.choice(images)  # Choix aléatoire d'une image dans le dossier "media_suite"
            while image in images_utilisees:  # Vérifie si l'image a déjà été utilisée pour cet hôtel
                image = random.choice(images)  # Choix d'une autre image
            
            images_utilisees.append(image)  # Ajoute l'image utilisée à la liste
            
            suite = {
                'numero': numero_suite,
                'nom_suite': nom_suite,
                'etage': etage,
                'nombre_lit': nombre_lit,
                'salle_bain': salle_bain,
                'hotel': hotel,
                'prix': prix,
                'description': description,
                'image': image
            }
            suites.append(suite)

    with open('suites.json', 'w', encoding="utf-8") as fichier:
        json.dump(suites, fichier, indent=4)

    print("Le fichier JSON a été généré avec succès.")

    with open("suites.sql", "w" , encoding="utf-8") as fichier_sql:
        create_table = """CREATE TABLE IF NOT EXISTS suites (
            id INT PRIMARY KEY AUTO_INCREMENT,
            numero INT NOT NULL,
            nom_suite VARCHAR(50) NOT NULL,
            etage INT NOT NULL,
            nombre_lit INT NOT NULL,
            salle_bain INT NOT NULL,
            hotel VARCHAR(50) NOT NULL,
            prix FLOAT NOT NULL,
            description TEXT NOT NULL,
            image VARCHAR(255) NOT NULL
        );"""
        fichier_sql.write(create_table + "\n\n")

        for suite in suites:
            numero = suite['numero']
            nom_suite = suite['nom_suite']
            etage = suite['etage']
            nombre_lit = suite['nombre_lit']
            salle_bain = suite['salle_bain']
            hotel = suite['hotel']
            prix = suite['prix']
            description = suite['description']
            image = suite['image']

            query = f"INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES ({numero}, '{nom_suite}', {etage}, {nombre_lit}, {salle_bain}, '{hotel}', {prix}, '{description}', '{image}');"
            fichier_sql.write(query + "\n")

    print("Le fichier SQL a été généré avec succès.")

generer_fichier_json()
