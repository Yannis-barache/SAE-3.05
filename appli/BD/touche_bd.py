"""
Fichier qui contient les requêtes SQL pour la table TOUCHE
"""

from sqlalchemy.sql.expression import text
from appli.modele.touche import Touche
from appli.BD.match_bd import MatchBD
from appli.BD.escrimeur_bd import EscrimeurBD

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
            query = text("SELECT idMatch, idEscrimeur, numTouche FROM TOUCHE")
            result = self.__connexion.execute(query)
            touches = []
            for id_match, id_escrimeur, num in result:
                match = MatchBD(self.__connexion).get_match_by_id(id_match)
                escrimeur = EscrimeurBD(self.__connexion).get_escrimeur_by_id(id_escrimeur)
                touches.append(Touche(match, escrimeur, num))
            return touches
        except Exception as e:
            print(e)
            return None
