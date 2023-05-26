

CREATE TABLE IF NOT EXISTS voitures (
    id INT PRIMARY KEY AUTO_INCREMENT,
    marque VARCHAR(255),
    modele VARCHAR(255),
    nombre_places INT,
    boite_vitesse VARCHAR(255),
    carburant VARCHAR(255),
    climatisation BOOLEAN,
    couleur VARCHAR(255),
    annee_production INT,
    cout_journalier_location VARCHAR(255),
    image_path VARCHAR(255),
    disponible BOOLEAN DEFAULT true
);



ALTER TABLE clients MODIFY id INT AUTO_INCREMENT;
ALTER TABLE voitures MODIFY id INT AUTO_INCREMENT;
ALTER TABLE reservations MODIFY id INT AUTO_INCREMENT;



 

with open("insertion-voiture.sql", "w") as fichier_sql:
    with open("donnees_voitures.json", "r", encoding="utf-8") as fichier_json:
        donnees = json.load(fichier_json)

    for voiture in donnees:
        marque = voiture["marque"]
        modele = voiture["modele"]
        nombre_places = voiture["nombre_places"]
        boite_vitesse = voiture["boite_vitesse"]
        carburant = voiture["carburant"]
        climatisation = voiture["climatisation"]
        couleur = voiture["couleur"]
        annee_production = voiture["annee_production"]
        cout_journalier_location = voiture["cout_journalier_location"]
        image_path = voiture["image_path"]

        query = f"INSERT INTO Voitures (marque, modele, nombre_places, boite_vitesse, carburant, climatisation, couleur, annee_production, cout_journalier_location, image_path) VALUES ('{marque}', '{modele}', {nombre_places}, '{boite_vitesse}', '{carburant}', {climatisation}, '{couleur}', {annee_production}, '{cout_journalier_location}', '{image_path}');"
        fichier_sql.write(query + "\n")

    print(query)

CREATE TABLE IF NOT EXISTS clients (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255), 
    password VARCHAR(255), 
    phone VARCHAR(255),
    address VARCHAR(255),INSERT INTO Voitures (marque, modele, nombre_places, boite_vitesse, carburant, climatisation, couleur, annee_production, cout_journalier_location, image_path) VALUES

);

CREATE TABLE IF NOT EXISTS voitures (
    id INT PRIMARY KEY,
    marque VARCHAR(255),
    modele VARCHAR(255),
    nombre_places 
    boite_vitesse 
    carburant 
    climatisation 
    couleur
    annee_production
    cout_journalier 
    disponible BOOLEAN DEFAULT true
);

CREATE TABLE IF NOT EXISTS reservations (
    id INT PRIMARY KEY,
    client_id INT,
    voiture_id INT,
    date_debut DATE, 
    date_fin DATE,
    FOREIGN KEY (client_id) REFERENCES clients(id),
    FOREIGN KEY (voiture_id) REFERENCES voitures(id)
);


 
