"""
Module contenant la classe Arbitrer
"""


class Arbitrer:
    """
    Classe Arbitrer permettant de lier un arbitre à une compétition

    Attribute:
    _________
        id_arbitre : int
            id de l'arbitre
        id_competition : int
            id de la compétition

    Methodes:
    _________

        get_id_arbitre(self):
            Retourne l'id de l'arbitre

        get_id_competition(self):
            Retourne l'id de la compétition

        set_id_arbitre(self, id_arbitre: int):
            Modifie l'id de l'arbitre

        set_id_competition(self, id_competition: int):
            Modifie l'id de la compétition

        __str__(self):
            Affiche l'objet Arbitrer
    """

    def __init__(self, id_arbitre: int, id_competition: int):
        """
        Fonction d'instanciation de la classe Arbitrer

        Args:
        ______
            id_arbitre : int
                id de l'arbitre
            id_competition : int
                id de la compétition
        """
        self.__id_arbitre = id_arbitre
        self.__id_competition = id_competition

    def get_id_arbitre(self):
        """
        Fonction qui retourne l'id de l'arbitre

        Returns:
            int: id de l'arbitre
        """
        return self.__id_arbitre

    def get_id_competition(self):
        """
        Fonction qui retourne l'id de la compétition

        Returns:
            int: id de la compétition
        """
        return self.__id_competition

    def set_id_arbitre(self, id_arbitre: int):
        """
        Fonction qui modifie l'id de l'arbitre

        Args:
            id_arbitre (int): id de l'arbitre
        """
        self.__id_arbitre = id_arbitre

    def set_id_competition(self, id_competition: int):
        """
        Fonction qui modifie l'id de la compétition

        Args:
            id_competition (int): id de la compétition
        """
        self.__id_competition = id_competition

    def __str__(self):
        return f'{self.__id_arbitre} - {self.__id_competition}'
