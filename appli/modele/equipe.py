"""
Module contenant la classe Equipe
"""
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))


class Equipe:
    """
    Classe Equipe
    """

    def __init__(self, id_comp: int, id_equipe: int, nom_equipe: str):
        self.__id_comp = id_comp
        self.__id = id_equipe
        self.__nom_equipe = nom_equipe

    def get_id_comp(self) -> int:
        """
        Fonction qui retourne l'id de la competition

        Returns :
            int : id de la competition
        """
        return self.__id_comp

    def get_id(self) -> int:
        """
        Fonction qui retourne l'id de l'Equipe

        Returns :
            int : id de l'Equipe
        """
        return self.__id

    def get_nom_equipe(self) -> str:
        """
        Fonction qui retourne le nom de l'Equipe

        Returns :
            str : nom de l'Equipe
        """
        return self.__nom_equipe

    def set_id_comp(self, id_comp: int):
        """
        Fonction qui modifie l'id de la competition

        Parameters :
            id_comp : int : id de la competition
        """
        self.__id_comp = id_comp

    def set_nom_equipe(self, nom_equipe: str):
        """
        Fonction qui modifie le nom de l'Equipe

        Parameters :
            nomEquipe : str : nom de l'Equipe
        """
        self.__nom_equipe = nom_equipe

    def __str__(self) -> str:
        return f"Equipe : {self.__nom_equipe}"
