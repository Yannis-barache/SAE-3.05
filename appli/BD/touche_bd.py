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
            for (id_match, id_escrimeur, num) in result:
                match.set_id(id_match)
                escrimeur = match.get_escrimeur1(
                ) if id_escrimeur == match.get_escrimeur1().get_id(
                ) else match.get_escrimeur2()
                touches.append(Touche(match, escrimeur, num))
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
            for (id_match, id_escrimeur, num) in result:
                match = MatchBD(self.__connexion).get_match_by_id(id_match)
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

    def insert_touche_2(self, id_match : int, id_escrimeur: int):
        """
        Fonction qui insert une touche dans la table TOUCHE
        :param touche: La touche à insérer
        """
        try:
            query = text(
                f"call ajoute_touche("
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

# if __name__ == '__main__':
#     from modele_appli import ModeleAppli
#     ModeleAppli().get_touche_bd().insert_touche_2(181, 13)