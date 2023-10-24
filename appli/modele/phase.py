"""
Module contenant la classe Phase
"""


class Phase:
    """
    Une classe permettant de représenter une phase

    Attributes:
    ___________
        id_phase (int): id de la phase
        id_comp (int): id de la compétition

    Methods:
    ________
        get_id_phase(self): retourne l'id de la phase
        get_id_comp(self): retourne l'id de la compétition
        set_id_phase(self, id_phase: int): modifie l'id de la phase
        set_id_comp(self, id_comp: int): modifie l'id de la compétition
    """

    def __init__(self, id_phase: int, id_comp: int):
        """Fonction d'instanciation de la classe Phase

        Args:
            id_phase (int): id de la phase
            id_comp (int): id de la compétition
        """
        self.__id_phase = id_phase
        self.__id_comp = id_comp

    def get_id_phase(self) -> int:
        """
        Fonction qui retourne l'id de la phase

        Returns:
            int: id de la phase
        """
        return self.__id_phase

    def get_id_comp(self) -> int:
        """
        Fonction qui retourne l'id de la compétition

        Returns:
            int: id de la compétition
        """
        return self.__id_comp

    def set_id_phase(self, id_phase: int) -> None:
        """
        Fonction qui modifie l'id de la phase

        Args:
            id_phase (int): id de la phase
        """
        self.__id_phase = id_phase

    def set_id_comp(self, id_comp: int) -> None:
        """
        Fonction qui modifie l'id de la compétition

        Args:
            id_comp (int): id de la compétition
        """
        self.__id_comp = id_comp

    def __str__(self):
        return f'{self.__id_phase} - {self.__id_comp}'
