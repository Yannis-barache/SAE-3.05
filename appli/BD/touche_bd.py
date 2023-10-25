from sqlalchemy.sql.expression import text
from appli.modele.touche import Touche
from appli.BD.match_bd import MatchBD
from appli.BD.escrimeur_bd import EscrimeurBD

class ToucheBD:
    def __int__(self, connexion):
        self.__connexion = connexion

    def get_all_touche(self):
        query = text("SELECT idMatch, idEscrimeur, numTouche FROM TOUCHE")
        result = self.__connexion.execute(query)
        touches = []
        for id_match, id_escrimeur, num in result:
            match = MatchBD.get_match_by_id(self, id_match)
            escrimeur = EscrimeurBD.get_escrimeur_by_id(self, id_escrimeur)
            touches.append(Touche(match, escrimeur, num))
        return touches
