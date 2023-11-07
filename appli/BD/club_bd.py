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
            query = text(f"INSERT INTO CLUB (nomClub, adresse, mdpClub) VALUES "
                         f"('{club.get_nom()}','"
                         f"{club.get_adresse()}','{club.get_mdp()}')")
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None

