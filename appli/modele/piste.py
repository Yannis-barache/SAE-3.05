"""
Module contenant la classe Piste
"""
from lieu import Lieu



class Piste:
    """
    Classe Piste
    """

    def __init__(self, id_piste: int, lieu: int, description_piste: str):
        """
        Constructeur de la classe Piste
        :param id_piste: id de la piste
        :param lieu: le lieu
        :param description_piste: description de la piste
        """
        self.__id = id_piste
        self.__lieu = lieu
        self.__description = description_piste


    def get_id_piste(self) -> int:

        """
        Fonction qui retourne l'id de la piste

        Returns:
            int: id de la piste
        """

        return self.__id

    def get_lieu(self):
        """
        Fonction qui retourne l'id du lieu

        Returns :
            int : id du lieu
        """
        return self.__lieu



    def get_description(self):
        """
        Fonction qui retourne la description de la piste

        Returns :
            str : description de la piste
        """
        return self.__description

    def __str__(self):
        """
        Fonction qui retourne une chaine de caractere contenant les informations de la piste

        Returns :
            str : informations de la piste
        """
        return ("Piste : id = " + str(self.__id) + ", idLieu = " + str(self.__lieu) +
                ", description = " + str(self.__description))
        return self.__id_piste



    def set_id_piste(self, id_piste: int) -> None:
        """
        Fonction qui modifie l'id de la piste

        Args:
            id_piste (int): id de la piste
        """
        self.__id_piste = id_piste

    def set_id_lieu(self, id_lieu: int) -> None:
        """
        Fonction qui modifie l'id du lieu

        Args:
            id_lieu (int): id du lieu
        """
        self.__id_lieu = id_lieu

    def set_description(self, description: str) -> None:
        """
        Fonction qui modifie la description de la piste

        Args:
            description (str): description de la piste
        """
        self.__description = description
