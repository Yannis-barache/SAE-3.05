"""
Module contenant la classe Competition
"""

from categorie import Categorie
from arme import Arme
from lieu import Lieu


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

    def __str__(self) -> str:
        """
        Fonction qui retourne une chaine de caractere contenant les informations de la competition

        Returns:
            str: informations de la competition
        """
        return f"Competition: {self.__id}, {self.__nom}, {self.__date}, " \
        f"{self.__date_fin_inscription}, {self.__saison}, {self.__lieu}, " \
        f"{self.__arme}, {self.__categorie}"
