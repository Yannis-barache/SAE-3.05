"""
Module contenant la classe Categorie
"""


class Categorie:
    """
    Classe Categorie
    """

    def __init__(self, id_cate: int, nom: str):
        """
        Constructeur de la classe Categorie

        Args:
            id (int): L'id de la categorie
            nom (str): Le nom de la categorie
        """
        self.__id = id_cate
        self.__nom = nom

    def get_id(self) -> int:
        """
        Fonction qui retourne l'id de la categorie

        Returns:
            str: id de la categorie
        """
        return self.__id

    def get_nom(self) -> str:
        """
        Fonction qui retourne le nom de la categorie

        Returns:
            str: nom de la categorie
        """
        return self.__nom

    def set_id(self, id_cate: int) -> None:
        """
        Fonction qui modifie l'id de la categorie

        Args:
            id (int): id de la categorie
        """
        self.__id = id_cate

    def set_nom(self, nom: str) -> None:
        """
        Fonction qui modifie le nom de la categorie

        Args:
            nom (str): nom de la categorie
        """
        self.__nom = nom

    def __str__(self) -> str:
        """
        Fonction qui retourne une chaine de caractere contenant les informations de la categorie

        Returns:
            str: informations de la categorie
        """
        return f"Catégorie : {self.__id} - {self.__nom} |"
