CREATE TABLE IF NOT EXISTS suites (
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
        );

INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (1, 'Radisson Blu - Obamalia', 6, 1, 1, 'Radisson Blu', 119.94, 'Suite spacieuse avec vue sur la mer', '1.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (2, 'Radisson Blu - Noflayenne', 7, 2, 2, 'Radisson Blu', 169.28, 'Suite luxueuse avec jacuzzi privé', '8.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (3, 'Radisson Blu - Dallouna', 3, 2, 2, 'Radisson Blu', 208.53, 'Suite luxueuse avec jacuzzi privé', '20.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (4, 'Radisson Blu - Royale', 8, 1, 1, 'Radisson Blu', 227.89, 'Suite spacieuse avec vue sur la mer', '21.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (5, 'Radisson Blu - Dallouise', 4, 1, 2, 'Radisson Blu', 275.9, 'Suite élégante avec vue panoramique', '23.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (6, 'Radisson Blu - Impériale', 2, 3, 2, 'Radisson Blu', 263.78, 'Suite spacieuse avec vue sur la mer', '7.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (7, 'Radisson Blu - Noflayenne', 9, 1, 1, 'Radisson Blu', 297.55, 'Suite élégante avec vue panoramique', '15.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (8, 'Radisson Blu - Aldiano', 9, 3, 1, 'Radisson Blu', 220.86, 'Suite luxueuse avec jacuzzi privé', '5.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (9, 'Radisson Blu - Albar', 8, 2, 1, 'Radisson Blu', 161.45, 'Suite spacieuse avec vue sur la mer', '6.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (10, 'Radisson Blu - Albar', 10, 3, 1, 'Radisson Blu', 233.39, 'Suite élégante avec vue panoramique', '11.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (11, 'Radisson Blu - Noflayenne Deluxe', 10, 2, 1, 'Radisson Blu', 198.44, 'Suite élégante avec vue panoramique', '22.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (12, 'Radisson Blu - Noflayenne', 9, 2, 1, 'Radisson Blu', 211.04, 'Suite luxueuse avec jacuzzi privé', '3.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (13, 'Radisson Blu - Almeida', 5, 1, 1, 'Radisson Blu', 104.62, 'Suite spacieuse avec vue sur la mer', '2.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (14, 'Radisson Blu - Dallouni', 6, 2, 1, 'Radisson Blu', 279.52, 'Suite luxueuse avec jacuzzi privé', '12.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (15, 'Radisson Blu - Présidentielle', 1, 1, 2, 'Radisson Blu', 186.6, 'Suite élégante avec vue panoramique', '10.jpeg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (16, 'Radisson Blu - Noflaye Plus', 4, 2, 1, 'Radisson Blu', 102.0, 'Suite confortable avec cheminée', '14.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (17, 'Radisson Blu - Noflayenne Prestige', 4, 2, 1, 'Radisson Blu', 245.0, 'Suite élégante avec vue panoramique', '19.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (18, 'Radisson Blu - Impériale Royale', 1, 3, 1, 'Radisson Blu', 170.0, 'Suite confortable avec cheminée', '25.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (19, 'Radisson Blu - Obamienne', 3, 1, 1, 'Radisson Blu', 117.37, 'Suite élégante avec vue panoramique', '13.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (20, 'Radisson Blu - Dallou', 5, 1, 2, 'Radisson Blu', 223.07, 'Suite confortable avec cheminée', '4.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (21, 'Radisson Blu - Royale', 7, 1, 2, 'Radisson Blu', 197.58, 'Suite moderne avec balcon', '18.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (22, 'Radisson Blu - Noflaye', 8, 3, 2, 'Radisson Blu', 226.35, 'Suite luxueuse avec jacuzzi privé', '24.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (23, 'Radisson Blu - Noflayenne Prestige', 3, 1, 2, 'Radisson Blu', 251.55, 'Suite spacieuse avec vue sur la mer', '16.jpeg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (24, 'Radisson Blu - Dallouna', 2, 2, 2, 'Radisson Blu', 186.08, 'Suite élégante avec vue panoramique', '9.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (25, 'Radisson Blu - Noflayenne Prestige', 7, 1, 1, 'Radisson Blu', 177.91, 'Suite spacieuse avec vue sur la mer', '17.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (1, 'Terrou Bi - Dallouise', 7, 1, 2, 'Terrou Bi', 254.16, 'Suite confortable avec cheminée', '8.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (2, 'Terrou Bi - Obamic', 5, 3, 1, 'Terrou Bi', 262.36, 'Suite luxueuse avec jacuzzi privé', '23.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (3, 'Terrou Bi - Noflayenne', 6, 3, 2, 'Terrou Bi', 170.88, 'Suite luxueuse avec jacuzzi privé', '7.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (4, 'Terrou Bi - Impériale Royale', 3, 1, 1, 'Terrou Bi', 268.74, 'Suite confortable avec cheminée', '5.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (5, 'Terrou Bi - Almeida', 5, 2, 1, 'Terrou Bi', 283.89, 'Suite luxueuse avec jacuzzi privé', '19.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (6, 'Terrou Bi - Albar', 8, 1, 2, 'Terrou Bi', 298.55, 'Suite élégante avec vue panoramique', '17.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (7, 'Terrou Bi - Aldiana', 3, 3, 2, 'Terrou Bi', 233.87, 'Suite spacieuse avec vue sur la mer', '12.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (8, 'Terrou Bi - Obama', 5, 3, 1, 'Terrou Bi', 165.55, 'Suite élégante avec vue panoramique', '11.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (9, 'Terrou Bi - Dallou', 6, 2, 1, 'Terrou Bi', 229.02, 'Suite élégante avec vue panoramique', '22.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (10, 'Terrou Bi - Dallou', 5, 3, 2, 'Terrou Bi', 273.1, 'Suite luxueuse avec jacuzzi privé', '1.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (11, 'Terrou Bi - Obamienne', 1, 1, 2, 'Terrou Bi', 198.07, 'Suite spacieuse avec vue sur la mer', '20.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (12, 'Terrou Bi - Dallouise', 10, 1, 1, 'Terrou Bi', 183.13, 'Suite élégante avec vue panoramique', '24.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (13, 'Terrou Bi - Obamic', 4, 3, 1, 'Terrou Bi', 138.64, 'Suite spacieuse avec vue sur la mer', '14.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (14, 'Terrou Bi - Impériale Royale', 1, 2, 2, 'Terrou Bi', 123.29, 'Suite spacieuse avec vue sur la mer', '18.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (15, 'Terrou Bi - Aldiano', 9, 1, 2, 'Terrou Bi', 220.41, 'Suite spacieuse avec vue sur la mer', '2.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (16, 'Terrou Bi - Dallouise', 6, 1, 1, 'Terrou Bi', 157.17, 'Suite spacieuse avec vue sur la mer', '9.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (17, 'Terrou Bi - Impériale Royale', 8, 3, 1, 'Terrou Bi', 125.73, 'Suite luxueuse avec jacuzzi privé', '15.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (18, 'Terrou Bi - Obamalia', 7, 2, 2, 'Terrou Bi', 123.29, 'Suite spacieuse avec vue sur la mer', '25.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (19, 'Terrou Bi - Obamalia', 7, 2, 2, 'Terrou Bi', 224.69, 'Suite spacieuse avec vue sur la mer', '10.jpeg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (20, 'Terrou Bi - Almeida', 1, 2, 1, 'Terrou Bi', 100.16, 'Suite confortable avec cheminée', '16.jpeg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (21, 'Terrou Bi - Noflayenne', 1, 1, 1, 'Terrou Bi', 251.5, 'Suite moderne avec balcon', '21.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (22, 'Terrou Bi - Impériale Royale', 7, 2, 2, 'Terrou Bi', 296.08, 'Suite luxueuse avec jacuzzi privé', '6.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (23, 'Terrou Bi - Dalliana', 7, 2, 2, 'Terrou Bi', 181.11, 'Suite confortable avec cheminée', '3.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (24, 'Terrou Bi - Obamienne', 3, 1, 2, 'Terrou Bi', 262.86, 'Suite luxueuse avec jacuzzi privé', '13.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (25, 'Terrou Bi - Noflaye Plus', 4, 2, 2, 'Terrou Bi', 283.76, 'Suite élégante avec vue panoramique', '4.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (1, 'Pullman - Noflayenne Prestige', 9, 2, 1, 'Pullman', 229.23, 'Suite élégante avec vue panoramique', '1.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (2, 'Pullman - Royale', 8, 3, 1, 'Pullman', 271.7, 'Suite luxueuse avec jacuzzi privé', '22.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (3, 'Pullman - Almeida', 8, 1, 1, 'Pullman', 281.12, 'Suite moderne avec balcon', '15.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (4, 'Pullman - Dallouna', 1, 1, 1, 'Pullman', 112.7, 'Suite luxueuse avec jacuzzi privé', '25.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (5, 'Pullman - Noflayenne Prestige', 10, 3, 1, 'Pullman', 283.7, 'Suite luxueuse avec jacuzzi privé', '24.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (6, 'Pullman - Impériale', 9, 3, 1, 'Pullman', 114.4, 'Suite luxueuse avec jacuzzi privé', '6.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (7, 'Pullman - Obamiana', 9, 2, 1, 'Pullman', 123.72, 'Suite confortable avec cheminée', '23.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (8, 'Pullman - Présidentielle', 10, 3, 2, 'Pullman', 151.21, 'Suite moderne avec balcon', '11.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (9, 'Pullman - Impériale Royale', 8, 2, 2, 'Pullman', 126.69, 'Suite luxueuse avec jacuzzi privé', '10.jpeg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (10, 'Pullman - Royale', 5, 1, 1, 'Pullman', 189.04, 'Suite moderne avec balcon', '20.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (11, 'Pullman - Dallou', 6, 2, 2, 'Pullman', 192.35, 'Suite moderne avec balcon', '21.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (12, 'Pullman - Noflayenne Deluxe', 9, 2, 2, 'Pullman', 197.4, 'Suite luxueuse avec jacuzzi privé', '18.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (13, 'Pullman - Noflayenne Prestige', 10, 2, 1, 'Pullman', 297.87, 'Suite confortable avec cheminée', '16.jpeg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (14, 'Pullman - Noflayenne Deluxe', 2, 1, 1, 'Pullman', 284.12, 'Suite confortable avec cheminée', '2.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (15, 'Pullman - Obamiana', 9, 3, 1, 'Pullman', 173.13, 'Suite luxueuse avec jacuzzi privé', '19.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (16, 'Pullman - Présidentielle', 7, 3, 2, 'Pullman', 254.52, 'Suite confortable avec cheminée', '12.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (17, 'Pullman - Obamiana', 6, 2, 1, 'Pullman', 136.24, 'Suite luxueuse avec jacuzzi privé', '13.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (18, 'Pullman - Aldiano', 9, 2, 2, 'Pullman', 119.31, 'Suite luxueuse avec jacuzzi privé', '9.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (19, 'Pullman - Impériale Royale', 1, 1, 1, 'Pullman', 103.1, 'Suite confortable avec cheminée', '5.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (20, 'Pullman - Dalliana', 4, 3, 1, 'Pullman', 133.03, 'Suite spacieuse avec vue sur la mer', '17.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (21, 'Pullman - Albar', 5, 1, 2, 'Pullman', 158.37, 'Suite moderne avec balcon', '3.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (22, 'Pullman - Impériale Royale', 2, 3, 1, 'Pullman', 213.32, 'Suite luxueuse avec jacuzzi privé', '7.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (23, 'Pullman - Almeida', 5, 2, 1, 'Pullman', 134.83, 'Suite moderne avec balcon', '8.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (24, 'Pullman - Dallouise', 4, 1, 1, 'Pullman', 176.48, 'Suite spacieuse avec vue sur la mer', '4.jpg');
INSERT INTO suites (numero, nom_suite, etage, nombre_lit, salle_bain, hotel, prix, description, image) VALUES (25, 'Pullman - Obamienne', 1, 2, 1, 'Pullman', 199.38, 'Suite spacieuse avec vue sur la mer', '14.jpg');
