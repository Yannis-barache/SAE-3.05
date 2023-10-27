"""
    Fichier qui contient les requêtes SQL pour la table POULE
"""

import sys
import os
from sqlalchemy import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from poule import Poule


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
