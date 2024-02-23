"""
Fichier qui contient les requêtes SQL pour la table ARBITRER
"""

import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from inscrire import Inscrire
from escrimeur import Escrimeur


class InscrireBD:
    """
    Classe InscrireBD
    """

    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_inscrire(self):
        """
        Fonction qui retourne tous les inscrire
        :return: liste d'inscrire
        """
        try:
            query = text('SELECT idEscrimeur, idCompetition FROM INSCRIRE')
            result = self.__connexion.execute(query)
            inscrires = []
            for (id_escrimeur, id_competition) in result:
                inscrires.append(Inscrire(id_competition, id_escrimeur))
            return inscrires
        except Exception as e:
            print(e)
            return None

    def get_all_inscrit_compet(self, competition):
        """
        Fonction qui retourne tous les inscrits à une compétition

        Args:
            competition (Competition): compétition
        """
        try:
            query = text(
                f'SELECT idEscrimeur FROM INSCRIRE WHERE idCompetition = {competition.get_id()}'
            )
            result = self.__connexion.execute(query)
            inscrires = []
            for (id_escrimeur, ) in result:
                inscrires.append(Inscrire(competition.get_id(), id_escrimeur))
            return inscrires
        except Exception as e:
            print(e)
            return None

    def get_nb_escrimeurs_competition(self, id_compet):
        """
        Fonction qui retourne le nombre d'escrimeurs inscrits à une compétition

        Args:
            id_compet (int): id de la compétition
        """
        try:
            query = text(
                f'SELECT COUNT(idEscrimeur) FROM INSCRIRE WHERE idCompetition = {id_compet}'
            )
            result = self.__connexion.execute(query)
            for (nombre, ) in result:
                return nombre
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

    def delete_inscrire_competition(self, inscrire: Inscrire):
        """
        Fonction qui supprime un inscrire
        :param inscrire: inscrire
        """
        try:
            query = text("DELETE FROM INSCRIRE WHERE idCompetition =" +
                         str(inscrire.get_id_competition()) +
                         " AND idEscrimeur = " +
                         str(inscrire.get_id_escrimeur()))
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None

    def get_all_inscrit_escrimeur(self, escrimeur: Escrimeur):
        """
        Fonction qui retourne tous les inscrits à une compétition

        Args:
            competition (Competition) : compétition
            :param escrimeur:
        """
        try:
            query = text(
                f'SELECT idCompetition FROM INSCRIRE WHERE idEscrimeur = {escrimeur.get_id()}'
            )
            result = self.__connexion.execute(query)
            inscrires = []
            for (id_competition, ) in result:
                inscrires.append(Inscrire(id_competition, escrimeur.get_id()))
            return inscrires
        except Exception as e:
            print(e)
            return None
