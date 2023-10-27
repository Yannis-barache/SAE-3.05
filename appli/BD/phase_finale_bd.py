"""
    Fichier qui contient les requêtes SQL pour la table PHASE_FINALE
"""

from sqlalchemy import text
from appli.modele.phase_final import PhaseFinal

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
            query = text("SELECT idPhaseFinale FROM PHASE_FINALE")
            result = self.__connexion.execute(query)
            phase_finals = []
            for id_phase_finale in result:
                phase_finals.append(PhaseFinal(id_phase_finale))
            return phase_finals
        except Exception as e:
            print(e)
            return None

    def insert_phase_finale(self):
        """
        Fonction qui insère une phase finale
        """
        try:
            query = text("INSERT INTO PHASE_FINALE DEFAULT VALUES")
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None
