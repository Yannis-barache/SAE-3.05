"""
Module contenant la classe Escrimeur
"""

from club import Club


class Escrimeur:
    """
    Classe Escrimeur
    """

    def __init__(self, id_escrim: int, nom: str, prenom: str,
                 date_naissance: str, nom_utilisateur: str, adresse_mail: str,
                 mdp: str, licence: str, classement: int | None, club: Club):
        self.__id = id_escrim
        self.__nom = nom
        self.__prenom = prenom
        self.__date_naissance = date_naissance
        self.__nom_utilisateur = nom_utilisateur
        self.__adresse_mail = adresse_mail
        self.__mdp = mdp
        self.__licence = licence
        self.__classement = classement
        self.__club = club

    def get_id(self) -> int:
        """
        Fonction qui retourne l'id de l'escrimeur

        Returns:
            int: id de l'escrimeur
        """
        return self.__id

    def get_nom(self) -> str:
        """
        Fonction qui retourne le nom de l'escrimeur

        Returns:
            str: nom de l'escrimeur
        """
        return self.__nom

    def get_prenom(self) -> str:
        """
        Fonction qui retourne le prenom de l'escrimeur

        Returns:
            str: prenom de l'escrimeur
        """
        return self.__prenom

    def get_date_naissance(self) -> str:
        """
        Fonction qui retourne la date de naissance de l'escrimeur

        Returns:
            str: date de naissance de l'escrimeur
        """
        return self.__date_naissance

    def get_nom_utilisateur(self) -> str:
        """
        Fonction qui retourne le nom d'utilisateur de l'escrimeur

        Returns:
            str: nom d'utilisateur de l'escrimeur
        """
        return self.__nom_utilisateur

    def get_adresse_mail(self) -> str:
        """
        Fonction qui retourne l'adresse mail de l'escrimeur

        Returns:
            str: adresse mail de l'escrimeur
        """
        return self.__adresse_mail

    def get_mdp(self) -> str:
        """
        Fonction qui retourne le mot de passe de l'escrimeur

        Returns:
            str: mot de passe de l'escrimeur
        """
        return self.__mdp

    def get_licence(self) -> str:
        """
        Fonction qui retourne la licence de l'escrimeur

        Returns:
            str: licence de l'escrimeur
        """
        return self.__licence

    def get_classement(self) -> int | None:
        """
        Fonction qui retourne le classement de l'escrimeur

        Returns:
            int: classement de l'escrimeur
        """
        return self.__classement

    def get_club(self) -> Club:
        """
        Fonction qui retourne le club de l'escrimeur

        Returns:
            Club: club de l'escrimeur
        """
        return self.__club

    def set_id(self, id_escrim: int) -> None:
        """
        Fonction qui modifie l'id de l'escrimeur

        Args:
            id (int): id de l'escrimeur
        """
        self.__id = id_escrim

    def set_nom(self, nom: str) -> None:
        """
        Fonction qui modifie le nom de l'escrimeur

        Args:
            nom (str): nom de l'escrimeur
        """
        self.__nom = nom

    def set_prenom(self, prenom: str) -> None:
        """
        Fonction qui modifie le prenom de l'escrimeur

        Args:
            prenom (str): prenom de l'escrimeur
        """
        self.__prenom = prenom

    def set_date_naissance(self, date_naissance: str) -> None:
        """
        Fonction qui modifie la date de naissance de l'escrimeur

        Args:
            date_naissance (str): date de naissance de l'escrimeur
        """
        self.__date_naissance = date_naissance

    def set_nom_utilisateur(self, nom_utilisateur: str) -> None:
        """
        Fonction qui modifie le nom d'utilisateur de l'escrimeur

        Args:
            nom_utilisateur (str): nom d'utilisateur de l'escrimeur
        """
        self.__nom_utilisateur = nom_utilisateur

    def set_adresse_mail(self, adresse_mail: str) -> None:
        """
        Fonction qui modifie l'adresse mail de l'escrimeur

        Args:
            adresse_mail (str): adresse mail de l'escrimeur
        """
        self.__adresse_mail = adresse_mail

    def set_mdp(self, mdp: str) -> None:
        """
        Fonction qui modifie le mot de passe de l'escrimeur

        Args:
            mdp (str): mot de passe de l'escrimeur
        """
        self.__mdp = mdp

    def set_licence(self, licence: str) -> None:
        """
        Fonction qui modifie la licence de l'escrimeur

        Args:
            licence (str): licence de l'escrimeur
        """
        self.__licence = licence

    def set_classement(self, classement: int | None) -> None:
        """
        Fonction qui modifie le classement de l'escrimeur

        Args:
            classement (int): classement de l'escrimeur
        """
        self.__classement = classement

    def set_club(self, club: Club) -> None:
        """
        Fonction qui modifie le club de l'escrimeur

        Args:
            club (Club): club de l'escrimeur
        """
        self.__club = club

    def __str__(self) -> str:
        """
        Fonction qui retourne une chaine de caractere contenant les informations de l'escrimeur

        Returns:
            str: informations de l'escrimeur
        """
        return f'{self.__id} - {self.__nom} - {self.__prenom} - {self.__date_naissance} - ' \
                f'{self.__nom_utilisateur} - {self.__adresse_mail} - {self.__mdp} - ' \
                f'{self.__licence} - {self.__classement} - {self.__club}'
