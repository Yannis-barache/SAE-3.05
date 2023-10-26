"""
Module contenant la classe Match
"""

from escrimeur import Escrimeur


class Match:
    """
    Classe Match
    """

    def __init__(self, id_match: int, id_phase: int, escrimeur1: Escrimeur,
                 escrimeur2: Escrimeur, arbitre: Escrimeur, heure: float,
                 finis: bool):
        self.__id = id_match
        self.__id_phase = id_phase
        self.__escrimeur1 = escrimeur1
        self.__escrimeur2 = escrimeur2
        self.__arbitre = arbitre
        self.__heure = heure
        self.__finis = finis
        self.__les_touches: list = []

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

    def get_arbitre(self) -> Escrimeur:
        """
        Fonction qui retourne l'arbitre

        Returns:
            Escrimeur: arbitre
        """
        return self.__arbitre

    def get_heure(self) -> float:
        """
        Fonction qui retourne l'heure du match

        Returns:
            float: heure du match
        """
        return self.__heure

    def est_finis(self) -> bool:
        """
        Fonction qui retourne si le match est finis

        Returns:
            bool: si le match est finis
        """
        return self.__finis

    def est_commencer(self) -> bool:
        """
        Fonction qui retourne si le match est commencer

        Returns:
            bool: si le match est commencer
        """
        return len(self.__les_touches) > 0

    def get_les_touches(self) -> list:
        """
        Fonction qui retourne les touches du match

        Returns:
            list[Touche]: touches du match
        """
        return self.__les_touches

    def get_nb_touche(self, escrimeur: Escrimeur) -> int:
        """
        Fonction qui retourne le nombre de touche du match

        Args:
            escrimeur (Escrimeur): escrimeur

        Returns:
            int: nombre de touche du match
        """
        cpt = 0
        for touche in self.__les_touches:
            if touche.get_escrimeur() == escrimeur:
                cpt += 1
        return cpt

    def get_gagnant(self) -> Escrimeur | None:
        """
        Fonction qui retourne le gagnant du match

        Returns:
            Escrimeur | None: gagnant du match
        """
        if self.est_finis():
            escrimeur1 = 0
            escrimeur2 = 0
            for touche in self.__les_touches:
                if touche.get_escrimeur() == self.__escrimeur1:
                    escrimeur1 += 1
                else:
                    escrimeur2 += 1
            if escrimeur1 > escrimeur2:
                return self.__escrimeur1
            elif escrimeur1 < escrimeur2:
                return self.__escrimeur2
            return None
        else:
            return None

    def ajouter_touche(self, touche) -> None:
        """
        Fonction qui ajoute une touche au match

        Args:
            touche (Touche): touche à ajouter
        """
        self.__les_touches.append(touche)

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

    def set_arbitre(self, arbitre: Escrimeur) -> None:
        """
        Fonction qui modifie l'arbitre

        Args:
            arbitre (Escrimeur): arbitre
        """
        self.__arbitre = arbitre

    def set_heure(self, heure: float) -> None:
        """
        Fonction qui modifie l'heure du match

        Args:
            heure (float): heure du match
        """
        self.__heure = heure

    def set_finis(self, finis: bool) -> None:
        """
        Fonction qui modifie si le match est finis

        Args:
            finis (bool): si le match est finis
        """
        self.__finis = finis

    def __str__(self):
        return (f'{self.__id} - {self.__id_phase} - '
                f'{self.__escrimeur1} - {self.__escrimeur2} - '
                f'{self.__les_touches}')
