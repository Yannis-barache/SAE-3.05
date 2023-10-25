"""
Module contenant la classe Poule
"""

from escrimeur import Escrimeur
from match import Match


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

    def generer_matchs(self, infos: tuple[Escrimeur, list[Escrimeur]],
                       heure_debut: float) -> list[Match]:
        """
        Fonction qui genere les matchs de la poule

        Args:
            infos (tuple[Escrimeur, list[Escrimeur]]): Les infos de la poule

        Returns:
            list[Match]: liste des matchs de la poule
        """
        les_matchs = []
        arbitre, les_escrimeurs = infos
        for escrimeur1 in les_escrimeurs:
            for escrimeur2 in les_escrimeurs:
                if escrimeur1 != escrimeur2 and escrimeur1.get_id(
                ) < escrimeur2.get_id():
                    les_matchs.append(
                        Match(-1, self.__id, escrimeur1, escrimeur2, arbitre,
                              heure_debut))
                    heure_debut += 0.05
                    if heure_debut % 1 >= 0.6:
                        heure_debut += 0.4
        return les_matchs

    def __str__(self):
        return f'{self.__id}'
