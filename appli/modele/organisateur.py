"""
Module contenant la classe Organisateur
"""


class Organisateur:
    """
    Classe Organisateur
    """

    def __init__(self, id_organisateur: int, nom: str, prenom: str,
                 adresse_mail: str, mdp: str, nom_utilisateur: str):
        self.__id = id_organisateur
        self.__nom = nom
        self.__prenom = prenom
        self.__adresse_mail = adresse_mail
        self.__mdp = mdp
        self.__nom_utilisateur = nom_utilisateur

    def get_id(self) -> int:
        """
        Fonction qui retourne l'id de l'organisateur
        """
        return self.__id

    def get_nom(self) -> str:
        """
        Fonction qui retourne le nom de l'organisateur
        """
        return self.__nom

    def get_prenom(self) -> str:
        """
        Fonction qui retourne le prénom de l'organisateur
        """
        return self.__prenom

    def get_adresse_mail(self) -> str:
        """
        Fonction qui retourne l'adresse mail de l'organisateur
        """
        return self.__adresse_mail

    def get_mdp(self) -> str:
        """
        Fonction qui retourne le mot de passe de l'organisateur
        """
        return self.__mdp

    def get_nom_utilisateur(self) -> str:
        """
        Fonction qui retourne le nom d'utilisateur de l'organisateur
        """
        return self.__nom_utilisateur

    def set_id(self, id_organisateur: int):
        """
        Fonction qui modifie l'id de l'organisateur
        """
        self.__id = id_organisateur

    def set_nom(self, nom: str):
        """
        Fonction qui modifie le nom de l'organisateur
        """
        self.__nom = nom

    def set_prenom(self, prenom: str):
        """
        Fonction qui modifie le prénom de l'organisateur
        """
        self.__prenom = prenom

    def set_adresse_mail(self, adresse_mail: str):
        """
        Fonction qui modifie l'adresse mail de l'organisateur
        """
        self.__adresse_mail = adresse_mail

    def set_mdp(self, mdp: str):
        """
        Fonction qui modifie le mot de passe de l'organisateur
        """
        self.__mdp = mdp

    def set_nom_utilisateur(self, nom_utilisateur: str):
        """
        Fonction qui modifie le nom d'utilisateur de l'organisateur
        """
        self.__nom_utilisateur = nom_utilisateur

    def __str__(self):
        return (
            f'Organisateur : {self.__id} - {self.__nom} - {self.__prenom} - '
            f'{self.__adresse_mail} - {self.__mdp} - {self.__nom_utilisateur} |'
        )
