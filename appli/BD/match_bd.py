from sqlalchemy import text
from appli.modele.match import Match
from appli.BD.phase_bd import PhaseBD
from appli.BD.escrimeur_bd import EscrimeurBD
from appli.BD.arbitre_bd import ArbitreBD


class MatchBD:
    def __int__(self, connexion):
        self.__connexion = connexion

    def get_all_match(self):
        try:
            query = text("SELECT idMatch, idPhase, idEscrimeur1, idEscrimeur2, idArbitre, heureMatch FROM MATCHS")
            result = self.__connexion.execute(query)
            matchs = []
            for id_match, id_phase, id_escrimeur1, id_escrimeur2, id_abitre, heure in result:
                phase = PhaseBD.get_phase_by_id(self, id_phase)
                escrimeur1 = EscrimeurBD.get_escrimeur_by_id(self, id_escrimeur1)
                escrimeur2 = EscrimeurBD.get_escrimeur_by_id(self, id_escrimeur2)
                arbitre = ArbitreBD.get_arbitre_by_id(self, id_abitre)
                matchs.append(Match(id_match, phase, escrimeur1, escrimeur2, arbitre, heure))
            return matchs
        except Exception as e:
            print(e)
            return None


    def get_match_by_id(self, id):
        try:
            query = text("SELECT idMatch, idPhase, idEscrimeur1, idEscrimeur2, idArbitre, heureMatch FROM MATCHS WHERE idMatch = :id")
            result = self.__connexion.execute(query, id=id)
            for id_match, id_phase, id_escrimeur1, id_escrimeur2, id_abitre, heure in result:
                phase = PhaseBD.get_phase_by_id(self, id_phase)
                escrimeur1 = EscrimeurBD.get_escrimeur_by_id(self, id_escrimeur1)
                escrimeur2 = EscrimeurBD.get_escrimeur_by_id(self, id_escrimeur2)
                arbitre = ArbitreBD.get_arbitre_by_id(self, id_abitre)
                return Match(id_match, phase, escrimeur1, escrimeur2, arbitre, heure)
            return None
        except Exception as e:
            print(e)
            return None
