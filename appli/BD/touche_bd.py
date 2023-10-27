"""
Fichier qui contient les requêtes SQL pour la table TOUCHE
"""

import sys
import os
from sqlalchemy.sql.expression import text
from match_bd import MatchBD
from escrimeur_bd import EscrimeurBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from touche import Touche


class ToucheBD:
    """
    Classe ToucheBD
    """

    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_touche(self):
        """
        Fonction qui retourne toutes les touches
        :return: liste de touche
        """
        try:
            query = text('SELECT idMatch, idEscrimeur, numTouche FROM TOUCHE')
            result = self.__connexion.execute(query)
            touches = []
            for id_match, id_escrimeur, num in result:
                match = MatchBD(self.__connexion).get_match_by_id(id_match)
                escrimeur = EscrimeurBD(
                    self.__connexion).get_escrimeur_by_id(id_escrimeur)
                touches.append(Touche(match, escrimeur, num))
            return touches
        except Exception as e:
            print(e)
            return None


    def insert_poule(self, touche):
        """
        Fonction qui insert une touche dans la table TOUCHE
        :param touche: La touche à insérer
        """
        try :
            query = text(f"call ajoute_touche({touche.get_match()},{touche.get_escrimeur()})")
            self.__connexion.execute(query)
            self.__connexion.commit()

        except Exception as e:
            print(e)
