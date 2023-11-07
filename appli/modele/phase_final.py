"""
Module contenant la classe PhaseFinal
"""

from match import Match
from escrimeur import Escrimeur
import random


class PhaseFinal:
    """
    La classe PhaseFinal
    """

    def __init__(self, id_phase_f: int):
        self.__id_phase_f = id_phase_f
        self.__les_matchs: list[Match] = []

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

    def set_id_phase_f(self, id_phase_f: int) -> None:
        """
        Fonction qui modifie l'id de la phase finale

        Args:
            id_phase_f (int): id de la phase finale
        """
        self.__id_phase_f = id_phase_f

    def generer_les_matchs(self, liste_escrimeurs: list[Escrimeur | None],
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
        cpt = 0
        liste_matchs = []
        while cpt < len(liste_escrimeurs) / 2:
            escrimeur1 = liste_escrimeurs[cpt]
            escrimeur2 = liste_escrimeurs[-(cpt + 1)]
            arbitre = random.choice(liste_arbitres)
            liste_matchs.append(
                Match(-1, self.__id_phase_f, escrimeur1, escrimeur2, arbitre,
                      heure_debut, False))
            heure_debut += 0.25
            if heure_debut % 1 >= 0.6:
                heure_debut += 0.4
            cpt += 1
        self.__les_matchs = liste_matchs
        return liste_matchs

    def __str__(self):
        return f'Phase finale : {self.__id_phase_f} |'
