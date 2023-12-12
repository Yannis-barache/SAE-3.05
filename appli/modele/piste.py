"""
Module contenant la classe Piste
"""


class Piste:
    """
    Classe
    """

    def __init__(self, id_piste: int, id_lieu: int, description_piste: str):
        """
        Constructeur de la classe Piste
        :param id_piste: id de la piste
        :param id_lieu: id du lieu
        :param description_piste: description de la piste
        """
        self.__id = id_piste
        self.__id_lieu = id_lieu
        self.__description = description_piste

    def get_id(self):
        """
        Fonction qui retourne l'id de la categorie

        Returns:
            int: id de la categorie
        """
        return self.__id

    def get_id_lieu(self):
        """
        Fonction qui retourne l'id du lieu

        Returns :
            int : id du lieu
        """
        return self.__id_lieu

    def set_description(self, description: str):
        """
        Fonction qui modifie la description de la categorie

        Args:
            description (str): description de la categorie
        """
        self.__description = description


    def get_description(self):
        """
        Fonction qui retourne la description de la categorie

        Returns :
            str : description de la categorie
        """
        return self.__description

    def __str__(self):
        """
        Fonction qui retourne une chaine de caractere contenant les informations de la categorie

        Returns :
            str : informations de la categorie
        """
        return ("Piste : id = " + str(self.__id) + ", idLieu = " + str(self.__idLieu) +
                ", description = " + str(self.__descriptionPiste))
