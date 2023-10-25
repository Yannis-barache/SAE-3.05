"""
Module contenant la classe Club
"""


class Club:
    """
    Classe Club
    """

    def __init__(self, id_club: int, nom: str, adresse: str):
        self.__id = id_club
        self.__nom = nom
        self.__adresse = adresse

    def get_id(self):
        """
        Fonction qui retourne l'id du club

        Returns:
            int: id du club
        """
        return self.__id

    def get_nom(self):
        """
        Fonction qui retourne le nom du club

        Returns:
            str: nom du club
        """
        return self.__nom

    def get_adresse(self):
        """
        Fonction qui retourne l'adresse du club

        Returns:
            str: adresse du club
        """
        return self.__adresse

    def set_id(self, id_club: int):
        """
        Fonction qui modifie l'id du club

        Args:
            id (int): id du club
        """
        self.__id = id_club

    def set_nom(self, nom: str):
        """
        Fonction qui modifie le nom du club

        Args:
            nom (str): nom du club
        """
        self.__nom = nom

    def set_adresse(self, adresse: str):
        """
        Fonction qui modifie l'adresse du club

        Args:
            adresse (str): adresse du club
        """
        self.__adresse = adresse

    def __str__(self):
        """
        Fonction qui retourne une chaine de caractere contenant les informations du club

        Returns:
            str: informations du club
        """
        return f"{self.__id} - {self.__nom} - {self.__adresse}"
