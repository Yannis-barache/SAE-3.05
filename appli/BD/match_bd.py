'''
Fichier qui contient les requêtes SQL pour la table MATCHS
'''

import sys
import os
from sqlalchemy import text
from phase_bd import PhaseBD
from escrimeur_bd import EscrimeurBD
from inscrire_arbitre_bd import InscrireArbitreBD

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
                         'idEscrimeur2, idArbitre, heureMatch, '
                         'fini FROM MATCHS')
            result = self.__connexion.execute(query)
            matchs = []
            for (id_match, id_phase, id_escrimeur1, id_escrimeur2, id_arbitre,
                 heure, fini) in result:
                fini = fini == 1
                phase = PhaseBD(self.__connexion).get_phase_by_id(id_phase)
                escrimeur1 = EscrimeurBD(
                    self.__connexion).get_escrimeur_by_id(id_escrimeur1)
                escrimeur2 = EscrimeurBD(
                    self.__connexion).get_escrimeur_by_id(id_escrimeur2)
                arbitre = InscrireArbitreBD(
                    self.__connexion).get_arbitre_by_id(id_arbitre)
                matchs.append(
                    Match(id_match, phase, escrimeur1, escrimeur2, arbitre,
                          heure, fini))
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
                'idArbitre, heureMatch, fini FROM MATCHS '
                'WHERE idMatch = ' + str(id_m))
            result = self.__connexion.execute(query)
            for (id_match, id_phase, id_escrimeur1, id_escrimeur2, id_arbitre,
                 heure, fini) in result:
                fini = fini == 1
                phase = PhaseBD(self.__connexion).get_phase_by_id(id_phase)
                escrimeur1 = EscrimeurBD(
                    self.__connexion).get_escrimeur_by_id(id_escrimeur1)
                escrimeur2 = EscrimeurBD(
                    self.__connexion).get_escrimeur_by_id(id_escrimeur2)
                arbitre = InscrireArbitreBD(
                    self.__connexion).get_arbitre_by_id(id_arbitre)
                return Match(id_match, phase, escrimeur1, escrimeur2, arbitre,
                             heure, fini)
            return None
        except Exception as e:
            print(e)
            return None
