from sqlalchemy import text
from appli.modele.phase_final import PhaseFinal

class PhaseFinaleBD:
    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_phase_final(self):
        try:
            query = text("SELECT idPhaseFinale FROM PHASE_FINALE")
            result = self.__connexion.execute(query)
            phase_finals = []
            for id_phase_finale in result:
                phase_finals.append(PhaseFinal(id_phase_finale))
            return phase_finals
        except Exception as e:
            print(e)
            return None