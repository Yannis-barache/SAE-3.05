"""
    Fichier qui contient les requêtes SQL pour la table PHASE_FINALE
"""

import sys
import os
from sqlalchemy import text
from escrimeur_bd import EscrimeurBD
from inscrire_arbitre_bd import InscrireArbitreBD

from piste_bd import PisteBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from phase_final import PhaseFinal

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/BD'))

from match_bd import MatchBD
from touche_bd import ToucheBD


class PhaseFinaleBD:
    """
    Classe PhaseFinaleBD
    """

    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_phase_final(self):
        """
        Fonction qui retourne toutes les phases finales
        :return: liste de phase finale
        """
        try:
            query = text('SELECT idPhaseFinale FROM PHASE_FINALE')
            result = self.__connexion.execute(query)
            phase_finals = []
            for id_phase_finale in result:
                phase_finals.append(PhaseFinal(id_phase_finale))
            return phase_finals
        except Exception as e:
            print(e)
            return None

    def get_phase_finale_by_compet(self, id_compet: int):
        """
        Fonction qui retourne la phase finale d'une compétition
        :param id_compet: id de la compétition
        :return: phase finale
        """
        try:
            query = text(
                f'SELECT idPhaseFinale FROM PHASE_FINALE JOIN PHASE on PHASE.idPhase = PHASE_FINALE.idPhaseFinale WHERE idCompetition = {id_compet}'
            )
            result = self.__connexion.execute(query)
            for (id_phase_finale, ) in result:
                p = PhaseFinal(id_phase_finale)
                match_bd = MatchBD(self.__connexion)
                toucher_bd = ToucheBD(self.__connexion)
                piste_bd = PisteBD(self.__connexion)
                les_pistes = piste_bd.get_pistes_by_id_competition(id_compet)
                les_matchs = match_bd.get_match_by_phase(id_phase_finale)
                for m in les_matchs:
                    les_touches = toucher_bd.get_touches_by_id_match(
                        m.get_id())
                    m.set_touche(les_touches)
                p.set_les_matchs(les_matchs)
                p.set_les_pistes(les_pistes)
                return p
        except Exception as e:
            print(e)
            return None

    def get_phase_finale_bd_by_id(self, id_phase_finalee: int):
        """
        Fonction qui retourne la phase finale d'une compétition
        :param id_compet: id de la compétition
        :return: phase finale
        """
        try:
            query = text(
                f'SELECT idPhaseFinale FROM PHASE_FINALE WHERE idPhaseFinale = {id_phase_finalee}'
            )
            result = self.__connexion.execute(query)
            for (id_phase_finale, ) in result:
                p = PhaseFinal(id_phase_finale)
                match_bd = MatchBD(self.__connexion)
                toucher_bd = ToucheBD(self.__connexion)
                les_matchs = match_bd.get_match_by_phase(id_phase_finale)
                for m in les_matchs:
                    les_touches = toucher_bd.get_touches_by_id_match(
                        m.get_id())
                    m.set_touche(les_touches)
                p.set_les_matchs(les_matchs)
                return p
        except Exception as e:
            print(e)
            return None

    def insert_phase_finale(self, phase_finale: PhaseFinal):
        """
        Fonction qui insère une phase finale
        """
        try:
            if phase_finale.get_id_phase_f(
            ) is None or phase_finale.get_id_phase_f() == -1:
                return None
            query = text("INSERT INTO PHASE_FINALE (idPhaseFinale) VALUES (" +
                         str(phase_finale.get_id_phase_f()) + ")")
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None

    def delete_phase_finale(self, phase_finale: PhaseFinal):
        """
        Fonction qui supprime une phase finale
        """
        try:
            if phase_finale.get_id_phase_f(
            ) is None or phase_finale.get_id_phase_f() == -1:
                return None
            query = text("DELETE FROM PHASE_FINALE WHERE idPhaseFinale = " +
                         str(phase_finale.get_id_phase_f()))
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None

    def exist_phase_finale(self, id_compet: int):
        """
        Fonction qui vérifie si il existe une phase finale pour une compétition
        
        Args:
            id_compet (int) : id de la compétition
        """
        try:
            query = text(
                f'SELECT idPhaseFinale FROM PHASE_FINALE JOiN PHASE on PHASE.idPhase = PHASE_FINALE.idPhaseFinale WHERE idCompetition = {id_compet}'
            )
            result = self.__connexion.execute(query)
            return result.rowcount > 0
        except Exception as e:
            print(e)
            return None

    def get_phase_finale_by_competition(self, id_compet: int):
        """
        Fonction qui retourne une phase finale pour une compétition

        Args :
            id_compet (int) : id de la compétition
        """
        try:
            query = text(
                f'SELECT idPhaseFinale FROM PHASE_FINALE JOiN PHASE on PHASE.idPhase = PHASE_FINALE.idPhaseFinale WHERE idCompetition = {id_compet}'
            )
            result = self.__connexion.execute(query)
            for (id_phase_finale, ) in result:
                return id_phase_finale

    def generer_tour_suivant(self, phase_finale: PhaseFinal, id_compet: int,
                             heure_debut: float):
        """
        Fonction qui génère le tour suivant d'une phase finale
        """
        try:
            escrimeur_bd = EscrimeurBD(self.__connexion)
            match_bd = MatchBD(self.__connexion)
            les_inscriptions_arbitres = InscrireArbitreBD(
                self.__connexion).get_arbitre_by_id_competition(id_compet)
            les_arbitres = []
            for inscrire in les_inscriptions_arbitres:
                les_arbitres.append(
                    escrimeur_bd.get_escrimeur_by_id(
                        inscrire.get_id_escrimeur()))
            les_matchs = phase_finale.generer_tour_suivant(
                les_arbitres, heure_debut)
            for m in les_matchs:
                match_bd.insert_match(m)
        except Exception as e:
            print(e)
            return None
