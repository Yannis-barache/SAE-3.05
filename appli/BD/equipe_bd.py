"""
Fichier qui contient les requêtes SQL pour la table EQUIPE
"""

import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from equipe import Equipe


class EquipeBD:
    """
        Classe EquipeBD

        Methods:
            __init__(self, connexion)
            get_all_equipe(self)
            get_equipe_by_id(self, id_equipe: int)
            get_equipe_by_id_comp(self, id_comp: int)
            get_nb_equipe(self, id_comp: int)
            insert_equipe(self, id_comp: int, nom_equipe: str)
            delete_equipe(self, id_equipe: int)
            update_equipe(self, id_equipe: int, nom_equipe: str)
    """

    def __init__(self, connexion):
        """
        Constructeur de la classe EquipeBD
        :param connexion: connexion à la base de données
        """
        self.__connexion = connexion

    def get_all_equipe(self):
        """
        Fonction qui retourne toutes les équipes
        :return: liste d'équipe
        """
        try:
            query = text('SELECT idCompetition, idEquipe, nomEquipe FROM EQUIPE')
            result = self.__connexion.execute(query)
            equipes = []
            for id_comp, id_equipe, nom_equipe in result:
                equipes.append(Equipe(id_comp, id_equipe, nom_equipe))
            return equipes
        except Exception as e:
            print(e)
            return None

    def get_equipe_by_id(self, id_equipe: int):
        """
        Fonction qui retourne une équipe en fonction de son id
        :param id_equipe: id de l'équipe
        :return: L'équipe avec l'id correspondant
        """
        try:
            query = text('SELECT idCompetition, idEquipe, nomEquipe FROM EQUIPE '
                         'WHERE idEquipe =' + str(id_equipe))
            result = self.__connexion.execute(query)
            for id_comp, id_equipe_local, nom_equipe in result:
                return Equipe(id_comp, id_equipe_local, nom_equipe)
            return None
        except Exception as e:
            print(e)
            return None

    def get_equipe_by_id_comp(self, id_comp: int):
        """
        Fonction qui retourne une équipe en fonction de son id de competition

        Parameters :
            id_comp(int) id de la competition

        Returns :
            list : liste des équipes dans la competition

        """
        try:
            query = text('SELECT idCompetition, idEquipe, nomEquipe FROM EQUIPE '
                         'WHERE idCompetition =' + str(id_comp))
            result = self.__connexion.execute(query)
            equipes = []
            for id_comp_local, id_equipe, nom_equipe in result:
                equipes.append(Equipe(id_comp_local, id_equipe, nom_equipe))
            return equipes
        except Exception as e:
            print(e)
            return None

    def get_nb_equipe(self, id_comp: int):
        """
        Fonction qui retourne le nombre d'équipes d'une competition

        Parameters :
            id_comp (int) : id de la competition
        Returns :
            int : nombre d'équipes dans la competition
        """

        try:
            query = text('SELECT count(*) FROM EQUIPE WHERE idCompetition =' + str(id_comp))
            result = self.__connexion.execute(query)
            for nb in result:
                return nb[0]
        except Exception as e:
            print(e)
            return None

    def insert_equipe(self, id_comp: int, nom_equipe: str):
        """
        Fonction qui insère une équipe dans la base de données

        Parameters :
            id_comp (int) : id de la competition
            nom_equipe (str) : nom de l'équipe
        """
        try:
            id = self.get_max_id() + 1
            query = text('INSERT INTO EQUIPE (idEquipe,idCompetition, nomEquipe) '
                         'VALUES (:id_equipe, :id_comp, :nom_equipe)')
            self.__connexion.execute(query, {'id_equipe': id, 'id_comp': id_comp, 'nom_equipe': nom_equipe})
            self.__connexion.commit()
        except Exception as e:
            print(e)

    def delete_equipe(self, id_equipe: int):
        """
        Fonction qui supprime une équipe de la base de données

        Parameters :
            id_equipe (int) : id de l'équipe
        """
        try:
            query = text('DELETE FROM EQUIPE WHERE idEquipe = :id_equipe')
            self.__connexion.execute(query, {'id_equipe': id_equipe})
            self.__connexion.commit()
        except Exception as e:
            print(e)

    def get_membres_equipe(self,id_equipe :int) -> list | None:
        """
        Fonction qui retourne les id des tireurs qui font partie d'une équipe
        :param id_equipe: id de l'équipe
        :return: liste d'id de tireurs
        """
        try:
            query = text('SELECT idEscrimeur FROM FAIT_PARTIE WHERE idEquipe =' + str(id_equipe))
            result = self.__connexion.execute(query)
            id_escrimeurs = []
            for id_escrimeur in result:
                id_escrimeurs.append(id_escrimeur[0])
            return id_escrimeurs
        except Exception as e:
            print(e)
            return None

    def update_equipe(self, id_equipe: int, nom_equipe: str):
        """
        Fonction qui met à jour le nom d'une équipe

        Parameters :
            id_equipe (int) : id de l'équipe
            nom_equipe (str) : nom de l'équipe
        """
        try:
            query = text('UPDATE EQUIPE SET nomEquipe = :nom_equipe WHERE idEquipe = :id_equipe')
            self.__connexion.execute(query, {'id_equipe': id_equipe, 'nom_equipe': nom_equipe})
            self.__connexion.commit()
        except Exception as e:
            print(e)

    def get_max_id(self) -> int:
        """
        Fonction qui retourne l'id maximum des équipes
        :return: id maximum
        """
        try:
            query = text('SELECT MAX(idEquipe) FROM EQUIPE')
            result = self.__connexion.execute(query)
            for id_equipe in result:
                return id_equipe[0]
        except Exception as e:
            print(e)
            return None


    def supprimer_composition(self, id_equipe : int):
        try:
            query = text('DELETE FROM FAIT_PARTIE WHERE idEquipe = :id_equipe')
            self.__connexion.execute(query, {'id_equipe': id_equipe})
            self.__connexion.commit()
        except Exception as e:
            print(e)


