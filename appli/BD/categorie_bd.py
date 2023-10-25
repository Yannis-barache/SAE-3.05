from sqlalchemy.sql.expression import text
from appli.modele.categorie import Categorie


class CategorieBD:
    def __int__(self, connexion):
        self.__connexion = connexion

    def get_all_categorie(self):
        query = text("SELECT idCategorie, nomCategorie FROM CATEGORIE")
        result = self.__connexion.execute(query)
        categories = []
        for id_categorie, nom in result:
            categories.append(Categorie(id_categorie, nom))
        return categories

    def get_categorie_by_id(self, id):
        query = text("SELECT idCategorie, nomCategorie FROM CATEGORIE WHERE idCategorie = :id")
        result = self.__connexion.execute(query, id=id)
        for id_categorie, nom in result:
            return Categorie(id_categorie, nom)
        return None
