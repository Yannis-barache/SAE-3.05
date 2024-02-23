"""
Fichier qui contient les requêtes SQL pour la table EQUIPE
"""

import sys
import os
from sqlalchemy.sql.expression import text


from escrimeur_bd import EscrimeurBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from equipe import Equipe
from escrimeur import Escrimeur


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

    def __init__(self, connexion):
        self.__connexion = connexion

    def get_equipe_by_id(self, id_equipe) -> Equipe | None:
        """
        Fonction qui retourne une équipe par son id
        :param id_equipe: id de l'équipe
        :return: équipe
        """
        try:
            query = text(
                f'SELECT idEquipe, nomEquipe, idCompetition FROM EQUIPE WHERE idEquipe = {id_equipe}'
            )
            result = self.__connexion.execute(query)
            for (
                    id_equipee,
                    nom_equipe,
                    id_competition,
            ) in result:
                equipe = Equipe(id_competition, id_equipee, nom_equipe)
                equipe.set_les_escrimeurs(
                    self.get_escrimeur_by_equipe(id_equipee))
                return equipe
            return None
        except Exception as e:
            print(e)
            return None
          
    def get_escrimeur_by_equipe(self, id_equipe) -> list[Escrimeur] | None:
        """
        Fonction qui retourne tous les escrimeurs d'une équipe
        :param id_equipe: id de l'équipe
        :return: liste d'escrimeurs
        """
        try:
            query = text(
                f'SELECT idEscrimeur FROM FAIT_PARTIE WHERE idEquipe = {id_equipe}'
            )
            result = self.__connexion.execute(query)
            escrimeurs = []
            escrimeur_db = EscrimeurBD(self.__connexion)
            for (id_escrimeur, ) in result:
                escrimeurs.append(
                    escrimeur_db.get_escrimeur_by_id(id_escrimeur))
            return escrimeurs
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

    def get_all_equipe_by_competition(self,
                                      id_competition) -> list[Equipe] | None:
        """
        Fonction qui retourne toutes les équipes d'une compétition
        :param id_competition: id de la compétition
        :return: liste d'équipes
        """
        try:
            query = text(
                f'SELECT idEquipe, nomEquipe, idCompetition FROM EQUIPE WHERE idCompetition = {id_competition}'
            )
            result = self.__connexion.execute(query)
            equipes = []
            for (
                    id_equipe,
                    nom_equipe,
                    id_competitio,
            ) in result:
                equipes.append(Equipe(id_competitio, id_equipe, nom_equipe))
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
            id_max = self.get_max_id() + 1
            query = text('INSERT INTO EQUIPE (idEquipe,idCompetition, nomEquipe) '
                         'VALUES (:id_equipe, :id_comp, :nom_equipe)')
            self.__connexion.execute(query, {'id_equipe': id_max, 'id_comp': id_comp, 'nom_equipe': nom_equipe})
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

    def get_membres_equipe(self, id_equipe: int) -> list | None:
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

    def update_equipe(self, id_equipe: int, nom_equipe: str) -> None:
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
            return None

    def get_max_id(self) -> int:
        """
        Fonction qui retourne l'id maximum des équipes
        :return: id maximum
        """
        try:
            query = text('SELECT MAX(idEquipe) FROM EQUIPE')
            result = self.__connexion.execute(query)
            return result.fetchone()[0]
        except Exception as e:
            print(e)
            return 0

    def supprimer_composition(self, id_equipe: int) -> bool:
        """
        Fonction qui supprime la composition d'une équipe

        Parameters :
            id_equipe (int) : id de l'équipe
        Returns :
            bool : True si la suppression a réussi, False sinon

        """
        try:
            query = text('DELETE FROM FAIT_PARTIE WHERE idEquipe = :id_equipe')
            self.__connexion.execute(query, {'id_equipe': id_equipe})
            self.__connexion.commit()
            return True
        except Exception as e:
            print(e)
            return False
