"""
Module contenant la classe Piste
"""

class Piste:
    """
    Classe Piste
    """

    def __init__(self, id_piste: int, id_lieu: int, description: str):
        self.__id_piste = id_piste
        self.__id_lieu = id_lieu
        self.__description = description

    def get_id_piste(self) -> int:
        """
        Fonction qui retourne l'id de la piste

        Returns:
            int: id de la piste
        """
        return self.__id_piste

    def get_id_lieu(self) -> int:
        """
        Fonction qui retourne l'id du lieu

        Returns:
            int: id du lieu
        """
        return self.__id_lieu

    def get_description(self) -> str:
        """
        Fonction qui retourne la description de la piste

        Returns:
            str: description de la piste
        """
        return self.__description

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

    def __str__(self):
        return f'{self.__description}'