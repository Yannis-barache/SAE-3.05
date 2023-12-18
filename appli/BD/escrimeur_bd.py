"""
    Fichier qui contient les requêtes SQL pour la table Escrimeur
"""

from sqlalchemy import text
import sys
import os
from club_bd import ClubBD
from categorie_bd import CategorieBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from escrimeur import Escrimeur


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
            query = text(
                'SELECT idEscrimeur, nomEscrimeur, licence, prenomEscrimeur, '
                'dateNaissance, nomUtilisateurEscrimeur, mdpEscrimeur, classement, '
                'sexeEscrimeur, idClub, idCategorie, arbitrage FROM ESCRIMEUR')
            result = self.__connexion.execute(query)
            escrimeurs = []

            for (id_escrimeur, nom, licence, prenom, date_naissance,
                 nom_utilisateur, mdp, classement, sexe, id_club, id_categorie,
                 arbitrage) in result:
                arbitrage = arbitrage == 1
                club = ClubBD(self.__connexion).get_club_by_id(id_club)
                categorie = CategorieBD(
                    self.__connexion).get_categorie_by_id(id_categorie)

                escrimeurs.append(
                    Escrimeur(id_escrimeur, nom, prenom, sexe, date_naissance,
                              nom_utilisateur, mdp, licence, classement, club,
                              categorie, arbitrage))
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
            query = text(
                'SELECT idEscrimeur, nomEscrimeur, licence, prenomEscrimeur, '
                'dateNaissance, nomUtilisateurEscrimeur, mdpEscrimeur, classement, '
                'sexeEscrimeur, idClub, idCategorie, arbitrage '
                'FROM ESCRIMEUR WHERE idEscrimeur = ' + str(id_e))
            result = self.__connexion.execute(query)

            for (id_escrimeur, nom, licence, prenom, date_naissance,
                 nom_utilisateur, mdp, classement, sexe, id_club, id_categorie,
                 arbitrage) in result:
                arbitrage = arbitrage == 1
                club = ClubBD(self.__connexion).get_club_by_id(id_club)
                categorie = CategorieBD(
                    self.__connexion).get_categorie_by_id(id_categorie)

                return Escrimeur(id_escrimeur, nom, prenom, sexe,
                                 date_naissance, nom_utilisateur, mdp, licence,
                                 classement, club, categorie, arbitrage)
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
            if escrimeur.get_classement() is None:
                classement = 'NULL'
            else:
                classement = str(escrimeur.get_classement())
            query = text(
                f"INSERT INTO ESCRIMEUR (nomEscrimeur, licence, "
                f"prenomEscrimeur, dateNaissance, nomUtilisateurEscrimeur, "
                f"mdpEscrimeur, classement, sexeEscrimeur, idClub, idCategorie, "
                f"arbitrage) VALUES ('{escrimeur.get_nom()}', "
                f"'{escrimeur.get_licence()}', '{escrimeur.get_prenom()}', "
                f"'{escrimeur.get_date_naissance()}', "
                f"'{escrimeur.get_nom_utilisateur()}', "
                f"'{escrimeur.get_mdp()}', {classement}, "
                f"'{escrimeur.get_sexe()}', {escrimeur.get_club().get_id()}, "
                f"{str(escrimeur.get_categorie().get_id())}, {str(escrimeur.get_arbitrage())})"
            )
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            raise e

    def delete_escrimeur_by_nom(self, nom: str):
        """
        Fonction qui supprime un escrimeur en fonction de son nom
        :param nom: nom de l'escrimeur
        """
        try:
            query = text("DELETE FROM ESCRIMEUR WHERE nomEscrimeur ='" + nom +
                         "'")
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None

    def login_escrimeur(self, login_escrimeur: int, login_mdp: str):
        """
        Fonction qui permet de vérifier les identifiants d'un escrimeur
        :param login_escrimeur: licence de l'escrimeur
        :param login_mdp: mdp de l'escrimeur
        :return: escrimeur
        """
        try:
            query = text(
                'SELECT idEscrimeur, nomEscrimeur, licence, prenomEscrimeur, '
                'dateNaissance, nomUtilisateurEscrimeur, mdpEscrimeur, classement, '
                'sexeEscrimeur, idClub, idCategorie, arbitrage '
                'FROM ESCRIMEUR WHERE licence = ' + str(login_escrimeur))
            result = self.__connexion.execute(query)

            for (id_escrimeur, nom, licence, prenom, date_naissance,
                 nom_utilisateur, mdp, classement, sexe, id_club, id_categorie,
                 arbitrage) in result:

                fonction = text('SELECT verif_mdp_escrimeur(:id, :mdp)')
                result = self.__connexion.execute(fonction, {
                    "id": id_escrimeur,
                    "mdp": login_mdp
                })
                if result.fetchone()[0] == 0:
                    return None

                arbitrage = arbitrage == 1
                club = ClubBD(self.__connexion).get_club_by_id(id_club)
                categorie = CategorieBD(
                    self.__connexion).get_categorie_by_id(id_categorie)

                return Escrimeur(id_escrimeur, nom, prenom, sexe,
                                 date_naissance, nom_utilisateur, mdp, licence,
                                 classement, club, categorie, arbitrage)
        except Exception as e:
            print(e)
            return None
