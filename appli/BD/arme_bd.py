"""
    Fichier qui contient les requêtes SQL pour la table Arme
"""

from sqlalchemy.sql.expression import text
from appli.modele.arme import Arme


class ArmeBD:
    """
    Classe qui fait le lien entre les objets Arme et la BD
    """

    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_arme(self):
        """
        Méthode qui récupère toutes les armes
        :return: Une liste d'objets Arme
        """
        try:
            query = text("SELECT idArme, nomArme, sexeArme FROM ARMES")
            result = self.__connexion.execute(query)
            armes = []
            for id_arme, nom, sexe in result:
                armes.append(Arme(id_arme, nom, sexe))
            return armes
        except Exception as e:
            print(e)
            return None

    def get_arme_by_id(self, id_ar: int):
        """
        Méthode qui récupère une arme par son id
        :param id_ar: id de l'arme
        :return: Un objet Arme
        """
        try:
            query = text(
                "SELECT idArme, nomArme, sexeArme FROM ARMES WHERE idArme =" +
                str(id_ar))
            result = self.__connexion.execute(query)
            for id_arme, nom, sexe in result:
                return Arme(id_arme, nom, sexe)
            return None
        except Exception as e:
            print(e)
            return None
