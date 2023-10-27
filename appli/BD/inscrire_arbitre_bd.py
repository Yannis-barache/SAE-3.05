"""
    Fichier qui contient les requêtes SQL pour la table InscrireArbitre
"""

import sys
import os
from sqlalchemy.sql.expression import text
from escrimeur_bd import EscrimeurBD
from competition_bd import CompetitionBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from inscrire_arbitre import InscrireArbitre


class InscrireArbitreBD:
    """
    Classe InscrireArbitreBD
    """

    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_arbitre(self):
        """
        Fonction qui retourne tous les arbitres
        :return: liste d'arbitre
        """
        try:
            query = text("SELECT idEscrimeur, idCompetition FROM ARBITRER")
            result = self.__connexion.execute(query)
            arbitres = []
            for id_escrimeur, id_categorie in result:
                escrimeur = EscrimeurBD(
                    self.__connexion).get_escrimeur_by_id(id_escrimeur)
                competition = CompetitionBD(
                    self.__connexion).get_competition_by_id(id_categorie)
                arbitres.append(InscrireArbitre(escrimeur, competition))
            return arbitres
        except Exception as e:
            print(e)
            return None

    def get_arbitre_by_id(self, id_a: int):
        """
        Fonction qui retourne un arbitre en fonction de son id
        :param id_a: id de l'arbitre
        :return: arbitre
        """
        try:
            query = text("SELECT idEscrimeur, idCompetition "
                         "FROM ARBITRER WHERE idEscrimeur =" + str(id_a))
            result = self.__connexion.execute(query)
            for id_escrimeur, id_competition in result:
                escrimeur = EscrimeurBD(
                    self.__connexion).get_escrimeur_by_id(id_escrimeur)
                competition = CompetitionBD(
                    self.__connexion).get_competition_by_id(id_competition)
                return InscrireArbitre(escrimeur, competition)
            return None
        except Exception as e:
            print(e)
            return None
