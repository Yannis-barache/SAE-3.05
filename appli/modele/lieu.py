"""
Module contenant la classe Lieu
"""


class Lieu:
    """
    Classe Lieu
    """

    def __init__(self, id_lieu: int, nom: str, description: str, adresse: str):
        self.__id = id_lieu
        self.__nom = nom
        self.__description = description
        self.__adresse = adresse

    def get_id(self):
        """
        Fonction qui retourne l'id de la categorie

        Returns:
            int: id de la categorie
        """
        return self.__id

    def get_nom(self):
        """
        Fonction qui retourne le nom de la categorie

        Returns:
            str: nom de la categorie
        """
        return self.__nom

    def get_description(self):
        """
        Fonction qui retourne la description de la categorie

        Returns:
            str: description de la categorie
        """
        return self.__description

    def get_adresse(self):
        """
        Fonction qui retourne l'adresse de la categorie

        Returns:
            str: adresse de la categorie
        """
        return self.__adresse

    def set_id(self, id_lieu: int):
        """
        Fonction qui modifie l'id de la categorie

        Args:
            id (int): id de la categorie
        """
        self.__id = id_lieu

    def set_nom(self, nom: str):
        """
        Fonction qui modifie le nom de la categorie

        Args:
            nom (str): nom de la categorie
        """
        self.__nom = nom

    def set_description(self, description: str):
        """
        Fonction qui modifie la description de la categorie

        Args:
            description (str): description de la categorie
        """
        self.__description = description

    def set_adresse(self, adresse: str):
        """
        Fonction qui modifie l'adresse de la categorie

        Args:
            adresse (str): adresse de la categorie
        """
        self.__adresse = adresse

    def __str__(self):
        """
        Fonction qui retourne une chaine de caractere contenant les informations de la categorie

        Returns:
            str: informations de la categorie
        """
        return "id : " + str(
            self.__id
        ) + " nom : " + self.__nom + " description : " + self.__description + " adresse : " + str(
            self.__adresse)
