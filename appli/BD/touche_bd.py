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
from match import Match


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
            for (
                    id_match,
                    id_escrimeur,
                    num,
            ) in result:
                match = MatchBD(self.__connexion).get_match_by_id(id_match)
                escrimeur = EscrimeurBD(
                    self.__connexion).get_escrimeur_by_id(id_escrimeur)
                touches.append(Touche(match, escrimeur, num))
            return touches
        except Exception as e:
            print(e)
            return None

    def get_by_match(self, match: Match):
        """
        Fonction qui retourne toutes les touches d'un match

        Args:
            match_id (int): l'id du match
        """
        try:
            query = text(
                f"SELECT idMatch, idEscrimeur, numTouche FROM TOUCHE WHERE idMatch = {match.get_id()}"
            )
            result = self.__connexion.execute(query)
            touches = []
            #pylint: disable=W0612
            for (id_match, id_escrimeur, num) in result:
                escrimeur = EscrimeurBD(
                    self.__connexion).get_escrimeur_by_id(id_escrimeur)
                touches.append(Touche(match, escrimeur, int(num)))
            return touches
        except Exception as e:
            print(e)
            return None

    def get_touches_by_id_match(self, id_match: int):
        """
        Fonction qui retourne toutes les touches d'un match

        Args:
            match_id (int): l'id du match
        """
        try:
            query = text(
                f"SELECT idMatch, idEscrimeur, numTouche FROM TOUCHE WHERE idMatch = {id_match}"
            )
            result = self.__connexion.execute(query)
            touches = []
            for (id_match_bd, id_escrimeur, num) in result:
                match = MatchBD(self.__connexion).get_match_by_id(id_match_bd)
                escrimeur = EscrimeurBD(
                    self.__connexion).get_escrimeur_by_id(id_escrimeur)
                touches.append(Touche(match, escrimeur, num))
            return touches
        except Exception as e:
            print(e)
            return None

    def insert_touche(self, touche: Touche):
        """
        Fonction qui insert une touche dans la table TOUCHE
        :param touche: La touche à insérer
        """
        try:
            query = text(
                f"call ajoute_touche("
                f"{touche.get_match().get_id()}, {touche.get_escrimeur().get_id()}"
                ")")
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)

    def insert_touche_2(self, id_match: int, id_escrimeur: int):
        """
        Fonction qui insert une touche dans la table TOUCHE
        :param touche: La touche à insérer
        """
        try:
            query = text(f"call ajoute_touche("
                         f"{id_match}, {id_escrimeur}"
                         ")")
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)

    def delete_touche(self, touche: Touche, num_touche: int):
        """
        Fonction qui supprime une touche dans la table TOUCHE
        :param touche: La touche à supprimer
        :param num_touche: Le numéro de la touche à supprimer
        """
        try:
            query = text(
                f"DELETE FROM TOUCHE WHERE idMatch = {touche.get_match().get_id()} "
                f"AND idEscrimeur = {touche.get_escrimeur().get_id()} "
                f"AND numTouche = {num_touche}")
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)

    def delete_last_touche(self, id_match: int):
        """
        Fonction qui supprime la dernière touche d'un match
        :param id_match: L'id du match
        """
        try:
            query = text(
                f"DELETE FROM TOUCHE WHERE idMatch = {id_match} AND numTouche = (SELECT MAX(numTouche) FROM TOUCHE WHERE idMatch = {id_match})"
            )
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)

    def get_max_num_touche(self, id_match: int):
        """Function that returns the number of the next touch to insert into the database for a given match.

        Args:
            id_match (int): Match ID
        """
        try:
            query = text(f"SELECT COALESCE(MAX(numTouche), 0) AS maxTouche\
                FROM TOUCHE WHERE idMatch = {id_match};")
            result = self.__connexion.execute(query).fetchone()
            if result is not None:
                for element in result:
                    return int(element)
            else:
                return 0
        except Exception as e:
            print(e)
            # Handle the exception appropriately, e.g., log the error or raise it.

    def get_touche_by_id(self, id_match: int, num_touche: int):
        """Fonction qui retourne une touche en fonction de son placement dans le match.

        Args:
            id_match (int): id du match
            num_touche (int): numéro de la touche
        """
        try:
            query = text(
                f"SELECT idMatch, idEscrimeur, numTouche FROM TOUCHE WHERE idMatch = {id_match} AND numTouche = {num_touche}"
            )
            result = self.__connexion.execute(query).fetchone()
            if result is not None:
                match = MatchBD(self.__connexion).get_match_by_id(result[0])
                escrimeur = EscrimeurBD(self.__connexion).get_escrimeur_by_id(
                    result[1])
                return Touche(match, escrimeur, int(result[2]))
            else:
                return None
        except Exception as e:
            print(e)
            return None

    def get_nb_touche_by_phase_and_escrimeur(self, id_phase: int,
                                             id_escrimeur: int) -> int | None:
        """Fonction qui retourne le nombre de touche d'un escrimeur dans une phase.

        Args:
            id_phase (int): id de la Phase
            id_escrimeur (int): id de l'escrimeur
        """
        try:
            query = text(
                f"SELECT COUNT(*) FROM TOUCHE NATURAL JOIN MATCHS NATURAL JOIN PHASE WHERE idPhase = {id_phase} AND idEscrimeur = {id_escrimeur}"
            )
            result = self.__connexion.execute(query).fetchone()
            if result is not None:
                return int(result[0])
            else:
                return None
        except Exception as e:
            print(e)
            return None
