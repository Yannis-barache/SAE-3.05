"""
Module contenant la classe Match
"""

from escrimeur import Escrimeur


class Match:
    """
    Une classe permettant de représenter un match

    Attributes:
    ___________
        id (int): id du match
        id_phase (int): id de la phase
        escrimeur1 (Escrimeur): premier escrimeur
        escrimeur2 (Escrimeur): deuxième escrimeur

    Methods:
    ________
        les getters et setters de chaque attribut
    """

    def __init__(self, id_match: int, id_phase: int, escrimeur1: Escrimeur,
                 escrimeur2: Escrimeur):
        """Fonction d'instanciation de la classe Match

        Args:
            id_match (int): id du match
            id_phase (int): id de la phase
            escrimeur1 (Escrimeur): premier escrimeur
            escrimeur2 (Escrimeur): deuxième escrimeur
        """
        self.__id = id_match
        self.__id_phase = id_phase
        self.__escrimeur1 = escrimeur1
        self.__escrimeur2 = escrimeur2

    def get_id(self) -> int:
        """
        Fonction qui retourne l'id du match

        Returns:
            int: id du match
        """
        return self.__id

    def get_id_phase(self) -> int:
        """
        Fonction qui retourne l'id de la phase

        Returns:
            int: id de la phase
        """
        return self.__id_phase

    def get_escrimeur1(self) -> Escrimeur:
        """
        Fonction qui retourne le premier escrimeur

        Returns:
            Escrimeur: premier escrimeur
        """
        return self.__escrimeur1

    def get_escrimeur2(self) -> Escrimeur:
        """
        Fonction qui retourne le deuxième escrimeur

        Returns:
            Escrimeur: deuxième escrimeur
        """
        return self.__escrimeur2

    def set_id(self, id_match: int) -> None:
        """
        Fonction qui modifie l'id du match

        Args:
            id_match (int): id du match
        """
        self.__id = id_match

    def set_id_phase(self, id_phase: int) -> None:
        """
        Fonction qui modifie l'id de la phase

        Args:
            id_phase (int): id de la phase
        """
        self.__id_phase = id_phase

    def set_escrimeur1(self, escrimeur1: Escrimeur) -> None:
        """
        Fonction qui modifie le premier escrimeur

        Args:
            escrimeur1 (Escrimeur): premier escrimeur
        """
        self.__escrimeur1 = escrimeur1

    def set_escrimeur2(self, escrimeur2: Escrimeur) -> None:
        """
        Fonction qui modifie le deuxième escrimeur

        Args:
            escrimeur2 (Escrimeur): deuxième escrimeur
        """
        self.__escrimeur2 = escrimeur2

    def __str__(self):
        return f'{self.__id} - {self.__id_phase} - {self.__escrimeur1} - {self.__escrimeur2}'
