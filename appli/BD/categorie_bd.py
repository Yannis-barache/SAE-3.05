"""
    Fichier qui contient les requêtes SQL pour la table CATEGORIE
"""
import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from categorie import Categorie


class CategorieBD:
    """
    Classe CategorieBD
    """

    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_categorie(self):
        """
        Fonction qui retourne toutes les categories
        :return: liste de categorie
        """
        try:
            query = text("SELECT idCategorie, nomCategorie FROM CATEGORIE")
            result = self.__connexion.execute(query)
            categories = []
            for id_categorie, nom in result:
                categories.append(Categorie(id_categorie, nom))
            return categories
        except Exception as e:
            print(e)
            return None

    def get_categorie_by_id(self, id_cat: int):
        """
        Fonction qui retourne une categorie en fonction de son id
        :param id_cat: id de la categorie
        :return: categorie
        """
        try:
            query = text("SELECT idCategorie, nomCategorie FROM CATEGORIE "
                         "WHERE idCategorie =" + str(id_cat))
            result = self.__connexion.execute(query)
            for id_categorie, nom in result:
                return Categorie(id_categorie, nom)
            return None
        except Exception as e:
            print(e)
            return None
