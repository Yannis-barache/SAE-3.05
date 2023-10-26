"""
Module contenant la classe Poule
"""


class Poule:
    """
    Classe Poule
    """

    def __init__(self, id_poule):
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
        return f'Poule : {self.__id} |'
