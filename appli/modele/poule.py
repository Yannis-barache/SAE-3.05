"""
Module contenant la classe Poule
"""


class Poule:
    """
    Une classe permettant de représenter une poule

    Attributes:
    ___________
        id (int): id de la poule

    Methods:
    ________
        get_id(self): retourne l'id de la poule
        set_id(self, id_poule: int): modifie l'id de la poule
    """

    def __init__(self, id_poule: int):
        """Fonction d'instanciation de la classe Poule

        Args:
            id_poule (int): id de la poule
        """
        self.__id = id_poule

    def get_id(self) -> int:
        """
        Fonction qui retourne l'id de la poule

        Returns:
            int: id de la poule
        """
        return self.__id

    def set_id(self, id_poule) -> None:
        """
        Fonction qui modifie l'id de la poule

        Args:
            id_poule (int): id de la poule
        """
        self.__id = id_poule

    def __str__(self):
        return f'{self.__id}'
