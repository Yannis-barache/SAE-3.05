"""
    Fichier qui contient les requêtes SQL pour la table Club
"""

import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from club import Club


class ClubBD:
    """
    Classe ClubBD
    """

    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_club(self):
        """
        Fonction qui retourne tous les clubs
        :return: liste de Club
        """
        try:
            query = text('SELECT idClub, nomClub, adresse, mdpClub FROM CLUB')
            result = self.__connexion.execute(query)
            clubs = []
            for id_club, nom, adresse, mdp in result:
                clubs.append(Club(id_club, nom, adresse, mdp))
            return clubs
        except Exception as e:
            print(e)
            return None

    def get_all_club_2(self):
        """
        Fonction qui retourne tous les clubs
        :return: liste de Club
        """
        try:
            query = text('SELECT idClub, nomClub, adresse, mdpClub FROM CLUB')
            result = self.__connexion.execute(query)
            clubs = []
            for id_club, nom, adresse, mdp in result:
                nombre_member = self.get_nb_licencies(id_club)
                clubs.append((Club(id_club, nom, adresse, mdp), nombre_member))
            return clubs
        except Exception as e:
            print(e)
            return None

    def get_nb_licencies(self, id_cl: int):
        """
        Fonction qui retourne le nombre de licenciés d'un club
        :param id_cl: id du club
        :return: nombre de licenciés
        """
        try:
            query = text(
                'SELECT count(*) FROM CLUB NATURAL JOIN ESCRIMEUR where idClub ='
                + str(id_cl))
            result = self.__connexion.execute(query)
            for nb in result:
                return nb[0]
        except Exception as e:
            print(e)
            return None

    def get_club_by_id(self, id_cl: int):
        """
        Fonction qui retourne un club en fonction de son id
        :param id_cl: id du club
        :return: club
        """
        try:
            query = text('SELECT idClub, nomClub, adresse, mdpClub '
                         'FROM CLUB WHERE idClub =' + str(id_cl))
            result = self.__connexion.execute(query)
            for id_club, nom, adresse, mdp in result:
                return Club(id_club, nom, adresse, mdp)
            return None
        except Exception as e:
            print(e)
            return None

    def insert_club(self, club: Club):
        """
        Fonction qui insère un club
        :param club : club
        """
        try:
            query = text(
                f"INSERT INTO CLUB (nomClub, adresse, mdpClub) VALUES "
                f"('{club.get_nom()}','"
                f"{club.get_adresse()}','{club.get_mdp()}')")
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None

    def delete_club(self, id_cl: int):
        """
        Fonction qui supprime un club
        :param id_cl: id du club
        """
        try:
            query = text('DELETE FROM CLUB WHERE idClub =' + str(id_cl))
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None

    def delete_club_by_nom(self, nom_cl: str):
        """
        Fonction qui supprime un club
        :param nom_cl: nom du club
        """
        try:
            query = text("DELETE FROM CLUB WHERE nomClub ='" + nom_cl + "'")
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None

    def update_club(self, club: Club):
        """
        Fonction qui met à jour un club
        :param club: club
        """
        try:
            query = text(
                f"UPDATE CLUB SET nomClub = '{club.get_nom()}', adresse = '{club.get_adresse()}', "
                f"mdpClub = '{club.get_mdp()}' WHERE idClub = {club.get_id()}")
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None

    def login_club(self, login_club: str, login_mdp: str):
        """
        Fonction qui vérifie les identifiants d'un club
        :param login_club: nom du club
        :param login_mdp: mot de passe du club
        :return: club
        """
        try:
            query = text(f"SELECT idClub, nomClub, adresse, mdpClub "
                         f"FROM CLUB WHERE nomClub = '{login_club}'")
            result = self.__connexion.execute(query)
            for id_club, nom, adresse, mdp in result:
                fonction = text("SELECT verif_mdp_club(:id, :mdp)")
                result = self.__connexion.execute(fonction, {
                    "id": id_club,
                    "mdp": login_mdp
                })
                if result.fetchone()[0] == 0:
                    return None
                return Club(id_club, nom, adresse, mdp)
        except Exception as e:
            print(e)
            return None
