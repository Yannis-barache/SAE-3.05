from sqlalchemy.sql.expression import text
from appli.modele.arbitrer import Arbitrer
from appli.BD.escrimeur_bd import EscrimeurBD
from appli.BD.competition_bd import CompetitionBD


class ArbitreBD:
    def __int__(self, connexion):
        self.__connexion = connexion

    def get_all_arbitre(self):
        try:
            query = text("SELECT idEscrimeur, idCompetition FROM ARBITRER")
            result = self.__connexion.execute(query)
            arbitres = []
            for id_escrimeur, id_categorie in result:
                escrimeur = EscrimeurBD.get_escrimeur_by_id(self, id_escrimeur)
                competition = CompetitionBD.get_competition_by_id(self, id_categorie)
                arbitres.append(Arbitrer(escrimeur, competition))
            return arbitres
        except Exception as e:
            print(e)
            return None


    def get_arbitre_by_id(self, id):
        try:
            query = text("SELECT idEscrimeur, idCompetition FROM ARBITRER WHERE idEscrimeur = :id")
            result = self.__connexion.execute(query, id=id)
            for id_escrimeur, id_competition in result:
                escrimeur = EscrimeurBD.get_escrimeur_by_id(self, id_escrimeur)
                competition = CompetitionBD.get_competition_by_id(self, id_competition)
                return Arbitrer(escrimeur, competition)
            return None
        except Exception as e:
            print(e)
            return None
