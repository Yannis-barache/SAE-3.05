"""
Fichier qui contient les requêtes SQL pour la table PHASE
"""

import sys
import os
from sqlalchemy.sql.expression import text

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
            query = text('SELECT idPhase, idCompetition FROM PHASE')
            result = self.__connexion.execute(query)
            phases = []
            for (
                    id_phase,
                    id_competition,
            ) in result:
                phases.append(Phase(id_phase, id_competition))
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
                'SELECT idPhase, idCompetition FROM PHASE WHERE idPhase =' +
                str(id_p))
            result = self.__connexion.execute(query)
            for (
                    id_phase,
                    id_competition,
            ) in result:
                return Phase(id_phase, id_competition)
            return None
        except Exception as e:
            print(e)
            return None

    def insert_phase(self, phase: Phase):
        """
        Fonction qui insère une phase
        :param phase : phase
        return : id de la phase
        """
        try:
            query = text(f"INSERT INTO PHASE (idCompetition) "
                         f"VALUES ({phase.get_id_comp()})")
            self.__connexion.execute(query)
            self.__connexion.commit()
            query = text("SELECT LAST_INSERT_ID()")
            result = self.__connexion.execute(query)
            for (id_phase, ) in result:
                return id_phase
        except Exception as e:
            print(e)
            return None

    def insert_phase_by_id(self, phase: Phase):
        """
        Fonction qui insère une phase en fonction de son id
        :param phase : phase
        """
        try:
            query = text(
                f"INSERT INTO PHASE (idPhase, idCompetition) "
                f"VALUES ({phase.get_id_phase()}, {phase.get_id_comp()})")
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None

    def delete_phase_by_id(self, id_p: int):
        """
        Fonction qui supprime une phase en fonction de son id
        :param id_p: id de la phase
        """
        try:
            query = text(f"DELETE FROM PHASE WHERE idPhase = {id_p}")
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None
