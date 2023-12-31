"""
    Fichier qui contient les requêtes SQL pour la table InscrireArbitre
"""

import sys
import os
from sqlalchemy.sql.expression import text

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
            query = text('SELECT idEscrimeur, idCompetition FROM ARBITRER')
            result = self.__connexion.execute(query)
            arbitres = []
            for (id_escrimeur, id_competition) in result:
                arbitres.append(InscrireArbitre(id_escrimeur, id_competition))
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
            query = text('SELECT idEscrimeur, idCompetition '
                         'FROM ARBITRER WHERE idEscrimeur =' + str(id_a))
            result = self.__connexion.execute(query)
            for id_escrimeur, id_competition in result:
                return InscrireArbitre(id_escrimeur, id_competition)
            return None
        except Exception as e:
            print(e)
            return None

    def get_arbitre_by_competition(self, competition):
        """
        Fonction qui retourne tous les arbitres d'une compétition
        :param competition: compétition
        :return: liste d'arbitre
        """
        try:
            query = text(
                f'SELECT idEscrimeur FROM ARBITRER WHERE idCompetition = {competition.get_id()}'
            )
            result = self.__connexion.execute(query)
            arbitres = []
            for (id_escrimeur, ) in result:
                arbitres.append(
                    InscrireArbitre(id_escrimeur, competition.get_id()))
            return arbitres
        except Exception as e:
            print(e)
            return None

    def get_arbitre_by_id_competition(self, id_competition):
        """
        Fonction qui retourne tous les arbitres d'une compétition
        :param id_competition: id de la compétition
        :return: liste d'arbitre
        """
        try:
            query = text(
                f'SELECT idEscrimeur FROM ARBITRER WHERE idCompetition = {id_competition}'
            )
            result = self.__connexion.execute(query)
            arbitres = []
            for (id_escrimeur, ) in result:
                arbitres.append(InscrireArbitre(id_escrimeur, id_competition))
            return arbitres
        except Exception as e:
            print(e)
            return None

    def get_nb_arbitres_competition(self, id_compet):
        """
        Fonction qui retourne le nombre d'arbitres inscrits à une compétition
        :param id_compet: id de la compétition
        :return: nombre d'arbitres
        """
        try:
            query = text(
                f'SELECT COUNT(idEscrimeur) FROM ARBITRER WHERE idCompetition = {id_compet}'
            )
            result = self.__connexion.execute(query)
            for (nombre, ) in result:
                return nombre
        except Exception as e:
            print(e)
            return None

    def insert_arbitre(self, arbitre: InscrireArbitre):
        """
        Fonction qui insère un arbitre
        :param arbitre : arbitre
        """
        try:
            query = text(
                f"INSERT INTO ARBITRER (idEscrimeur, idCompetition) VALUES "
                f"({str(arbitre.get_id_escrimeur())},"
                f"{str(arbitre.get_id_competition())})")
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None

    def delete_arbitre(self, arbitre: InscrireArbitre):
        """
        Fonction qui supprime un arbitre
        :param arbitre : arbitre
        """
        try:
            query = text(
                f"DELETE FROM ARBITRER WHERE idEscrimeur = {str(arbitre.get_id_escrimeur())} "
                f"AND idCompetition = {str(arbitre.get_id_competition())}")

            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None

    def get_all_compet_arbitre(self, id_arbitre):
        """
        Fonction qui retourne toutes les compétitions d'un arbitre
        :param id_arbitre : id de l'arbitre
        :return: liste d'id de compétition
        """
        try:
            query = text(
                f"SELECT idCompetition FROM ARBITRER WHERE idEscrimeur = {str(id_arbitre)}"
            )
            result = self.__connexion.execute(query)
            competitions = []
            for (id_competition, ) in result:
                competitions.append(id_competition)
            return competitions
        except Exception as e:
            print(e)
            return None
