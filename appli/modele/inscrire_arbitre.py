"""
Module contenant la classe InscrireArbitre
"""


class InscrireArbitre:
    """
    Classe Arbitrer
    """

    def __init__(self, id_escrimeur: int, id_competition: int):
        self.__id_escrimeur = id_escrimeur
        self.__id_competition = id_competition

    def get_id_escrimeur(self):
        """
        Fonction qui retourne l'id de l'escrimeur

        Returns:
            int: id de l'escrimeur
        """
        return self.__id_escrimeur

    def get_id_competition(self):
        """
        Fonction qui retourne l'id de la compétition

        Returns:
            int: id de la compétition
        """
        return self.__id_competition

    def set_id_escrimeur(self, id_escrimeur: int):
        """
        Fonction qui modifie l'id de l'escrimeur

        Args:
            id_escrimeur (int): id de l'escrimeur
        """
        self.__id_escrimeur = id_escrimeur

    def set_id_competition(self, id_competition: int):
        """
        Fonction qui modifie l'id de la compétition

        Args:
            id_competition (int): id de la compétition
        """
        self.__id_competition = id_competition

    def __str__(self):
        return f'Arbitre : {self.__id_escrimeur} - {self.__id_competition} |'
