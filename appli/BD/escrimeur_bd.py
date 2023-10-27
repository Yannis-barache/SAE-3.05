"""
    Fichier qui contient les requêtes SQL pour la table Escrimeur
"""

from sqlalchemy import text
from appli.modele.escrimeur import Escrimeur
from appli.BD.club_bd import ClubBD
from appli.BD.categorie_bd import CategorieBD


class EscrimeurBD:
    """
    Classe EscrimeurBD
    """
    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_escrimeur(self):
        """
        Fonction qui retourne tous les escrimeurs
        :return: liste d'escrimeur
        """
        try:
            query = text("SELECT idEscrimeur, nomEscrimeur, licence, prenomEscrimeur, "
                         "dateNaissance, nomUtilisateurEscrimeur, mdpEscrimeur, classement, "
                         "sexeEscrimeur, idClub, idCategorie, arbitrage FROM ESCRIMEUR")
            result = self.__connexion.execute(query)
            escrimeurs = []

            for (id_escrimeur, nom, licence, prenom, date_naissance, nom_utilisateur, mdp,
                 classement, sexe, id_club, id_categorie, arbitrage) in result:

                if arbitrage == 1:
                    arbitrage = True
                else:
                    arbitrage = False

                club = ClubBD(self.__connexion).get_club_by_id(id_club)
                categorie = CategorieBD(self.__connexion).get_categorie_by_id(id_categorie)

                escrimeurs.append(Escrimeur(id_escrimeur, nom, prenom, sexe, date_naissance,
                                            nom_utilisateur, mdp, licence, classement,
                                            club, categorie, arbitrage))
            return escrimeurs
        except Exception as e:
            print(e)
            return None

    def get_escrimeur_by_id(self, id_e: int):
        """
        Fonction qui retourne un escrimeur en fonction de son id
        :param id_e: id de l'escrimeur
        :return: escrimeur
        """
        try:
            query = text("SELECT idEscrimeur, nomEscrimeur, licence, prenomEscrimeur, "
                         "dateNaissance, nomUtilisateurEscrimeur, mdpEscrimeur, classement, "
                         "sexeEscrimeur, idClub, idCategorie, arbitrage "
                         "FROM ESCRIMEUR WHERE idEscrimeur = " + str(id_e))
            result = self.__connexion.execute(query)

            for (id_escrimeur, nom, licence, prenom, date_naissance, nom_utilisateur,
                 mdp, classement, sexe, id_club, id_categorie, arbitrage) in result:

                if arbitrage == 1:
                    arbitrage = True
                else:
                    arbitrage = False

                club = ClubBD(self.__connexion).get_club_by_id(id_club)
                categorie = CategorieBD(self.__connexion).get_categorie_by_id(id_categorie)

                return Escrimeur(id_escrimeur, nom, prenom, sexe, date_naissance,
                                 nom_utilisateur, mdp, licence, classement, club,
                                 categorie, arbitrage)
            return None
        except Exception as e:
            print(e)
            return None

    def insert_escrimeur(self, escrimeur: Escrimeur):
        """
        Fonction qui insère un escrimeur
        :param escrimeur : escrimeur
        """
        try:
            query = text(f"INSERT INTO ESCRIMEUR (nomEscrimeur, licence, "
                         f"prenomEscrimeur, dateNaissance, nomUtilisateurEscrimeur, "
                         f"mdpEscrimeur, classement, sexeEscrimeur, idClub, idCategorie, "
                         f"arbitrage) VALUES ('{escrimeur.get_nom()}', "
                         f"'{escrimeur.get_licence()}', '{escrimeur.get_prenom()}', "
                         f"'{escrimeur.get_date_naissance()}', '{escrimeur.get_nom_utilisateur()}', "
                         f"'{escrimeur.get_mdp()}', {str(escrimeur.get_classement())}, "
                         f"'{escrimeur.get_sexe()}', {str(escrimeur.get_club())}, "
                         f"{str(escrimeur.get_categorie())}, {str(escrimeur.get_arbitrage())})")
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None
