"""
Module contenant la classe PhaseFinal
"""

from match import Match
from escrimeur import Escrimeur
from piste import Piste
import random


class PhaseFinal:
    """
    La classe PhaseFinal
    """

    def __init__(self, id_phase_f: int):
        self.__id_phase_f = id_phase_f
        self.__les_matchs: list[Match] = []
        self.__les_pistes: list[Piste] = []
        self.__index_piste = 0
        self.__heure = 0

    def get_id_phase_f(self) -> int:
        """
        Fonction qui retourne l'id de la phase finale

        Returns:
            int: id de la phase finale
        """
        return self.__id_phase_f

    def get_les_matchs(self) -> list[Match]:
        """
        Fonction qui retourne la liste des matchs

        Returns:
            list: liste des matchs
        """
        return self.__les_matchs

    def get_les_pistes(self) -> list[Piste]:
        """
        Fonction qui retourne la liste des pistes

        Returns:
            list: liste des pistes
        """
        return self.__les_pistes

    def set_id_phase_f(self, id_phase_f: int) -> None:
        """
        Fonction qui modifie l'id de la phase finale

        Args:
            id_phase_f (int): id de la phase finale
        """
        self.__id_phase_f = id_phase_f

    def set_match(self, match: Match) -> None:
        """
        Fonction qui ajoute un match à la liste des matchs

        Args:
            match (Match): match
        """
        self.__les_matchs.append(match)

    def set_les_pistes(self, liste_pistes: list[Piste]) -> None:
        """
        Fonction qui ajoute une piste à la liste des pistes

        Args:
            piste (Piste): piste
        """
        self.__les_pistes.append(liste_pistes)

    def generer_les_matchs(self, liste_escrimeurs: list[Escrimeur],
                           liste_arbitres: list[Escrimeur],
                           heure_debut: float) -> list[Match]:
        """
        Fonction qui génère les matchs de la phase finale

        Args:
            liste_escrimeurs (list): liste des escrimeurs
            liste_arbitres (list): liste des arbitres
            heure_debut (float): heure de début

        Returns:
            list: liste des matchs
        """
        self.__heure = heure_debut
        cpt = 0
        liste_matchs = []
        while cpt < len(liste_escrimeurs) / 2:
            escrimeur1 = liste_escrimeurs[cpt]
            escrimeur2 = liste_escrimeurs[-(cpt + 1)]
            arbitre = random.choice(liste_arbitres)
            liste_matchs.append(Match(-1, self.__id_phase_f, escrimeur1, escrimeur2, arbitre, heure_debut, False, self.__les_pistes[self.__index_piste]))
            self.__index_piste += 1
            if self.__index_piste == len(self.__les_pistes):
                self.__index_piste = 0
                self.__heure += 0.25
                if self.__heure % 1 >= 0.6:
                    self.__heure += 0.4
            cpt += 1
        self.__les_matchs = liste_matchs
        return liste_matchs

    def est_finis(self) -> bool:
        """
        Fonction qui vérifie si la phase finale est finis

        Returns:
            bool: True si la phase finale est finis, False sinon
        """
        if len(self.__les_matchs) == 0:
            return False
        for match in self.__les_matchs:
            if not match.est_finis():
                return False
        return True

    def clear_matchs(self) -> None:
        """
        Fonction qui vide la liste des matchs
        """
        self.__les_matchs = []

    def __str__(self):
        return f'Phase finale : {self.__id_phase_f} |'
