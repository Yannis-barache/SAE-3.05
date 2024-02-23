INSERT INTO ARMES(idArme, nomArme,sexeArme) values
        (1,'fleuret homme','H'),
        (2,'fleuret femme','F'),
        (3,'sabre homme','H'),
        (4,'sabre femme','F'),
        (5,'épée homme','H'),
        (6,'épée femme','F');

INSERT INTO CATEGORIE(idCategorie, nomCategorie) values
        (1,'U13'),
        (2,'U15'),
        (3,'U17'),
        (4,'U20'),
        (5,'Senior'),
        (6,'V1'),
        (7,'V2'),
        (8,'V3'),
        (9,'V4');

INSERT INTO CLUB(idClub, nomClub, adresse, mdpClub) values
        (1,'Escrimeur indépendant','Aucune','independant'),
        (2,'Club d''escrime de Paris quai de seine','3 Quai Saint-Bernard 75005 Paris','lesquais'),
        (3,'Club d''escrime de Lyon','215 Rue Paul Bert, 69003 Lyon','leslions'),
        (4,'Club d''escrime de Marseille','33 Rue Crillon, 13005 Marseille','marseille'),
        (5,'Club d''escrime de Bordeaux','53 Rue Pauline Kergomard, 33800 Bordeaux','levin'),
        (6,'TUC Escrime','6 Rue Claudius Rougenet, 31500 Toulouse','lessaucisses'),
        (7,'Académie vauban','Pl. Nouvelle Aventure, 59000 Lille','vauban'),
        (8,'NEC','Rue Louis Joxe, 44200 Nantes','mantes'),
        (9,'SUC','43 Av. du Rhin, 67100 Strasbourg','presqueallemagne'),
        (10,'MUC','60 Pl. Jacques Mirouze, 34000 Montpellier','sud'),
        (11,'Club d''escrime de Rennes','8 Av. des Gayeulles, 35700 Rennes','villedeKnou'),
        (12,'Club d''escrime de Reims','Imp. Léo Lagrange, 51100 Reims','et'),
        (13,'Club d''escrime de Saint-Etienne','Rue du Dr Paul Michelon, 42000 Saint-Étienne','perdant'),
        (14,'Cercle d''escrime de Blois ','25 Rue Lucien Joubert, 41000 Blois','ceblois');


INSERT INTO ORGANISATEUR(idOrganisateur, nomOrganisateur, prenomOrganisateur, adresseMailOrganisateur, mdpOrganisateur, nomUtilisateur) values
        (1,'BARACHE','Yannis','yannis.barache1@gmail.com','yannis','barache'),
        (2,'FOFANA','Abdoulahi','abdoulahifofana10@gmail.com','abdoulahi','fofana'),
        (3,'MERIT','Juliann','juliann.merit@gmail.com','juliann','merit'),
        (4,'CHEDEVILLE','Baptiste','baba.chedeville45@gmail.com','baptiste','chedeville'),
        (5,'ELKASMI','Hajar','elks.hajar@gmail.com','hajar','elkasmi'),
        (6,'LECHOPIER','Christophe','christophe.lechopier@univ-orleans.fr','christophe','lechopier');


INSERT INTO ESCRIMEUR(idEscrimeur, nomEscrimeur, prenomEscrimeur, licence, dateNaissance, nomUtilisateurEscrimeur, mdpEscrimeur, classement, idClub, sexeEscrimeur, idCategorie, arbitrage) values
        (1,'Barache', 'Yannis', '123456', '2004-09-30', 'yannis', 'barache', NULL, 1, 'H', 4, true),
        (2, 'Doe', 'John', '1234566', '1999-01-01', 'johndoe', 'password', NULL, 2, 'H', 5, false),
        (3, 'Dark', 'Vador', '1234567', '1999-01-01', 'etoile', 'noire', NULL, 3, 'H', 5, true),
        (4, 'Skywalker', 'Luke', '234567', '1999-01-01', 'etoile', 'claire', NULL, 4, 'H', 5, true),
        (5, 'Solo', 'Han', '987611', '1999-01-01', 'hansolo', 'password', NULL, 5, 'H', 5, true),
        (6, 'Organa', 'Leia', '00000', '1999-01-01', 'leiaorgana', 'password', NULL, 6, 'F', 5, true),
        (7, 'Calrissian', 'Lando', '567878', '1999-01-01', 'landocalrissian', 'password', NULL, 7, 'H', 5, false),
        (8, 'Chewbacca', 'Chewie', '23232323', '1999-01-01', 'chewbacca', 'password', NULL, 8, 'H', 5, true),
        (9, 'Fett', 'Boba', '45454545', '1999-01-01', 'bobafett', 'password', NULL, 9, 'H', 5, false),
        (10, 'Maul', 'Darth', '8765', '1999-01-01', 'darthmaul', 'password', NULL, 10, 'H', 5, true),
        (11, 'Lechopier','Christophe', '1', '1999-01-01', 'christophe', 'lechopier', NULL, 14, 'H', 5, true),
        (12, 'Fofana','Abdoulahi', '224224', '1999-01-01', 'abdoulahi', 'fofana', NULL, 12, 'H', 5, true),
        (13, 'Merit','Juliann', '963963', '1999-01-01', 'juliann', 'merit', NULL, 14, 'H', 5, false),
        (14, 'Chedeville','Baptiste', '33333333', '1999-01-01', 'baptiste', 'chedeville', NULL, 12, 'H', 5, true),
        (15, 'Elkasmi','Hajar', '212212212', '1999-01-01', 'hajar', 'elkasmi', NULL, 11, 'H', 5, false),
        (16, 'Doe', 'Jane', '87654', '1999-01-01', 'janedoe', 'password', NULL, 2, 'H', 5, false),
        (17, 'Abada','Khalil','213213213','1999-01-01','khalil','abada',NULL,1,'H',5,false);

INSERT INTO LIEU(idLieu, adresseLieu, descriptionLieu) values
        (1,'3 Quai Saint-Bernard 75005 Paris','Salle d''escrime de Paris quai de seine'),
        (2,'215 Rue Paul Bert, 69003 Lyon','Salle d''escrime de Lyon'),
        (3,'33 Rue Crillon, 13005 Marseille','Salle d''escrime de Marseille'),
        (4,'53 Rue Pauline Kergomard, 33800 Bordeaux','Salle d''escrime de Bordeaux'),
        (5,'6 Rue Claudius Rougenet, 31500 Toulouse','Salle d''escrime de Toulouse'),
        (6,'Pl. Nouvelle Aventure, 59000 Lille','Salle d''escrime de Lille'),
        (7,'Rue Louis Joxe, 44200 Nantes','Salle d''escrime de Nantes'),
        (8,'43 Av. du Rhin, 67100 Strasbourg','Salle d''escrime de Strasbourg'),
        (9,'60 Pl. Jacques Mirouze, 34000 Montpellier','Salle d''escrime de Montpellier'),
        (10,'8 Av. des Gayeulles, 35700 Rennes','Salle d''escrime de Rennes'),
        (11,'Imp. Léo Lagrange, 51100 Reims','Salle d''escrime de Reims'),
        (12,'Rue du Dr Paul Michelon, 42000 Saint-Étienne','Salle d''escrime de Saint-Etienne'),
        (13,'25 Rue Lucien Joubert, 41000 Blois','Salle d''escrime de Blois');

INSERT INTO COMPETITION(idCompetition, nomCompetition, dateCompetition, saisonCompetition, idArme, idCategorie, idLieu, dateFinInscription, coefficientCompetition, isEquipe) values
        (8,'Competition de Nantes', '2024-05-23', 'printemps', 3, 2, 7, '2024-05-15', 0.8, false),
        (14, 'Competition en Equipe','2024-05-23','hiver',2,3,12,'2024-05-15',0.7,true);

INSERT INTO PISTE(idPiste, idLieu,descriptionPiste) VALUES
        (1, 1,'Piste 1'),
        (2, 1,'Piste 2'),
        (3, 1,'Piste 3'),
        (4, 1,'Piste 4'),
        (5,2,'Piste a'),
        (6,2,'Piste b'),
        (7,2,'Piste c'),
        (8,2,'Piste d'),
        (9,3,'Piste e'),
        (10,3,'Piste f'),
        (11,3,'Piste g'),
        (12,3,'Piste h'),
        (13,4,'Piste i'),
        (14,4,'Piste j'),
        (15,4,'Piste k'),
        (16,4,'Piste l'),
        (17,5,'Piste m'),
        (18,5,'Piste n'),
        (19,5,'Piste o'),
        (20,5,'Piste p'),
        (21,6,'Piste q'),
        (22,6,'Piste r'),
        (23,6,'Piste s'),
        (24,6,'Piste t'),
        (25,7,'Piste u'),
        (26,7,'Piste v'),
        (27,7,'Piste w'),
        (28,7,'Piste x'),
        (29,8,'Piste y'),
        (30,8,'Piste z'),
        (31,8,'Piste do'),
        (32,8,'Piste re'),
        (33,9,'Piste mi'),
        (34,9,'Piste fa'),
        (35,9,'Piste sol'),
        (36,9,'Piste la'),
        (37,10,'Piste si'),
        (38,10,'Piste do#'),
        (39,10,'Piste Marie Curie'),
        (40,10,'Piste Albert Einstein'),
        (41,11,'Piste Isaac Newton'),
        (42,11,'Piste Galilée'),
        (43,11,'Piste Charles Darwin'),
        (44,11,'Piste Stephen Hawking'),
        (45,12,'Piste IUT1'),
        (46,12,'Piste IUT2'),
        (47,12,'Piste  IUT3'),
        (48,12,'Piste IUT4'),
        (49,13,'Piste hehe'),
        (50,13,'Piste hoho'),
        (51,13,'Piste hihi'),
        (52,13,'Piste haha');



INSERT INTO INSCRIRE(idEscrimeur, idCompetition) VALUES
        (10,8),
        (11,8),
        (12,8),
        (13,8),
        (17,8);


INSERT INTO EQUIPE (idEquipe, nomEquipe, idCompetition) VALUES
        (1, "Equipe A", 14),
        (2, "Equipe B", 14),
        (3, "Equipe C", 14),
        (4, "Equipe D", 14);

INSERT INTO FAIT_PARTIE (idEscrimeur, idEquipe, role) VALUES
        (1, 1, "Tireur"),
        (2, 1, "Tireur"),
        (3, 1, "Tireur"),
        (4, 1, "Remplacent"),
        (5, 2, "Tireur"),
        (6, 2, "Tireur"),
        (7, 2, "Tireur"),
        (8, 2, "Remplacent"),
        (9, 3, "Tireur"),
        (10, 3, "Tireur"),
        (11, 3, "Tireur"),
        (12, 3, "Remplacent"),
        (13, 4, "Tireur"),
        (14, 4, "Tireur"),
        (15, 4, "Tireur"),
        (16, 4, "Remplacent");
