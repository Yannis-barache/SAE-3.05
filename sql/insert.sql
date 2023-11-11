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
        (15, 'Elkasmi','Hajar', '212212212', '1999-01-01', 'hajar', 'elkasmi', NULL, 11, 'F', 5, false),
        (16, 'Doe', 'Jane', '87654', '1999-01-01', 'janedoe', 'password', NULL, 2, 'F', 5, false),
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

INSERT INTO COMPETITION(idCompetition, nomCompetition, dateCompetition, saisonCompetition, idArme, idCategorie, idLieu, dateFinInscription, coefficientCompetition) values
        (1,'Championnat de France', '2024-03-15', 'hiver', 1, 2, 1, '2023-03-01', 0.8),
        (2,'Competition de Blois', '2024-03-15', 'été', 3, 3, 13, '2023-12-10', 0.6),
        (3,'Competition de Lyon', '2023-02-25', 'automne', 1, 2, 2, '2023-02-15', 0.7),
        (4,'Competition de Marseille', '2025-03-01', 'hiver', 2, 3, 3, '2025-02-20', 0.9),
        (5,'Competition de Bordeaux', '2021-02-18', 'hiver', 3, 1, 4, '2021-02-08', 0.5),
        (6,'Competition de Toulouse', '2023-11-10', 'été', 1, 3, 5, '2023-02-12', 0.6),
        (7,'Competition de Lille', '2023-11-09', 'été', 2, 1, 6, '2023-02-17', 0.7),
        (8,'Competition de Nantes', '2023-03-03', 'printemps', 3, 2, 7, '2023-02-23', 0.8),
        (9,'Competition de Strasbourg', '2023-02-16', 'printemps', 1, 3, 8, '2023-02-06', 0.4),
        (10,'Competition de Montpellier', '2023-02-21', 'hiver', 2, 1, 9, '2023-02-11', 0.5),
        (11,'Competition de Rennes', '2023-02-26', 'printemps', 3, 2, 10, '2023-02-16', 0.6),
        (12,'Competition de Reims', '2023-03-02', 'hiver', 1, 1, 11, '2023-02-22', 0.7),
        (13,'Competition de Saint-Etienne', '2023-02-23', 'hiver', 2, 3, 12, '2023-02-13', 0.8);


INSERT INTO PHASE(idPhase, idCompetition) VALUES
        (1, 1),
        (2, 1),
        (3, 1),
        (4, 1),
        (5, 1),
        (6, 2),
        (7, 2),
        (8, 2),
        (9, 2),
        (10, 2),
        (11, 2),
        (12, 2),
        (13, 2),
        (14, 2),
        (15, 3),
        (16, 3),
        (17, 3),
        (18, 3);

INSERT INTO PHASE_FINALE(idPhaseFinale) VALUES
        (1),
        (2),
        (3),
        (4),
        (5);
        

INSERT INTO POULE(idPoule) VALUES
        (6),
        (7),
        (8),
        (9),
        (10),
        (11),
        (12),
        (13),
        (14);


INSERT INTO MATCHS(idMatch,idEscrimeur1, idEscrimeur2, idPhase, idArbitre, heureMatch, fini) VALUES
        (1, 1, 2, 1, 10, '10:20:00',false),
        (2, 3, 4, 1, 2, '23:00:00',false),
        (3, 5, 6, 1, 3, '08:20:00',false),
        (4, 7, 8, 1, 4, '10:34:00',true),
        (5, 9, 10, 1, 5, '16:21:00',true),
        (6, 1, 3, 2, 6, '09:00:00',false),
        (7, 2, 4, 2, 7, '20:30:00',true),
        (8, 5, 7, 2, 8, '11:00:00',true),
        (9, 6, 8, 2, 9, '12:45:00',false),
        (10, 1, 2, 6, 10, 1, '10:20:00',false);


INSERT INTO INSCRIRE(idEscrimeur, idCompetition) VALUES
        (1,1),
        (1,2),
        (1,3);


INSERT INTO ARBITRER(idEscrimeur, idCompetition) VALUES
        (1,4),
        (1,5),
        (1,6),
        (3,1),
        (3,2),
        (3,3),
        (3,4),
        (3,5),
        (3,6),
        (4,1);


INSERT INTO TOUCHE(idMatch, idEscrimeur, numTouche) VALUES
        (1,1,1),
        (1,2,2),
        (1,1,3),
        (1,2,4),
        (1,1,5),
        (1,2,6),
        (1,1,7),
        (1,2,8),
        (1,1,9),
        (2,4,1),
        (2,3,2),
        (2,4,3),
        (2,3,4),
        (2,4,5),
        (2,3,6);
