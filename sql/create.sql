CREATE TABLE ARMES(
    idArme INT(10) AUTO_INCREMENT,
    nomArme VARCHAR(50),
    PRIMARY KEY (idArme)
);

CREATE TABLE CATEGORIE(
    idCategorie INT(10) AUTO_INCREMENT,
    nomCategorie VARCHAR(50),
    PRIMARY KEY (idCategorie)
);

CREATE TABLE CLUB(
    idClub INT(10) AUTO_INCREMENT,
    nomClub VARCHAR(50),
    adresse VARCHAR(50),
    PRIMARY KEY (idClub)
);

CREATE TABLE LIEU(
    idLieu INT(10) AUTO_INCREMENT,
    adresseLieu VARCHAR(100),
    descriptionLieu VARCHAR(1000),
    PRIMARY KEY (idLieu)

);

CREATE TABLE PHASE(
    idPhase INT(10) AUTO_INCREMENT,

    PRIMARY KEY (idPhase)
);

CREATE TABLE POULE(
    idPoule INT(10) AUTO_INCREMENT,
    PRIMARY KEY (idPoule)
);
CREATE TABLE ESCRIMEUR (
    idEscrimeur INT(10) AUTO_INCREMENT,
    nom VARCHAR(50),
    liscence boolean,
    prenom VARCHAR(50),
    dateNaissance DATE,
    nomUtilisateur VARCHAR(50),
    classement INT(10),
    PRIMARY KEY (idEscrimeur)
);

CREATE TABLE MATCHS(
    idEscrimeur1 INT(10),
    idEscrimeur2 INT(10),
    idPoule INT(10),
    PRIMARY KEY (idEscrimeur1,idEscrimeur2,idPoule),
    FOREIGN KEY (idEscrimeur1) REFERENCES ESCRIMEUR(idEscrimeur),
    FOREIGN KEY (idEscrimeur2) REFERENCES ESCRIMEUR(idEscrimeur),
    FOREIGN KEY (idPoule) REFERENCES POULE(idPoule)
);

CREATE TABLE TOUCHE(
    idMatch INT(10),
    idEscrimeur INT(10),
    numTouches INT(10),
    PRIMARY KEY (idMatch, idEscrimeur,numTouches),
    FOREIGN KEY (idEscrimeur) REFERENCES ESCRIMEUR(idEscrimeur)
);

CREATE TABLE COMPETITION(
    idCompetition INT(10) AUTO_INCREMENT,
    nomCompetition VARCHAR(50),
    dateCompetition DATE,
    saisonCompetition VARCHAR(50),
    idArme INT(10),
    idCategorie INT(10),
    dateFinInscription DATE,
    PRIMARY KEY (idCompetition)
);


CREATE TABLE ARBITRER(
    idEscrimeur INT(10),
    idCompetition INT(10),
    PRIMARY KEY (idCompetition,idEscrimeur),
    FOREIGN KEY (idCompetition) references COMPETITION(idCompetition),
    FOREIGN KEY (idEscrimeur) references ESCRIMEUR(idEscrimeur)
);

CREATE TABLE INSCRIRE(
    idEscrimeur INT(10),
    idCompetition INT(10),
    PRIMARY KEY (idCompetition,idEscrimeur),
    FOREIGN KEY (idCompetition) references COMPETITION(idCompetition),
    FOREIGN KEY (idEscrimeur) references ESCRIMEUR(idEscrimeur)
);

CREATE TABLE ETRE_DANS(
    idEscrimeur INT(10),
    idPoule INT(10),
    PRIMARY KEY (idEscrimeur,idPoule),
    FOREIGN KEY (idEscrimeur) references ESCRIMEUR(idEscrimeur),
    FOREIGN KEY (idPoule) references POULE(idPoule)
);



