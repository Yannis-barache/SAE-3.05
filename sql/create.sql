CREATE TABLE ARMES(
    idArme INT(10) AUTO_INCREMENT,
    nomArme VARCHAR(50),
    PRIMARY KEY (idArme)
);

CREATE TABLE ORGANISATEUR(
    idOrganisateur INT(10) AUTO_INCREMENT,
    nomOrganisateur VARCHAR(50),
    prenomOrganisateur VARCHAR(50),
    adresseMailOrganisateur VARCHAR(70),
    mdpOrganisateur VARCHAR(100),
    nomUtilisateur VARCHAR(50),
    PRIMARY KEY (idOrganisateur)
);

CREATE TABLE CATEGORIE(
    idCategorie INT(10) AUTO_INCREMENT,
    nomCategorie VARCHAR(50),
    PRIMARY KEY (idCategorie)
);

CREATE TABLE CLUB(
    idClub INT(10) AUTO_INCREMENT,
    nomClub VARCHAR(100),
    adresse VARCHAR(100),
    mdpClub VARCHAR(100),
    PRIMARY KEY (idClub)
);

CREATE TABLE LIEU(
    idLieu INT(10) AUTO_INCREMENT,
    adresseLieu VARCHAR(100),
    descriptionLieu VARCHAR(1000),
    PRIMARY KEY (idLieu)

);

CREATE TABLE COMPETITION(
    idCompetition INT(10) AUTO_INCREMENT,
    nomCompetition VARCHAR(50),
    dateCompetition DATE,
    saisonCompetition VARCHAR(50),
    idArme INT(10),
    idCategorie INT(10),
    idLieu INT(10),
    dateFinInscription DATE,
    coefficientCompetition INT(10),
    PRIMARY KEY (idCompetition),
    FOREIGN KEY (idArme) REFERENCES ARMES(idArme),
    FOREIGN KEY (idCategorie) REFERENCES CATEGORIE(idCategorie),
    FOREIGN KEY (idLieu) REFERENCES LIEU(idLieu)
);


CREATE TABLE PHASE(
    idPhase INT(10) AUTO_INCREMENT,
    idCompetition INT(10),
    PRIMARY KEY (idPhase,idCompetition),
    FOREIGN KEY (idCompetition) REFERENCES COMPETITION(idCompetition)
);

CREATE TABLE POULE(
    idPoule INT(10) AUTO_INCREMENT,
    idArbitre INT(10),
    PRIMARY KEY (idPoule,idArbitre),
    FOREIGN KEY (idPoule) REFERENCES PHASE(idPhase)
);

CREATE TABLE PHASE_FINALE(
    idPhaseFinale INT(10) AUTO_INCREMENT,
    PRIMARY KEY (idPhaseFinale),
    FOREIGN KEY (idPhaseFinale) REFERENCES PHASE(idPhase)
);

CREATE TABLE ESCRIMEUR (
    idEscrimeur INT(10) AUTO_INCREMENT,
    nom VARCHAR(50),
    liscence boolean,
    prenom VARCHAR(50),
    dateNaissance DATE,
    nomUtilisateurEscrimeur VARCHAR(50),
    mdpEscrimeur VARCHAR(100),
    classement INT(10),
    idClub INT(10),
    PRIMARY KEY (idEscrimeur),
    FOREIGN KEY (idClub) REFERENCES CLUB(idClub)
);

CREATE TABLE MATCHS(
    idMatch INT(10) AUTO_INCREMENT,
    idEscrimeur1 INT(10),
    idEscrimeur2 INT(10),
    idPhase INT(10),
    PRIMARY KEY (idMatch),
    FOREIGN KEY (idEscrimeur1) REFERENCES ESCRIMEUR(idEscrimeur),
    FOREIGN KEY (idEscrimeur2) REFERENCES ESCRIMEUR(idEscrimeur),
    FOREIGN KEY (idPhase) REFERENCES PHASE(idPhase)
);

CREATE TABLE TOUCHE(
    idMatch INT(10),
    idEscrimeur INT(10),
    numTouche INT(10),
    PRIMARY KEY (idMatch,numTouche),
    FOREIGN KEY (idMatch) REFERENCES MATCHS(idMatch),
    FOREIGN KEY (idEscrimeur) REFERENCES ESCRIMEUR(idEscrimeur)
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
