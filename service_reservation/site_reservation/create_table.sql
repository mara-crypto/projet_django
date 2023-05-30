DROP DATABASE IF EXISTS gestion_reservation;

create DATABASE gestion_reservation;

use gestion_reservation;

DROP TABLE IF EXISTS resto;

CREATE TABLE resto (
    id INT PRIMARY KEY AUTO_INCREMENT,
    emplacement VARCHAR(50) NOT NULL,
    type_table VARCHAR(50)  NOT NULL,
    couleur_nappe VARCHAR(50)  NOT NULL,
    cout_reservation VARCHAR(50)  NOT NULL,
    imgs VARCHAR(50)  NOT NULL
);

DROP TABLE IF EXISTS service;

CREATE TABLE service (
    id_service INT PRIMARY KEY AUTO_INCREMENT,
    nom_service VARCHAR(50)  NOT NULL
);

DROP TABLE IF EXISTS image;

CREATE TABLE image (
    id_image INT PRIMARY KEY AUTO_INCREMENT,
    id_service INT,
    FOREIGN KEY (id_service) REFERENCES service (id_service)
);

    