"""
Fichier qui contient les requêtes SQL pour la table ARBITRER
"""

import sys
import os
from sqlalchemy.sql.expression import text
from escrimeur_bd import EscrimeurBD
from competition_bd import CompetitionBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from inscrire import Inscrire


class InscrireBD:
    """
    Classe InscrireBD
    """

    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_inscrire(self):
        """
        Fonction qui retourne tous les inscrire
        :return: liste d'inscrire
        """
        try:
            query = text("SELECT idEscrimeur, idCompetition FROM INSCRIRE")
            result = self.__connexion.execute(query)
            inscrires = []
            for id_escrimeur, id_competition in result:
                escrimeur = EscrimeurBD.get_escrimeur_by_id(self, id_escrimeur)
                competition = CompetitionBD.get_competition_by_id(
                    self, id_competition)
                inscrires.append(Inscrire(escrimeur, competition))
            return inscrires
        except Exception as e:
            print(e)
            return None
