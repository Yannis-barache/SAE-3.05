from sqlalchemy.sql.expression import text
from appli.modele.arme import Arme


class ArmeBD:
    def __int__(self, connexion):
        self.__connexion = connexion

    def get_all_arme(self):
        try:
            query = text("SELECT idArme, nomArme FROM ARMES")
            result = self.__connexion.execute(query)
            armes = []
            for id_arme, nom in result:
                armes.append(Arme(id_arme, nom))
            return armes
        except Exception as e:
            print(e)
            return None

    def get_arme_by_id(self, id):
        try:
            query = text("SELECT idArme, nomArme FROM ARMES WHERE idArme = :id")
            result = self.__connexion.execute(query, id=id)
            for id_arme, nom in result:
                return Arme(id_arme, nom)
            return None
        except Exception as e:
            print(e)
            return None
