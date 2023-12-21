"""
Module contenant la classe Lieu
"""


class Lieu:
    """
    Classe Lieu
    """

    def __init__(self, id_lieu: int, description: str, adresse: str):
        self.__id = id_lieu
        self.__description = description
        self.__adresse = adresse

    def get_id(self):
        """
        Fonction qui retourne l'id du lieu
        
        Returns :
            int : id du lieu
        """
        return self.__id

    def get_description(self):
        """
        Fonction qui retourne la description du lieu
        
        Returns :
            str : description du lieu
        """
        return self.__description

    def get_adresse(self):
        """
        Fonction qui retourne l'adresse du lieu
        
        Returns :
            str : adresse du lieu
        """
        return self.__adresse

    def set_id(self, id_lieu: int):
        """
        Fonction qui modifie l'id du lieu

        Args :
            id_lieu (int) : nouvel id du lieu
        """
        self.__id = id_lieu

    def set_description(self, description: str):
        """
        Fonction qui modifie la description du lieu
        """
        self.__description = description

    def set_adresse(self, adresse: str):
        """
        Fonction qui modifie l'adresse du lieu

        Args :
            adresse (str) : adresse du lieu
        """
        self.__adresse = adresse

    def __str__(self):
        """
        Fonction qui retourne une chaine de caractère contenant les informations du lieu

        Returns :
            str : informations du lieu
        """
        return "Lieu : " + self.__description + " " + self.__adresse + " " + str(
            self.__id) + " |"
