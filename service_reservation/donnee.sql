 
CREATE TABLE IF NOT EXISTS clients (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS voitures (
    id INT PRIMARY KEY,
    marque VARCHAR(255),
    modele VARCHAR(255),
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


