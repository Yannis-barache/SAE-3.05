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
from touche_bd import ToucheBD


class PouleBD:
    """
    Classe PouleBD
    """

    def __init__(self, connexion):
        self.__connexion = connexion

    def get_poule_by_id(self, id_poulee: int):
        """
        Fonction qui retourne une poule par son id

        Args:
            id_poule (int): id de la poule
        """
        try:
            query = text("SELECT idPoule FROM POULE WHERE idPoule = " +
                         str(id_poulee))
            result = self.__connexion.execute(query)
            for (id_poule, ) in result:
                query = text("SELECT idMatch FROM MATCHS WHERE idPhase = " +
                             str(id_poule))
                result = self.__connexion.execute(query)
                matches = []
                for (id_match, ) in result:
                    match = MatchBD(self.__connexion).get_match_by_id(id_match)
                    match.set_touche(
                        ToucheBD(self.__connexion).get_by_match(match))
                    matches.append(match)
                la_poule = Poule(id_poule)
                la_poule.set_les_matchs(matches)
                return la_poule
        except Exception as e:
            print(e)
            return None

    def get_all_poule(self):
        """
        Fonction qui retourne toutes les poules
        :return: liste de poule
        """
        try:
            query = text('SELECT idPoule FROM POULE')
            result = self.__connexion.execute(query)
            poules = []
            for (id_poule, ) in result:
                poules.append(Poule(id_poule))
            return poules
        except Exception as e:
            print(e)
            return None

    def insert_poule(self):
        """
        Fonction qui insère une poule
        :param poule: poule
        """
        try:
            query = text("INSERT INTO POULE DEFAULT VALUES")
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
                "SELECT idPoule FROM POULE join PHASE ON idPhase = idPoule WHERE idCompetition = "
                + str(id_compet))
            result = self.__connexion.execute(query)
            poules = []
            for (id_poule, ) in result:
                query = text("SELECT idMatch FROM MATCHS WHERE idPhase = " +
                             str(id_poule))
                result = self.__connexion.execute(query)
                matches = []
                for (id_match, ) in result:
                    match = MatchBD(self.__connexion).get_match_by_id(id_match)
                    match.set_touche(
                        ToucheBD(self.__connexion).get_by_match(match))
                    matches.append(match)
                la_poule = Poule(id_poule)
                la_poule.set_les_matchs(matches)
                poules.append(la_poule)
            return poules
        except Exception as e:
            print(e)
            return None

    def get_poules_by_compet_nb(self, id_compet: int, nb: int):
        """
        Fonction qui retourne la n-ieme pour d'une competition

        Args:
            id_compet (int): id de la compétition
            nb (int): numéro de la poule
        """
        try:
            query = text(
                "SELECT idPoule FROM POULE join PHASE ON idPhase = idPoule WHERE idCompetition = "
                + str(id_compet))
            result = self.__connexion.execute(query)
            cpt = 0
            for (id_poule, ) in result:
                if cpt == nb:
                    query = text(
                        "SELECT idMatch FROM MATCHS WHERE idPhase = " +
                        str(id_poule))
                    result = self.__connexion.execute(query)
                    matches = []
                    for (id_match, ) in result:
                        match = MatchBD(
                            self.__connexion).get_match_by_id(id_match)
                        match.set_touche(
                            ToucheBD(self.__connexion).get_by_match(match))
                        matches.append(match)
                    la_poule = Poule(id_poule)
                    la_poule.set_les_matchs(matches)
                    return la_poule
                cpt += 1
            return None
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
                "SELECT count(idPoule) FROM POULE join PHASE on idPoule = idPhase WHERE idCompetition = "
                + str(id_compet))
            result = self.__connexion.execute(query)
            for (nb, ) in result:
                return int(nb)
        except Exception as e:
            print(e)
            return None
