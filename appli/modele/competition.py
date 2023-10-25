"""
Module contenant la classe Competition
"""

from categorie import Categorie
from arme import Arme
from lieu import Lieu
from escrimeur import Escrimeur
import math
import constantes as const
from exceptions import PasAssezDArbitres
from poule import Poule


class Competition:
    """
    Classe Competition
    """

    def __init__(self, id_comp: int, nom: str, date: str,
                 date_fin_inscription: str, saison: str, lieu: Lieu,
                 arme: Arme, categorie: Categorie, coeficient: float):
        """
        Constructeur de la classe Competition

        Args:
            id (int): L'id de la competition
            nom (str): Le nom de la competition
            date (str): La date de la competition
            date_fin_inscription (str): La date de fin d'inscription de la competition
            saison (str): La saison de la competition
            lieu (Lieu): Le lieu de la competition
            arme (Arme): L'arme de la competition
            categorie (Categorie): La categorie de la competition
        """
        self.__id = id_comp
        self.__nom = nom
        self.__date = date
        self.__date_fin_inscription = date_fin_inscription
        self.__saison = saison
        self.__lieu = lieu
        self.__arme = arme
        self.__categorie = categorie
        self.__coeficient = coeficient

    def get_id(self) -> int:
        """
        Fonction qui retourne l'id de la competition

        Returns:
            int: id de la competition
        """
        return self.__id

    def get_nom(self) -> str:
        """
        Fonction qui retourne le nom de la competition

        Returns:
            str: nom de la competition
        """
        return self.__nom

    def get_date(self) -> str:
        """
        Fonction qui retourne la date de la competition

        Returns:
            str: date de la competition
        """
        return self.__date

    def get_date_fin_inscription(self) -> str:
        """
        Fonction qui retourne la date de fin d'inscription de la competition
        
        Returns:
            str: date de fin d'inscription de la competition
        """
        return self.__date_fin_inscription

    def get_saison(self) -> str:
        """
        Fonction qui retourne la saison de la competition

        Returns:
            str: La saison de la competition
        """
        return self.__saison

    def get_lieu(self) -> Lieu:
        """
        Fonction qui retourne le lieu de la competition

        Returns:
            Lieu: Le lieu de la competition
        """
        return self.__lieu

    def get_arme(self) -> Arme:
        """
        Fonction qui retourne l'arme de la competition

        Returns:
            Arme: L'arme de la competition
        """
        return self.__arme

    def get_categorie(self) -> Categorie:
        """
        Fonction qui retourne la categorie de la competition

        Returns:
            Categorie: La categorie de la competition
        """
        return self.__categorie

    def get_coeficient(self) -> float:
        """
        Fonction qui retourne le coeficient de la competition

        Returns:
            float: Le coeficient de la competition
        """
        return self.__coeficient

    def set_id(self, id_comp: int) -> None:
        """
        Fonction qui modifie l'id de la competition

        Args:
            id (int): id de la competition
        """
        self.__id = id_comp

    def set_nom(self, nom: str) -> None:
        """
        Fonction qui modifie le nom de la competition

        Args:
            nom (str): nom de la competition
        """
        self.__nom = nom

    def set_date(self, date: str) -> None:
        """
        Fonction qui modifie la date de la competition

        Args:
            date (str): date de la competition
        """
        self.__date = date

    def set_date_fin_inscription(self, date_fin_inscription: str) -> None:
        """
        Fonction qui modifie la date de fin d'inscription de la competition

        Args:
            date_fin_inscription (str): date de fin d'inscription de la competition
        """
        self.__date_fin_inscription = date_fin_inscription

    def set_saison(self, saison: str) -> None:
        """
        Fonction qui modifie la saison de la competition

        Args:
            saison (str): saison de la competition
        """
        self.__saison = saison

    def set_lieu(self, lieu: Lieu) -> None:
        """
        Fonction qui modifie le lieu de la competition

        Args:
            lieu (Lieu): lieu de la competition
        """
        self.__lieu = lieu

    def set_arme(self, arme: Arme) -> None:
        """
        Fonction qui modifie l'arme de la competition

        Args:
            arme (Arme): arme de la competition
        """
        self.__arme = arme

    def set_categorie(self, categorie: Categorie) -> None:
        """
        Fonction qui modifie la categorie de la competition

        Args:
            categorie (Categorie): categorie de la competition
        """
        self.__categorie = categorie

    def set_coeficient(self, coeficient: float) -> None:
        """
        Fonction qui modifie le coeficient de la competition

        Args:
            coeficient (float): coeficient de la competition
        """
        self.__coeficient = coeficient

    @staticmethod
    def generation_poule(
        liste_escrimeur: list[Escrimeur], liste_arbitre: list[Escrimeur]
    ) -> dict[Poule, tuple[Escrimeur, list[Escrimeur]]] | None:
        """
        Fonction qui genere les poules de la competition

        Args:
            liste_escrimeur (list): liste des escrimeurs de la competition
            liste_arbitre (list): liste des arbitres de la competition
        
        Returns:
            dict[int, tuple[Escrimeur, list[Escrimeur]]]: 
                dictionnaire contenant les poules de la competition
            La clé est le numéro de la poule et la valeur est un tuple 
            contenant l'arbitre de la poule et la liste des escrimeurs de la poule
        """
        try:
            liste_escrimeur = Competition.trie_classement_inital(
                liste_escrimeur)
            nombre_poule = Competition.nombre_poule(len(liste_escrimeur),
                                                    len(liste_arbitre))[0]
            poule_int: dict[int, tuple[Escrimeur, list[Escrimeur]]] = {}

            # On initialise les poules avec les arbitres
            for i in range(nombre_poule):
                poule_int[i] = (liste_arbitre[i], [])

            # On ajoute les escrimeurs dans les poules
            for i in range(len(liste_escrimeur)):
                poule_int[i % nombre_poule][1].append(liste_escrimeur[i])

            # On transforme les poules en poules de type Poule
            poule: dict[Poule, tuple[Escrimeur, list[Escrimeur]]] = {}
            for i in range(nombre_poule):
                poule[Poule(-1)] = poule_int[i]
            return poule
        except PasAssezDArbitres:
            return None

    @staticmethod
    def trie_classement_inital(
            liste_escrimeur: list[Escrimeur]) -> list[Escrimeur]:
        """
        Fonction qui trie les escrimeurs par classement initial

        Args:
            liste_escrimeur (list[Escrimeur]): liste des escrimeurs de la competition

        Returns:
            list[Escrimeur]: liste des escrimeurs de la competition triee par classement initial
        """
        return sorted(liste_escrimeur,
                      key=lambda escrimeur: escrimeur.get_classement())

    @staticmethod
    def nombre_poule(nombre_escrimeur: int,
                     nombre_arbitre: int) -> tuple[int, int]:
        """
        Fonction qui retourne le nombre de poule et le nombre d'escrimeur par poule

        Args:
            nombre_escrimeur (int): nombre d'escrimeur de la competition
            nombre_arbitre (int): nombre d'arbitre de la competition

        Returns:
            tuple[int, int]: Le nombre de poule et le nombre d'escrimeur par poule
        """
        min_arbitres_necessaires = math.ceil(
            nombre_escrimeur / const.NOMBRE_MAXIMAL_ESCRIMEUR_POULE)
        if nombre_arbitre < min_arbitres_necessaires:
            raise PasAssezDArbitres(
                "Pas assez d'arbitres pour couvrir chaque poule.")
        nombre_poule = math.ceil(nombre_escrimeur /
                                 const.NOMBRE_MAXIMAL_ESCRIMEUR_POULE)
        nombre_escrimeur_par_poule = math.ceil(nombre_escrimeur / nombre_poule)
        return nombre_poule, nombre_escrimeur_par_poule

    def __str__(self) -> str:
        """
        Fonction qui retourne une chaine de caractere contenant les informations de la competition

        Returns:
            str: informations de la competition
        """
        return f"Competition: {self.__id}, {self.__nom}, {self.__date}, " \
        f"{self.__date_fin_inscription}, {self.__saison}, {self.__lieu}, " \
        f"{self.__arme}, {self.__categorie}"
