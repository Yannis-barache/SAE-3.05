"""
Module contenant la classe Arme
"""


class Arme:
    """
    Classe Arme permettant de créer une arme en fonction de son id et de son nom

    Attribute:
    _________
        id : int
            id de l'arme
        nom : str
            nom de l'arme

    Methodes:
    _________

        get_id(self):
            Retourne l'id de l'arme

        get_nom(self):
            Retourne le nom de l'arme

        set_id(self, id_arme: int):
            Modifie l'id de l'arme

        set_nom(self, nom: str):
            Modifie le nom de l'arme

        __str__(self):
            Affiche l'objet Arme
    """

    def __init__(self, id_arme: int, nom: str):
        """
        Fonction d'instanciation de la classe Arme

        Args:
        ______
            id_arme : int
                id de l'arme
            nom : str
                nom de l'arme
        """
        self.__id = id_arme
        self.__nom = nom

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

    def __str__(self):
        """
        Fonction qui retourne une chaine de caractere contenant les informations de l'arme

        Returns:
            str: informations de l'arme
        """
        return f"{self.__id} - {self.__nom}"
