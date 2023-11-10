"""
    Fichier qui contient les requêtes SQL pour la table POULE
"""

import sys
import os
from sqlalchemy import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from poule import Poule

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/BD'))

from match_bd import MatchBD

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
            query = text('SELECT idPoule FROM POULE')
            result = self.__connexion.execute(query)
            poules = []
            for (id_poule,) in result:
                poules.append(Poule(id_poule))
            return poules
        except Exception as e:
            print(e)
            return None

    def insert_poule(self, une_poule: Poule):
        """
        Fonction qui insère une poule
        :param poule: poule
        """
        try:
            query = text("INSERT INTO POULE (idPoule) VALUES (" +
                         str(une_poule.get_id()) + ")")
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None

    def delete_poule(self, une_poule: Poule):
        """
        Fonction qui supprime une poule
        :param poule: poule
        """
        try:
            query = text("DELETE FROM POULE WHERE idPoule = " +
                         str(une_poule.get_id()))
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None

    def get_poules_by_compet(self, id_compet: int):
        """
        Fonction qui retourne toutes les poules d'une compétition

        Args:
            id_compet (int): id de la compétition
        """
        try:
            query = text(
                "SELECT idPoule FROM POULE join PHASE ON idPhase = IdPoule WHERE idCompetition = " +
                str(id_compet))
            result = self.__connexion.execute(query)
            poules = []
            for (id_poule,) in result:
                query = text(
                    "SELECT idMatch FROM MATCHS WHERE idPhase = " +
                    str(id_poule))
                result = self.__connexion.execute(query)
                matches = []
                for (id_match,) in result:
                    matches.append(MatchBD(self.__connexion).get_match_by_id(id_match))
                la_poule = Poule(id_poule)
                la_poule.set_les_matchs(matches)
                poules.append(Poule(id_poule))
            return poules
        except Exception as e:
            print(e)
            return None

    def nb_poule_compet(self, id_compet: int):
        """
        Fonction qui retourne le nombre de poules d'une compétition

        Args:
            id_compet (int): id de la compétition
        """
        try:
            query = text(
                "SELECT idPoule FROM POULE join PHASE on idPoule = idPhase WHERE idCompetition = " +
                str(id_compet))
            result = self.__connexion.execute(query)
            cpt = 0
            for _ in result:
                cpt += 1
            return cpt
        except Exception as e:
            print(e)
            return None

if __name__ == "__main__":
    from modele_appli import ModeleAppli
    modele = ModeleAppli()
    poule = modele.get_poule_bd()
    print(poule.get_poules_by_compet(2)[0].get_les_matchs())