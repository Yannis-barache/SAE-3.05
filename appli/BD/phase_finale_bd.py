"""
    Fichier qui contient les requêtes SQL pour la table PHASE_FINALE
"""

import sys
import os
from sqlalchemy import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from phase_final import PhaseFinal

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/BD'))

from match_bd import MatchBD
from touche_bd import ToucheBD


class PhaseFinaleBD:
    """
    Classe PhaseFinaleBD
    """

    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_phase_final(self):
        """
        Fonction qui retourne toutes les phases finales
        :return: liste de phase finale
        """
        try:
            query = text('SELECT idPhaseFinale FROM PHASE_FINALE')
            result = self.__connexion.execute(query)
            phase_finals = []
            for id_phase_finale in result:
                phase_finals.append(PhaseFinal(id_phase_finale))
            return phase_finals
        except Exception as e:
            print(e)
            return None

    def insert_phase_finale(self, phase_finale: PhaseFinal):
        """
        Fonction qui insère une phase finale
        """
        try:
            if phase_finale.get_id_phase_f(
            ) is None or phase_finale.get_id_phase_f() == -1:
                return None
            query = text("INSERT INTO PHASE_FINALE (idPhaseFinale) VALUES (" +
                         str(phase_finale.get_id_phase_f()) + ")")
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None

    def delete_phase_finale(self, phase_finale: PhaseFinal):
        """
        Fonction qui supprime une phase finale
        """
        try:
            if phase_finale.get_id_phase_f(
            ) is None or phase_finale.get_id_phase_f() == -1:
                return None
            query = text("DELETE FROM PHASE_FINALE WHERE idPhaseFinale = " +
                         str(phase_finale.get_id_phase_f()))
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None

    def get_phase_finale_by_compet(self, id_compet: int):
        """
        Fonction qui retourne la phase finale d'une compétition
        :param id_compet: id de la compétition
        :return: phase finale
        """
        try:
            query = text(
                "SELECT idPhaseFinale FROM PHASE_FINALE join PHASE ON idPhase = idPhaseFinale WHERE idCompetition = "
                + str(id_compet))
            result = self.__connexion.execute(query)
            for (id_phase_finale, ) in result:
                phase_final = PhaseFinal(id_phase_finale)
            query = text(
                "SELECT idMatch FROM MATCHS where idPhase = " + str(phase_final.get_id_phase_f()))
            result = self.__connexion.execute(query)
            matches = []
            for (id_match, ) in result:
                match = MatchBD(self.__connexion).get_match_by_id(id_match)
                match.set_touche(ToucheBD(self.__connexion).get_by_match(match))
                matches.append(match)
            phase_final.set_match(matches)
            #TODO : ajouter les pistes

            return phase_final
        except Exception as e:
            print(e)
            return None
