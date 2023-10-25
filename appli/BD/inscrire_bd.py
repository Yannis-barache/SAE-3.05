from sqlalchemy.sql.expression import text
from appli.modele.inscrire import Inscrire
from appli.BD.escrimeur_bd import EscrimeurBD
from appli.BD.competition_bd import CompetitionBD


class InscrireBD:
    def __int__(self, connexion):
        self.__connexion = connexion

    def get_all_inscrire(self):
        query = text("SELECT idEscrimeur, idCompetition FROM INSCRIRE")
        result = self.__connexion.execute(query)
        inscrires = []
        for id_escrimeur, id_competition in result:
            escrimeur = EscrimeurBD.get_escrimeur_by_id(self, id_escrimeur)
            competition = CompetitionBD.get_competition_by_id(self, id_competition)
            inscrires.append(Inscrire(escrimeur, competition))
        return inscrires
