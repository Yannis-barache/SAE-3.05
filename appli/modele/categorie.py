"""
Module contenant la classe Catégorie
"""


class Categorie:
    """
    Classe Catégorie
    """

    def __init__(self, id_cate: int, nom: str):
        """
        Constructeur de la classe Catégorie

        Args :
            id_cate (int) : L'id de la catégorie
            nom (str) : Le nom de la catégorie
        """
        self.__id = id_cate
        self.__nom = nom

    def get_id(self) -> int:
        """
        Fonction qui retourne l'id de la catégorie

        Returns :
            str : id de la catégorie
        """
        return self.__id

    def get_nom(self) -> str:
        """
        Fonction qui retourne le nom de la catégorie

        Returns :
            str : nom de la catégorie
        """
        return self.__nom

    def set_id(self, id_cate: int) -> None:
        """
        Fonction qui modifie l'id de la catégorie

        Args :
            id_cate (int) : id de la catégorie
        """
        self.__id = id_cate

    def set_nom(self, nom: str) -> None:
        """
        Fonction qui modifie le nom de la catégorie

        Args :
            nom (str) : nom de la catégorie
        """
        self.__nom = nom

    def __str__(self) -> str:
        """
        Fonction qui retourne une chaine de caractère contenant les informations de la catégorie

        Returns :
            str : informations de la catégorie
        """
        return f"Catégorie : {self.__id} - {self.__nom} |"
