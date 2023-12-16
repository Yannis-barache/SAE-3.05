CREATE TABLE ARMES(
    idArme INT(10) AUTO_INCREMENT,
    nomArme VARCHAR(50),
    sexeArme VARCHAR(1),
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
    coefficientCompetition decimal(3,3),
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
    licence VARCHAR(50),
    prenomEscrimeur VARCHAR(50),
    dateNaissance DATE,
    nomUtilisateurEscrimeur VARCHAR(50),
    mdpEscrimeur VARCHAR(100),
    classement INT(10),
    idClub INT(10) NOT NULL,
    sexeEscrimeur VARCHAR(1),
    idCategorie INT(10) NOT NULL,
    arbitrage BOOLEAN default false,
    PRIMARY KEY (idEscrimeur),
    FOREIGN KEY (idClub) REFERENCES CLUB(idClub),
    FOREIGN KEY (idCategorie) REFERENCES CATEGORIE(idCategorie)
);

CREATE TABLE ARBITRER(
    idEscrimeur INT(10) NOT NULL,
    idCompetition INT(10) NOT NULL,
    PRIMARY KEY (idCompetition,idEscrimeur),
    FOREIGN KEY (idCompetition) references COMPETITION(idCompetition),
    FOREIGN KEY (idEscrimeur) references ESCRIMEUR(idEscrimeur)
);

CREATE TABLE MATCHS(
    idMatch INT(10) AUTO_INCREMENT NOT NULL,
    idEscrimeur1 INT(10) NOT NULL,
    idEscrimeur2 INT(10) NOT NULL,
    idPhase INT(10) NOT NULL,
    idArbitre INT(10) NOT NULL,
    heureMatch TIME,
    fini boolean,
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





CREATE TABLE INSCRIRE(
    idEscrimeur INT(10) NOT NULL,
    idCompetition INT(10) NOT NULL,
    PRIMARY KEY (idCompetition,idEscrimeur),
    FOREIGN KEY (idCompetition) references COMPETITION(idCompetition),
    FOREIGN KEY (idEscrimeur) references ESCRIMEUR(idEscrimeur)
);

-- TRIGGER

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
-- delimiter |
-- CREATE OR REPLACE trigger meme_arbitre_poule before insert on MATCHS
-- for each row
--  begin
--        if (select count(*) from MATCHS where idPhase = new.idPhase and idArbitre = new.idArbitre) > 0 then
--            signal sqlstate '45000' set message_text = 'Un arbitre ne peut pas arbitrer deux poules';
--    end if;
--    end |
-- delimiter ;


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
delimiter ;

-- TRIGGER qui bloque l'inscription par le sexe de l'escrimeur
DELIMITER |
CREATE OR REPLACE TRIGGER meme_sexe BEFORE INSERT ON INSCRIRE
FOR EACH ROW
BEGIN
    IF (SELECT sexeEscrimeur FROM ESCRIMEUR WHERE idEscrimeur = NEW.idEscrimeur) != (SELECT sexeArme FROM ARMES WHERE idArme = (SELECT idArme FROM COMPETITION WHERE idCompetition = NEW.idCompetition)) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Un escrimeur ne peut pas s''inscrire dans une compétition qui ne correspond pas à son sexe';
    END IF;
END|
DELIMITER ;

-- TRIGGER qui bloque l'inscription par la catégorie de l'escrimeur si la catégorie est inférieure (l'id correspond)
delimiter |
CREATE OR REPLACE trigger meme_categorie before insert on INSCRIRE
for each row
begin
    if (select idCategorie from ESCRIMEUR where idEscrimeur = new.idEscrimeur) < (select idCategorie from COMPETITION where idCompetition = new.idCompetition) then
        signal sqlstate '45000' set message_text = 'Un escrimeur ne peut pas s''inscrire dans une compétition qui une catégorie moins elevée que la sienne';
    end if;
end |

-- Trigger permettant une insertion seulement si l'escrimeur peut arbitrer
delimiter |
create or replace trigger peut_arbitrer before insert on ARBITRER
for each row
begin
    if (select arbitrage from ESCRIMEUR where idEscrimeur = new.idEscrimeur) = false then
        signal sqlstate '45000' set message_text = 'Un escrimeur ne peut pas arbitrer s''il n''est pas arbitre';
    end if;
end |
delimiter ;

-- Trigger permettant une insertion seulement si le joueur est dans le match
delimiter |
create or replace trigger est_dans_match before insert on TOUCHE
for each row
begin
    declare trouve boolean default false;
    if (select count(*) from MATCHS where idEscrimeur1=new.idEscrimeur and idMatch=new.idMatch) > 0 then
        set trouve=true;
    end if;
    if (select count(*) from MATCHS where idEscrimeur2=new.idEscrimeur and idMatch=new.idMatch) > 0 then
        set trouve=true;
    end if;

    if trouve=false then
        signal sqlstate '45000' set message_text = 'Un escrimeur ne peut pas ajouter de touche dans un match où il n''est pas';
    end if;
end |
delimiter ;

-- Trigger qui bloque l'inscription d'un arbitre dans un match si il est déjà inscrit en tant qu'arbitre dans ce match
DELIMITER |
CREATE OR REPLACE trigger tireur_pasarbitre before insert on MATCHS
for each row
BEGIN
    if (select count(*) from MATCHS where new.idEscrimeur1=new.idArbitre or new.idEscrimeur2=new.idArbitre) > 0 then
        signal sqlstate '45000' set message_text = 'Un tireur ne peut pas arbitrer un match';
    end if;
END|
DELIMITER ;

-- Trigger qui permet de pas avoir de duplicat de licence
delimiter |
CREATE OR REPLACE trigger num_licence before insert on ESCRIMEUR
for each row
begin
    if (select count(*) from ESCRIMEUR where licence = new.licence) > 0 then
        signal sqlstate '45000' set message_text = 'La licence appartient à quelqu''un d''autre';
    end if;
end |
delimiter ;

-- Trigger qui permet de mettre à jour le match quand il est fini
delimiter |
CREATE OR REPLACE trigger update_fini after insert on TOUCHE
for each row
begin
    declare nbTouchePhase int;
    if ((select count(*) from MATCHS natural join PHASE natural join POULE)>0) then
        set nbTouchePhase= 5;
    else
        set nbTouchePhase= 15;
    end if;

    if ((select count(*) from TOUCHE where idMatch=new.idMatch and idEscrimeur=new.idEscrimeur)=nbTouchePhase) then
        update MATCHS set fini=true where idMatch=new.idMatch;
    end if;
end |
delimiter ;

-- Trigger qui bloque l'ajout d'une touche dans un match fini
delimiter |
CREATE OR REPLACE trigger match_fini before insert on TOUCHE
for each row
begin
    if (select fini from MATCHS where idMatch=new.idMatch) = true then
        signal sqlstate '45000' set message_text = 'Le match est fini vous ne pouvez pas ajouter de touche';
    end if;
end |
delimiter ;


-- Trigger qui crypte le mot de passe de l'escrimeur
delimiter |
CREATE OR REPLACE trigger crypte_mdp before insert on ESCRIMEUR
for each row
begin
    set new.mdpEscrimeur=sha1(new.mdpEscrimeur);
end |
delimiter ;

-- Trigger qui crypte le mot de passe de l'organisateur
delimiter |
CREATE OR REPLACE trigger crypte_mdp2 before insert on ORGANISATEUR
for each row
begin
    set new.mdpOrganisateur=sha1(new.mdpOrganisateur);
end |
delimiter ;

-- Trigger qui crypte le mot de passe du club
delimiter |
CREATE OR REPLACE trigger crypte_mdp3 before insert on CLUB
for each row
begin
    set new.mdpClub=sha1(new.mdpClub);
end |
delimiter ;


-- PROCEDURE


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

-- Procedure pour permettre d'ajouter une touche a la table TOUCHE
delimiter |
CREATE OR REPLACE procedure ajoute_touche(IN idMatchA int, IN idEscrimeurA int)
begin
    declare nbTouche int;
    set nbTouche= (select count(*) from TOUCHE where idMatch=idMatchA);
    insert into TOUCHE(idMatch,idEscrimeur,numTouche) values (idMatchA,idEscrimeurA,nbTouche+1);
end |
delimiter ;


-- Procure permettant d'ajouter un escrimeur dans la base de données
delimiter |
CREATE OR REPLACE procedure ajoute_escrimeur(IN nomEscrimeurA varchar(50), IN licenceA varchar(50), IN prenomEscrimeurA varchar(50), IN dateNaissanceA date, IN nomUtilisateurEscrimeurA varchar(50), IN mdpEscrimeurA varchar(100), IN classementA int, IN idClubA int, IN sexeEscrimeurA varchar(1), IN idCategorieA int, IN arbitrageA boolean)
begin
    insert into ESCRIMEUR(nomEscrimeur,licence,prenomEscrimeur,dateNaissance,nomUtilisateurEscrimeur,mdpEscrimeur,classement,idClub,sexeEscrimeur,idCategorie,arbitrage) values (nomEscrimeurA,licenceA,prenomEscrimeurA,dateNaissanceA,nomUtilisateurEscrimeurA,mdpEscrimeurA,classementA,idClubA,sexeEscrimeurA,idCategorieA,arbitrageA);
end |
delimiter ;
-- FONCTIONS

-- Fonction qui compare le mdp passée en paramètre avec le mdp de l'escrimeur
delimiter |
CREATE OR REPLACE function verif_mdp_escrimeur(idEscrimeurA int, mdpEscrimeurA varchar(100)) returns boolean
begin
    declare mdp varchar(100);
    set mdpEscrimeurA=sha1(mdpEscrimeurA);
    set mdp= (select mdpEscrimeur from ESCRIMEUR where idEscrimeur=idEscrimeurA);
    if mdp=mdpEscrimeurA then
        return true;
    else
        return false;
    end if;
end |
delimiter ;

-- Fonction qui compare le mdp passée en paramètre avec le mdp de l'organisateur
delimiter |
CREATE OR REPLACE function verif_mdp_organisateur(idOrganisateurA int, mdpOrganisateurA varchar(100)) returns boolean
begin
    declare mdp varchar(100);
    set mdpOrganisateurA=sha1(mdpOrganisateurA);
    set mdp= (select mdpOrganisateur from ORGANISATEUR where idOrganisateur=idOrganisateurA);
    if mdp=mdpOrganisateurA then
        return true;
    else
        return false;
    end if;
end |
delimiter ;

-- Fonction qui compare le mdp passée en paramètre avec le mdp du club
delimiter |
CREATE OR REPLACE function verif_mdp_club(idClubA int, mdpClubA varchar(100)) returns boolean
begin
    declare mdp varchar(100);
    set mdpClubA=sha1(mdpClubA);
    set mdp= (select mdpClub from CLUB where idClub=idClubA);
    if mdp=mdpClubA then
        return true;
    else
        return false;
    end if;
end |
delimiter ;





