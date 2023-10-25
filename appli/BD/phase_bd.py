from sqlalchemy.sql.expression import text
from appli.modele.phase import Phase
from appli.BD.competition_bd import CompetitionBD

class PhaseBD:
    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_phase(self):
        query = text("SELECT idPhase, idCompetition FROM PHASE")
        result = self.__connexion.execute(query)
        phases = []
        for id_phase, id_competition in result:
            competition = CompetitionBD.get_competition_by_id(self, id_competition)
            phases.append(Phase(id_phase, competition))
        return phases

    def get_phase_by_id(self, id):
        query = text("SELECT idPhase, idCompetition FROM PHASE WHERE idPhase = :id")
        result = self.__connexion.execute(query, id=id)
        for id_phase, id_competition in result:
            competition = CompetitionBD.get_competition_by_id(self, id_competition)
            return Phase(id_phase, competition)
        return None
