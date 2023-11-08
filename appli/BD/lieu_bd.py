"""
    Fichier qui contient les requêtes SQL pour la table Lieu
"""

import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from lieu import Lieu


class LieuBD:
    """
    Classe LieuBD
    """

    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_lieu(self):
        """
        Fonction qui retourne tous les lieux
        :return: liste de Lieu
        """
        try:
            query = text(
                'SELECT idLieu, adresseLieu, descriptionLieu FROM LIEU')
            result = self.__connexion.execute(query)
            lieux = []
            for id_lieu, adresse, description in result:
                lieux.append(Lieu(id_lieu, description, adresse))
            return lieux
        except Exception as e:
            print(e)
            return None

    def get_lieu_by_id(self, id_l: int):
        """
        Fonction qui retourne un lieu en fonction de son id
        :param id_l: id du lieu
        :return: lieu
        """
        try:
            query = text('SELECT idLieu, adresseLieu, '
                         'descriptionLieu FROM LIEU WHERE idLieu =' +
                         str(id_l))
            result = self.__connexion.execute(query)
            for id_lieu, adresse, description in result:
                return Lieu(id_lieu, description, adresse)
            return None
        except Exception as e:
            print(e)
            return None

    def insert_lieu(self, lieu: Lieu):
        """
        Fonction qui insère un lieu
        :param lieu : lieu
        """
        try:
            query = text(
                f"INSERT INTO LIEU (adresseLieu, descriptionLieu) VALUES "
                f"('{lieu.get_adresse()}','{lieu.get_description()}')")
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None
