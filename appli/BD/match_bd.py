'''
Fichier qui contient les requêtes SQL pour la table MATCHS
'''

import sys
import os
from sqlalchemy import text
from phase_bd import PhaseBD
from escrimeur_bd import EscrimeurBD
from inscrire_arbitre_bd import InscrireArbitreBD
from piste_bd import PisteBD
from touche_bd import ToucheBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from match import Match


class MatchBD:
    '''
    Classe MatchBD
    '''

    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_match(self):
        '''
        Fonction qui retourne tous les matchs
        :return: liste de Match
        '''
        try:
            query = text('SELECT idMatch, idPhase, idEscrimeur1, '
                         'idEscrimeur2, idArbitre, idPiste, heureMatch, '
                         'fini FROM MATCHS')
            result = self.__connexion.execute(query)
            matchs = []
            for (id_match, id_phase, id_escrimeur1, id_escrimeur2, id_arbitre,
                 id_piste, heure, fini) in result:
                fini = fini == 1
                phase = PhaseBD(self.__connexion).get_phase_by_id(id_phase)
                escrimeur1 = EscrimeurBD(
                    self.__connexion).get_escrimeur_by_id(id_escrimeur1)
                escrimeur2 = EscrimeurBD(
                    self.__connexion).get_escrimeur_by_id(id_escrimeur2)
                arbitre = InscrireArbitreBD(
                    self.__connexion).get_arbitre_by_id(id_arbitre)
                piste = PisteBD(self.__connexion).get_piste_by_id(id_piste)
                matchs.append(
                    Match(id_match, phase, escrimeur1, escrimeur2, arbitre,
                          heure, fini, piste))
            return matchs
        except Exception as e:
            print(e)
            return None

    def get_match_by_id(self, id_m: int):
        '''
        Fonction qui retourne un match en fonction de son id
        :param id_m: id du match
        :return: match
        '''
        try:
            query = text(
                'SELECT idMatch, idPhase, idEscrimeur1, idEscrimeur2, '
                'idArbitre, idPiste, heureMatch, fini FROM MATCHS '
                'WHERE idMatch = ' + str(id_m))
            result = self.__connexion.execute(query)
            for (id_match, id_phase, id_escrimeur1, id_escrimeur2, id_arbitre,
                 id_piste, heure, fini) in result:
                fini = fini == 1
                phase = PhaseBD(self.__connexion).get_phase_by_id(id_phase)
                escrimeur1 = EscrimeurBD(
                    self.__connexion).get_escrimeur_by_id(id_escrimeur1)
                escrimeur2 = EscrimeurBD(
                    self.__connexion).get_escrimeur_by_id(id_escrimeur2)
                arbitre = EscrimeurBD(
                    self.__connexion).get_escrimeur_by_id(id_arbitre)
                piste = PisteBD(self.__connexion).get_piste_by_id(id_piste)
                match = Match(id_match, phase, escrimeur1, escrimeur2, arbitre,
                              heure, fini, piste)
                match.set_touche(ToucheBD(self.__connexion).get_by_match(match))
                return match
            return None
        except Exception as e:
            print(e)
            return None

    def get_match_by_phase(self, id_p: int):
        '''
        Fonction qui retourne les matchs en fonction de la phase
        :param id_p: id de la phase
        :return: liste de match
        '''
        try:
            query = text(
                'SELECT idMatch, idPhase, idEscrimeur1, idEscrimeur2, '
                'idArbitre, idPiste, heureMatch, fini FROM MATCHS '
                'WHERE idPhase = ' + str(id_p))
            result = self.__connexion.execute(query)
            matchs = []
            for (id_match, id_phase, id_escrimeur1, id_escrimeur2, id_arbitre,
                 id_piste, heure, fini) in result:
                fini = fini == 1
                phase = PhaseBD(self.__connexion).get_phase_by_id(id_phase)
                escrimeur1 = EscrimeurBD(
                    self.__connexion).get_escrimeur_by_id(id_escrimeur1)
                escrimeur2 = EscrimeurBD(
                    self.__connexion).get_escrimeur_by_id(id_escrimeur2)
                arbitre = EscrimeurBD(
                    self.__connexion).get_escrimeur_by_id(id_arbitre)
                piste = PisteBD(self.__connexion).get_piste_by_id(id_piste)
                matchs.append(
                    Match(id_match, phase, escrimeur1, escrimeur2, arbitre,
                          heure, fini, piste))
            return matchs
        except Exception as e:
            print(e)
            return None

    def insert_match(self, match: Match):
        """
        Fonction qui insère un match
        :param match : match
        """
        try:
            query = text(
                f"INSERT INTO MATCHS (idPhase, idEscrimeur1, "
                f"idEscrimeur2, idArbitre, idPiste, heureMatch, fini) VALUES "
                f"({str(match.get_id_phase())},"
                f"{str(match.get_escrimeur1().get_id())},{str(match.get_escrimeur2().get_id())},"
                f"{str(match.get_arbitre().get_id())}, {str(match.get_piste().get_id_piste())},"
                f"'{match.get_heure()}', {str(int(match.est_finis()))})")
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None

    def delete_match_by_arbitre(self, id_arbitre: int):
        """
        Fonction qui supprime un match en fonction de l'arbitre
        :param id_arbitre : id de l'arbitre
        """
        try:
            query = text(
                f"DELETE FROM MATCHS WHERE idArbitre = {str(id_arbitre)}")
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None
