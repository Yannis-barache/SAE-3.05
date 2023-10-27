"""
    Fichier qui contient les requêtes SQL pour la table POULE
"""

from sqlalchemy import text
from appli.modele.poule import Poule

class PouleBD:
    """
    Classe PouleBD
    """
    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_poule(self):
        """
        Fonction qui retourne toutes les poules
        :return: liste de poule
        """
        try:
            query = text("SELECT idPoule FROM POULE")
            result = self.__connexion.execute(query)
            poules = []
            for id_poule in result:
                poules.append(Poule(id_poule))
            return poules
        except Exception as e:
            print(e)
            return None

    def insert_poule(self):
        """
        Fonction qui insère une poule
        :param poule: poule
        """
        try:
            query = text("INSERT INTO POULE DEFAULT VALUES")
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None
