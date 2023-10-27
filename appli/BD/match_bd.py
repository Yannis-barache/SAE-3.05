"""
Fichier qui contient les requêtes SQL pour la table MATCHS
"""

from sqlalchemy import text
from appli.modele.match import Match
from appli.BD.phase_bd import PhaseBD
from appli.BD.escrimeur_bd import EscrimeurBD
from appli.BD.inscrire_arbitre_bd import InscrireArbitreBD


class MatchBD:
    """
    Classe MatchBD
    """
    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_match(self):
        """
        Fonction qui retourne tous les matchs
        :return: liste de Match
        """
        try:
            query = text("SELECT idMatch, idPhase, idEscrimeur1, "
                         "idEscrimeur2, idArbitre, heureMatch, "
                         "fini FROM MATCHS")
            result = self.__connexion.execute(query)
            matchs = []
            for (id_match, id_phase, id_escrimeur1, id_escrimeur2, id_arbitre,
                 heure, fini) in result:

                if fini == 1:
                    fini = True
                else:
                    fini = False

                phase = PhaseBD(self.__connexion).get_phase_by_id(id_phase)
                escrimeur1 = EscrimeurBD(self.__connexion).get_escrimeur_by_id(id_escrimeur1)
                escrimeur2 = EscrimeurBD(self.__connexion).get_escrimeur_by_id(id_escrimeur2)
                arbitre = InscrireArbitreBD(self.__connexion).get_arbitre_by_id(id_arbitre)

                matchs.append(Match(id_match, phase, escrimeur1, escrimeur2,
                                    arbitre, heure, fini))
            return matchs
        except Exception as e:
            print(e)
            return None


    def get_match_by_id(self, id_m: int):
        """
        Fonction qui retourne un match en fonction de son id
        :param id_m: id du match
        :return: match
        """
        try:
            query = text("SELECT idMatch, idPhase, idEscrimeur1, idEscrimeur2, "
                         "idArbitre, heureMatch, fini FROM MATCHS "
                         "WHERE idMatch = " + str(id_m))
            result = self.__connexion.execute(query)
            for (id_match, id_phase, id_escrimeur1, id_escrimeur2, id_arbitre,
                 heure, fini) in result:

                if fini == 1:
                    fini = True
                else:
                    fini = False

                phase = PhaseBD(self.__connexion).get_phase_by_id(id_phase)
                escrimeur1 = EscrimeurBD(self.__connexion).get_escrimeur_by_id(id_escrimeur1)
                escrimeur2 = EscrimeurBD(self.__connexion).get_escrimeur_by_id(id_escrimeur2)
                arbitre = InscrireArbitreBD(self.__connexion).get_arbitre_by_id(id_arbitre)

                return Match(id_match, phase, escrimeur1, escrimeur2, arbitre, heure, fini)
            return None
        except Exception as e:
            print(e)
            return None

    def insert_match(self, match: Match):
        """
        Fonction qui insère un match
        :param match : match
        """
        try:
            query = text(f"INSERT INTO MATCHS (idPhase, idEscrimeur1, "
                         f"idEscrimeur2, idArbitre, heureMatch, fini) VALUES "
                         f"({str(match.get_id_phase())},"
                         f"{str(match.get_escrimeur1())},{str(match.get_escrimeur2())},"
                         f"{str(match.get_arbitre())},'{match.get_heure()}',"
                         f"{str(match.get_fini())})")
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None
