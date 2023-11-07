"""
    Fichier qui contient les requêtes SQL pour la table PHASE_FINALE
"""

import sys
import os
from sqlalchemy import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from phase_final import PhaseFinal


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
