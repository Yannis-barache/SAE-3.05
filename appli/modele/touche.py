"""
Module contenant la classe Touche
"""

from match import Match
from escrimeur import Escrimeur


class Touche:
    """
    Une classe permettant de représenter une touche

    Attributes:
    ___________
        match (Match): Le match
        escrimeur (Escrimeur): L'escrimeur
        numero (int): Le numero de la touche

    Methods:
    ________
        les getters et setters de chaque attribut
    """

    def __init__(self, match: Match, escrimeur: Escrimeur, numero: int):
        """Fonction d'instanciation de la classe Touche

        Args:
            match (Match): un match
            escrimeur (Escrimeur): un escrimeur
            numero (int): le nombre de touche de l'escrimeur
        """
        self.__match = match
        self.__escrimeur = escrimeur
        self.__numero = numero

    def get_match(self) -> Match:
        """
        Fonction qui retourne le match

        Returns:
            Match: Le match
        """
        return self.__match

    def get_escrimeur(self) -> Escrimeur:
        """
        Fonction qui retourne l'escrimeur

        Returns:
            Escrimeur: L'escrimeur
        """
        return self.__escrimeur

    def get_numero(self) -> int:
        """
        Fonction qui retourne le numero de la touche

        Returns:
            int: Le numero de la touche
        """
        return self.__numero

    def set_match(self, match: Match) -> None:
        """
        Fonction qui modifie le match

        Args:
            match (Match): Le match
        """
        self.__match = match

    def set_escrimeur(self, escrimeur: Escrimeur) -> None:
        """
        Fonction qui modifie l'escrimeur

        Args:
            escrimeur (Escrimeur): L'escrimeur
        """
        self.__escrimeur = escrimeur

    def set_numero(self, numero: int) -> None:
        """
        Fonction qui modifie le numero de la touche

        Args:
            numero (int): Le numero de la touche
        """
        self.__numero = numero

    def __str__(self) -> str:
        """
        Fonction qui retourne une chaine de caractere contenant les informations de la touche

        Returns:
            str: Les informations de la touche
        """
        return f"{self.__match} - {self.__escrimeur} - {self.__numero}"
