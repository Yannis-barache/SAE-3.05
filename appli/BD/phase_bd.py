"""
Fichier qui contient les requêtes SQL pour la table PHASE
"""

import sys
import os
from sqlalchemy.sql.expression import text
from competition_bd import CompetitionBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from phase import Phase


class PhaseBD:
    """
    Classe PhaseBD
    """

    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_phase(self):
        """
        Fonction qui retourne toutes les phases
        :return: liste de phase
        """
        try:
            query = text("SELECT idPhase, idCompetition FROM PHASE")
            result = self.__connexion.execute(query)
            phases = []
            for id_phase, id_competition in result:
                competition = CompetitionBD(
                    self.__connexion).get_competition_by_id(id_competition)
                phases.append(Phase(id_phase, competition))
            return phases
        except Exception as e:
            print(e)
            return None

    def get_phase_by_id(self, id_p: int):
        """
        Fonction qui retourne une phase en fonction de son id
        :param id_p: id de la phase
        :return: phase
        """
        try:
            query = text(
                "SELECT idPhase, idCompetition FROM PHASE WHERE idPhase =" +
                str(id_p))
            result = self.__connexion.execute(query)
            for id_phase, id_competition in result:
                competition = CompetitionBD(
                    self.__connexion).get_competition_by_id(id_competition)
                return Phase(id_phase, competition)
            return None
        except Exception as e:
            print(e)
            return None
