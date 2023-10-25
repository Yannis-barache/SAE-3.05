from sqlalchemy.sql.expression import text
from appli.modele.arme import Arme


class ArmeBD:
    def __int__(self, connexion):
        self.__connexion = connexion

    def get_all_arme(self):
        query = text("SELECT idArme, nomArme FROM ARMES")
        result = self.__connexion.execute(query)
        armes = []
        for id_arme, nom in result:
            armes.append(Arme(id_arme, nom))
        return armes

    def get_arme_by_id(self, id):
        query = text("SELECT idArme, nomArme FROM ARMES WHERE idArme = :id")
        result = self.__connexion.execute(query, id=id)
        for id_arme, nom in result:
            return Arme(id_arme, nom)
        return None
