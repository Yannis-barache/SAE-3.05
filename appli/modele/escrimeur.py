"""
Module contenant la classe Escrimeur
"""

from club import Club
from categorie import Categorie


class Escrimeur:
    """
    Classe Escrimeur
    """

    def __init__(self, id_escrim: int, nom: str, prenom: str, sexe: str,
                 date_naissance: str, nom_utilisateur: str, mdp: str,
                 licence: str, classement: int | None, club: Club,
                 categorie: Categorie, arbitrage: bool):
        self.__id = id_escrim
        self.__nom = nom
        self.__prenom = prenom
        self.__sexe = sexe
        self.__date_naissance = date_naissance
        self.__nom_utilisateur = nom_utilisateur
        self.__mdp = mdp
        self.__licence = licence
        self.__classement = classement
        self.__club = club
        self.__categorie = categorie
        self.__arbitrage = arbitrage

    def get_id(self) -> int:
        """
        Fonction qui retourne l'id de l'escrimeur

        Returns:
            int: id de l'escrimeur
        """
        return self.__id

    def get_nom(self) -> str:
        """
        Fonction qui retourne le nom de l'escrimeur

        Returns:
            str: nom de l'escrimeur
        """
        return self.__nom

    def get_prenom(self) -> str:
        """
        Fonction qui retourne le prenom de l'escrimeur

        Returns:
            str: prenom de l'escrimeur
        """
        return self.__prenom

    def get_sexe(self) -> str:
        """
        Fonction qui retourne le sexe de l'escrimeur

        Returns:
            str: sexe de l'escrimeur
        """
        return self.__sexe

    def get_date_naissance(self) -> str:
        """
        Fonction qui retourne la date de naissance de l'escrimeur

        Returns:
            str: date de naissance de l'escrimeur
        """
        return self.__date_naissance

    def get_nom_utilisateur(self) -> str:
        """
        Fonction qui retourne le nom d'utilisateur de l'escrimeur

        Returns:
            str: nom d'utilisateur de l'escrimeur
        """
        return self.__nom_utilisateur

    def get_mdp(self) -> str:
        """
        Fonction qui retourne le mot de passe de l'escrimeur

        Returns:
            str: mot de passe de l'escrimeur
        """
        return self.__mdp

    def get_licence(self) -> str:
        """
        Fonction qui retourne la licence de l'escrimeur

        Returns:
            str: licence de l'escrimeur
        """
        return self.__licence

    def get_classement(self) -> int | None:
        """
        Fonction qui retourne le classement de l'escrimeur

        Returns:
            int: classement de l'escrimeur
        """
        return self.__classement

    def get_club(self) -> Club:
        """
        Fonction qui retourne le club de l'escrimeur

        Returns:
            Club: club de l'escrimeur
        """
        return self.__club

    def get_categorie(self) -> Categorie:
        """
        Fonction qui retourne la categorie de l'escrimeur

        Returns:
            Categorie: categorie de l'escrimeur
        """
        return self.__categorie

    def get_arbitrage(self) -> bool:
        """
        Fonction qui retourne l'arbitrage de l'escrimeur

        Returns:
            bool: arbitrage de l'escrimeur
        """
        return self.__arbitrage

    def set_id(self, id_escrim: int) -> None:
        """
        Fonction qui modifie l'id de l'escrimeur

        Args:
            id_escrim (int): id de l'escrimeur
        """
        self.__id = id_escrim

    def set_nom(self, nom: str) -> None:
        """
        Fonction qui modifie le nom de l'escrimeur

        Args:
            nom (str): nom de l'escrimeur
        """
        self.__nom = nom

    def set_prenom(self, prenom: str) -> None:
        """
        Fonction qui modifie le prenom de l'escrimeur

        Args:
            prenom (str): prenom de l'escrimeur
        """
        self.__prenom = prenom

    def set_sexe(self, sexe: str) -> None:
        """
        Fonction qui modifie le sexe de l'escrimeur

        Args:
            sexe (str): sexe de l'escrimeur
        """
        self.__sexe = sexe

    def set_date_naissance(self, date_naissance: str) -> None:
        """
        Fonction qui modifie la date de naissance de l'escrimeur

        Args:
            date_naissance (str): date de naissance de l'escrimeur
        """
        self.__date_naissance = date_naissance

    def set_nom_utilisateur(self, nom_utilisateur: str) -> None:
        """
        Fonction qui modifie le nom d'utilisateur de l'escrimeur

        Args:
            nom_utilisateur (str): nom d'utilisateur de l'escrimeur
        """
        self.__nom_utilisateur = nom_utilisateur

    def set_mdp(self, mdp: str) -> None:
        """
        Fonction qui modifie le mot de passe de l'escrimeur

        Args:
            mdp (str): mot de passe de l'escrimeur
        """
        self.__mdp = mdp

    def set_licence(self, licence: str) -> None:
        """
        Fonction qui modifie la licence de l'escrimeur

        Args:
            licence (str): licence de l'escrimeur
        """
        self.__licence = licence

    def set_classement(self, classement: int) -> None:
        """
        Fonction qui modifie le classement de l'escrimeur

        Args:
            classement (int): classement de l'escrimeur
        """
        self.__classement = classement

    def set_club(self, club: Club) -> None:
        """
        Fonction qui modifie le club de l'escrimeur

        Args:
            club (Club): club de l'escrimeur
        """
        self.__club = club

    def set_categorie(self, categorie: Categorie) -> None:
        """
        Fonction qui modifie la categorie de l'escrimeur

        Args:
            categorie (Categorie): categorie de l'escrimeur
        """
        self.__categorie = categorie

    def __lt__(self, autre: 'Escrimeur') -> bool:
        """
        Fonction qui compare le classement de l'escrimeur avec un autre

        Args:
            autre (Escrimeur): autre escrimeur

        Returns:
            bool: True si le classement de l'escrimeur est inferieur a celui de l'autre, False sinon
        """
        if self.__classement is None:
            return False
        if autre.__classement is None:
            return True
        return self.__classement < autre.__classement

    def set_arbitrage(self, arbitrage: bool) -> None:
        """
        Fonction qui modifie l'arbitrage de l'escrimeur

        Args:
            arbitrage (bool): arbitrage de l'escrimeur
        """
        self.__arbitrage = arbitrage

    def __str__(self) -> str:
        """
        Fonction qui retourne une chaine de caractere contenant les informations de l'escrimeur

        Returns:
            str: informations de l'escrimeur
        """
        return f'Escrimeur : {self.__id} - {self.__nom} - {self.__prenom} - ' \
            f'{self.__date_naissance} - ' \
            f'{self.__nom_utilisateur} - {self.__mdp} - ' \
            f'{self.__licence} - {self.__classement} - '\
            f'{self.__club} - {self.__categorie}' \
            f' - {self.__arbitrage} |'
