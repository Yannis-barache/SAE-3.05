"""
Module contenant la classe Phase
"""


class Phase:
    """
    Classe Phase
    """

    def __init__(self, id_phase: int, id_comp: int):
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
