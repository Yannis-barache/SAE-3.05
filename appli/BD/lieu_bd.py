from sqlalchemy.sql.expression import text
from appli.modele.lieu import Lieu


class LieuBD:
    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_lieu(self):
        query = text("SELECT idLieu, adresseLieu, descriptionLieu FROM LIEU")
        result = self.__connexion.execute(query)
        lieux = []
        for id_lieu, adresse, description in result:
            lieux.append(Lieu(id_lieu, adresse, description))
        return lieux

    def get_lieu_by_id(self, id):
        query = text("SELECT idLieu, adresseLieu, descriptionLieu FROM LIEU WHERE idLieu = :id")
        result = self.__connexion.execute(query, id=id)
        for id_lieu, adresse, description in result:
            return Lieu(id_lieu, adresse, description)
        return None
