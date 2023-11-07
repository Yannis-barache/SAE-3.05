"""
Fichier qui contient les requêtes SQL pour la table ARBITRER
"""

import sys
import os
from sqlalchemy.sql.expression import text
from escrimeur_bd import EscrimeurBD
from competition_bd import CompetitionBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from inscrire import Inscrire


class InscrireBD:
    """
    Classe InscrireBD
    """

    def __init__(self, connexion):
        self.__connexion = connexion
        self.__competition_bd = CompetitionBD(connexion)
        self.__escrimeur_bd = EscrimeurBD(connexion)

    def get_all_inscrire(self):
        """
        Fonction qui retourne tous les inscrire
        :return: liste d'inscrire
        """
        try:
            query = text('SELECT idEscrimeur, idCompetition FROM INSCRIRE')
            result = self.__connexion.execute(query)
            inscrires = []
            for id_escrimeur, id_competition in result:
                escrimeur = self.__escrimeur_bd.get_escrimeur_by_id(
                    id_escrimeur)
                competition = self.__competition_bd.get_competition_by_id(
                    id_competition)
                inscrires.append(Inscrire(escrimeur, competition))
            return inscrires
        except Exception as e:
            print(e)
            return None

    def insert_inscrire(self, inscrire: Inscrire):
        """
        Fonction qui insère un inscrire
        :param inscrire : inscrire
        """
        try:
            query = text(
                f"INSERT INTO INSCRIRE (idEscrimeur, idCompetition) VALUES "
                f"({str(inscrire.get_id_escrimeur())},"
                f"{str(inscrire.get_id_competition())})")
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None

    def delete_inscrire(self, inscrire: Inscrire):
        """
        Fonction qui supprime un inscrire
        :param inscrire: inscrire
        """
        try:
            query = text("DELETE FROM INSCRIRE WHERE idEscrimeur =" +
                         str(inscrire.get_id_escrimeur()))
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None
