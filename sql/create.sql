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
    idArme INT(10) NOT NULL,
    idCategorie INT(10) NOT NULL,
    idLieu INT(10) NOT NULL,
    dateFinInscription DATE,
    coefficientCompetition INT(10),
    PRIMARY KEY (idCompetition),
    FOREIGN KEY (idArme) REFERENCES ARMES(idArme),
    FOREIGN KEY (idCategorie) REFERENCES CATEGORIE(idCategorie),
    FOREIGN KEY (idLieu) REFERENCES LIEU(idLieu)
);


CREATE TABLE PHASE(
    idPhase INT(10) AUTO_INCREMENT,
    idCompetition INT(10) NOT NULL,
    PRIMARY KEY (idPhase),
    FOREIGN KEY (idCompetition) REFERENCES COMPETITION(idCompetition)
);

CREATE TABLE POULE(
    idPoule INT(10) not null ,
    PRIMARY KEY (idPoule),
    FOREIGN KEY (idPoule) REFERENCES PHASE(idPhase)
);

CREATE TABLE PHASE_FINALE(
    idPhaseFinale INT(10) AUTO_INCREMENT,
    PRIMARY KEY (idPhaseFinale),
    FOREIGN KEY (idPhaseFinale) REFERENCES PHASE(idPhase)
);

CREATE TABLE ESCRIMEUR (
    idEscrimeur INT(10) AUTO_INCREMENT,
    nomEscrimeur VARCHAR(50),
    liscence VARCHAR(50),
    prenomEscrimeur VARCHAR(50),
    dateNaissance DATE,
    nomUtilisateurEscrimeur VARCHAR(50),
    mdpEscrimeur VARCHAR(100),
    classement INT(10),
    idClub INT(10) NOT NULL,
    sexeEscrimeur VARCHAR(1),
    idCategorie INT(10) NOT NULL,
    PRIMARY KEY (idEscrimeur),
    FOREIGN KEY (idClub) REFERENCES CLUB(idClub),
    FOREIGN KEY (idCategorie) REFERENCES CATEGORIE(idCategorie)
);

CREATE TABLE MATCHS(
    idMatch INT(10) AUTO_INCREMENT NOT NULL,
    idEscrimeur1 INT(10) NOT NULL,
    idEscrimeur2 INT(10) NOT NULL,
    idPhase INT(10) NOT NULL,
    idArbitre INT(10) NOT NULL,
    heureMatch TIME,
    PRIMARY KEY (idMatch),
    FOREIGN KEY (idEscrimeur1) REFERENCES ESCRIMEUR(idEscrimeur),
    FOREIGN KEY (idEscrimeur2) REFERENCES ESCRIMEUR(idEscrimeur),
    FOREIGN KEY (idPhase) REFERENCES PHASE(idPhase),
    FOREIGN KEY (idArbitre) REFERENCES ESCRIMEUR(idEscrimeur)
);

CREATE TABLE TOUCHE(
    idMatch INT(10) NOT NULL,
    idEscrimeur INT(10) NOT NULL ,
    numTouche INT(10),
    PRIMARY KEY (idMatch,numTouche),
    FOREIGN KEY (idMatch) REFERENCES MATCHS(idMatch),
    FOREIGN KEY (idEscrimeur) REFERENCES ESCRIMEUR(idEscrimeur)
);



CREATE TABLE ARBITRER(
    idEscrimeur INT(10) NOT NULL,
    idCompetition INT(10) NOT NULL,
    PRIMARY KEY (idCompetition,idEscrimeur),
    FOREIGN KEY (idCompetition) references COMPETITION(idCompetition),
    FOREIGN KEY (idEscrimeur) references ESCRIMEUR(idEscrimeur)
);

CREATE TABLE INSCRIRE(
    idEscrimeur INT(10) NOT NULL,
    idCompetition INT(10) NOT NULL,
    PRIMARY KEY (idCompetition,idEscrimeur),
    FOREIGN KEY (idCompetition) references COMPETITION(idCompetition),
    FOREIGN KEY (idEscrimeur) references ESCRIMEUR(idEscrimeur)
);


-- TRIGGER qui va permettre de na pas ajouter dans phase_finale un id de phase déjà présent dans poule
delimiter |
CREATE OR REPLACE trigger meme_phase before insert on PHASE_FINALE
for each row
    begin
        if (select count(*) from POULE where idPoule = new.idPhaseFinale) > 0 then
            signal sqlstate '45000' set message_text = 'Une phase ne peut pas être à la fois une phase finale et une poule';
    end if;
    end |
delimiter ;

-- TRIGGER qui va permettre de na pas ajouter dans poule un id de phase déjà présent dans phase_finale
delimiter |
CREATE OR REPLACE trigger meme_phase2 before insert on POULE
for each row
    begin
        if (select count(*) from PHASE_FINALE where idPhaseFinale = new.idPoule) > 0 then
            signal sqlstate '45000' set message_text = 'Une phase ne peut pas être à la fois une phase finale et une poule';
    end if;
    end |
delimiter ;



-- TRIGGER qui permet de bloquer l'assignement d'un arbitre à une poule où un arbitre a deja été désigne. Une poule a un seul arbitre qui ne peut arbitrer dans une autre poule
delimiter |
CREATE OR REPLACE trigger meme_arbitre_poule before insert on MATCHS
for each row
    begin
        if (select count(*) from MATCHS where idPhase = new.idPhase and idArbitre = new.idArbitre) > 0 then
            signal sqlstate '45000' set message_text = 'Un arbitre ne peut pas arbitrer deux poules';
    end if;
    end |
delimiter ;


-- TRIGGER qui va permettre de bloquer l'inscription en tant qu'arbitre si un escrimeur est deja inscrit en tant que tireur
delimiter |
CREATE OR REPLACE trigger meme_escrimeur before insert on ARBITRER
for each row
begin
        if (select count(*) from INSCRIRE where idEscrimeur = new.idEscrimeur and idCompetition = new.idCompetition) > 0 then
            signal sqlstate '45000' set message_text = 'Un escrimeur ne peut pas être à la fois tireur et arbitre';
    end if;
end |
delimiter ;


-- TRIGGER qui va permettre de bloquer l'inscription en tant que tireur si un escrimeur est deja inscrit en tant que arbitre
delimiter |
CREATE OR REPLACE trigger meme_escrimeur2 before insert on INSCRIRE
for each row
begin
    if (select count(*) from ARBITRER where idEscrimeur = new.idEscrimeur and idCompetition = new.idCompetition) > 0 then
        signal sqlstate '45000' set message_text = 'Un escrimeur ne peut pas être à la fois tireur et arbitre';
    end if;
end |

-- Procédure qui permet de créer une poule à partir d'une phase
delimiter |
CREATE OR REPLACE PROCEDURE creer_poule(IN idPhase INT(10))
begin
    INSERT INTO POULE(idPoule) VALUES (idPhase);
end |
delimiter ;

-- Procédure qui permet de créer une phase finale à partir d'une phase
delimiter |
CREATE OR REPLACE PROCEDURE creer_phase_finale(IN idPhase INT(10))
begin
    INSERT INTO PHASE_FINALE(idPhaseFinale) VALUES (idPhase);
end |
delimiter ;


DELIMITER |
CREATE FUNCTION CalculerClassementProvisoire(
    escrimeur_id INT,
    phase_id INT
)
RETURNS INT
BEGIN
    DECLARE victoires INT;
    DECLARE touches_donnes INT;
    DECLARE touches_recues INT;
    DECLARE indice INT;

    -- Calculer le nombre de victoires de l'escrimeur dans la phase
    SET victoires = (SELECT COUNT(*) FROM MATCHS natural join TOUCHE WHERE (idEscrimeur1 = escrimeur_id OR idEscrimeur2 = escrimeur_id) AND idPhase = phase_id AND numTouche = 15);

    -- Calculer les touches données et reçues par l'escrimeur dans la phase
    SET touches_donnes = (SELECT COUNT(*) FROM TOUCHE WHERE idEscrimeur = escrimeur_id AND idMatch IN (SELECT idMatch FROM MATCHS WHERE idPhase = phase_id));
    SET touches_recues = (SELECT COUNT(*) FROM TOUCHE WHERE idMatch IN (SELECT idMatch FROM MATCHS WHERE idPhase = phase_id) AND idEscrimeur <> escrimeur_id);

    -- Calculer l'indice
    SET indice = touches_donnes - touches_recues;

    -- Calculer le classement provisoire
    SET @classement_provisoire = (victoires * 3) + (CASE WHEN indice > 0 THEN 2 ELSE 0 END);

    RETURN @classement_provisoire;
END|
DELIMITER ;

-- Fonction qui renvoie l'id des compétitions auquel un escrimeur s'est inscrit en tant que tireur
DELIMITER |
CREATE FUNCTION getCompetitionsTireur(escrimeur_id INT) RETURNS VARCHAR(1000)
BEGIN
    DECLARE competitions VARCHAR(1000);
    DECLARE competition_id INT;
    DECLARE done INT DEFAULT FALSE;
    DECLARE inscription CURSOR FOR SELECT idCompetition FROM INSCRIRE WHERE idEscrimeur = escrimeur_id;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    SET competitions = '';
    OPEN inscription;
    while not done do
        FETCH inscription INTO competition_id;
        IF NOT done THEN
            SET competitions = CONCAT(competitions, competition_id, ', ');
        END IF;
    end while;
END|
DELIMITER ;

-- Fonction qui renvoie l'id des compétitions auquel un escrimeur s'est inscrit en tant que arbitre
DELIMITER |
CREATE FUNCTION getCompetitionsArbitre(escrimeur_id INT) RETURNS VARCHAR(1000)
begin
    DECLARE competitions VARCHAR(1000);
    DECLARE competition_id INT;
    DECLARE done INT DEFAULT FALSE;
    DECLARE inscription CURSOR FOR SELECT idCompetition FROM ARBITRER WHERE idEscrimeur = escrimeur_id;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    SET competitions = '';
    OPEN inscription;
    while not done do
        FETCH inscription INTO competition_id;
        IF NOT done THEN
            SET competitions = CONCAT(competitions, competition_id, ', ');
        END IF;
    end while;
end |
DELIMITER ;



