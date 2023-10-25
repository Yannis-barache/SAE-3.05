"""
Module contenant la classe Arme
"""


class Arme:
    """
    Classe Arme
    """

    def __init__(self, id_arme: int, nom: str, sexe: str):
        self.__id = id_arme
        self.__nom = nom
        self.__sexe = sexe

    def get_id(self):
        """
        Fonction qui retourne l'id de l'arme

        Returns:
            int: id de l'arme
        """
        return self.__id

    def get_nom(self):
        """
        Fonction qui retourne le nom de l'arme

        Returns:
            str: nom de l'arme
        """
        return self.__nom

    def get_sexe(self):
        """
        Fonction qui retourne le sexe de l'arme

        Returns:
            str: sexe de l'arme
        """
        return self.__sexe

    def set_id(self, id_arme: int):
        """
        Fonction qui modifie l'id de l'arme

        Args:
            id (int): id de l'arme
        """
        self.__id = id_arme

    def set_nom(self, nom: str):
        """
        Fonction qui modifie le nom de l'arme

        Args:
            nom (str): nom de l'arme
        """
        self.__nom = nom

    def set_sexe(self, sexe: str):
        """
        Fonction qui modifie le sexe de l'arme

        Args:
            sexe (str): sexe de l'arme
        """
        self.__sexe = sexe

    def __str__(self):
        """
        Fonction qui retourne une chaine de caractere contenant les informations de l'arme

        Returns:
            str: informations de l'arme
        """
        return f"{self.__id} - {self.__nom} - {self.__sexe}"
