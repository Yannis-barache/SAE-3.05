'''
Fichier qui contient les requêtes SQL pour la table MATCHS
'''

import sys
import os
from sqlalchemy import text
from arme_bd import ArmeBD
from categorie_bd import CategorieBD
from competition import Competition
from equipe_bd import EquipeBD
from lieu_bd import LieuBD
from phase_bd import PhaseBD
from escrimeur_bd import EscrimeurBD
from inscrire_arbitre_bd import InscrireArbitreBD
from piste_bd import PisteBD

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
                match = Match(id_match, phase.get_id_phase(), escrimeur1,
                              escrimeur2, arbitre, heure, fini, piste)
                return match
            return None
        except Exception as e:
            print(e)
            return None

    def get_competition_by_phase(self, id_phase) -> Competition:
        """
        Fonction qui retourne une compétition en fonction de la phase
        :param id_phase: id de la phase
        :return: compétition
        """
        try:
            query = text(
                f'SELECT idCompetition FROM PHASE WHERE idPhase = {id_phase}')
            result = self.__connexion.execute(query)
            for (id_competition, ) in result:
                return self.get_competition_by_id(id_competition)
        except Exception as e:
            print(e)
            return None

    def get_competition_by_id(self, id_c: int):
        """
        Fonction qui retourne une competition en fonction de son id
        :param id_c: id de la competition
        :return: competition
        """
        try:
            query = text(
                'SELECT idCompetition, nomCompetition, dateCompetition, '
                'dateFinInscription, saisonCompetition,idLieu, idArme, '
                'idCategorie, coefficientCompetition, isEquipe FROM COMPETITION '
                'WHERE idCompetition =' + str(id_c))
            result = self.__connexion.execute(query)
            for (id_competition, nom, date, date_fin, saison, id_lieu, id_arme,
                 id_categorie, coefficient, is_equipe) in result:
                categorie = CategorieBD(
                    self.__connexion).get_categorie_by_id(id_categorie)
                lieu = LieuBD(self.__connexion).get_lieu_by_id(id_lieu)
                arme = ArmeBD(self.__connexion).get_arme_by_id(id_arme)
                return Competition(id_competition, nom, date, date_fin, saison,
                                   lieu, arme, categorie, coefficient,
                                   is_equipe)
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
            comp = self.get_competition_by_phase(id_p)
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
                if not comp.get_is_equipe() :
                    escrimeur1 = EscrimeurBD(
                        self.__connexion).get_escrimeur_by_id(id_escrimeur1)
                    escrimeur2 = EscrimeurBD(
                        self.__connexion).get_escrimeur_by_id(id_escrimeur2)
                else:
                    escrimeur1 = EquipeBD(self.__connexion).get_equipe_by_id(id_escrimeur1)
                    escrimeur2 = EquipeBD(self.__connexion).get_equipe_by_id(id_escrimeur2)
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

    def set_fini_match(self, match: Match):
        """
        Fonction qui met le match en fini
        :param match : match
        """
        try:
            if match.est_finis():
                return None
            query = text(
                f"UPDATE MATCHS SET fini = 1 WHERE idMatch = {str(match.get_id())}"
            )
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None

    def set_finis_match_2(self, id_match: int):
        """
        Fonction qui met le match en fini
        :param match : match
        """
        try:
            query = text(
                f"UPDATE MATCHS SET fini = 1 WHERE idMatch = {str(id_match)}")
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None

    def get_id_competition_du_match(self, match: Match):
        """
        Fonction qui retourne l'ID de la compétition du match
        :param match : match
        """
        try:
            query = text(
                f"SELECT idCompetition FROM MATCHS NATURAL JOIN PHASE WHERE idMatch = {match.get_id()}"
            )
            result = self.__connexion.execute(query)

            id_competition = result.fetchone()
            for ele in id_competition:
                print(ele)

            if id_competition:
                return int(id_competition[0])
            else:
                return None

        except Exception as e:
            print(e)
            return None

    def get_type_phase(self, match: Match):
        """
        Fonction qui retourne le type de la phase du match
        :param match : match
        """
        try:
            query = text(
                f"SELECT count(*) FROM POULE WHERE idPoule = {match.get_id_phase()}"
            )
            result = self.__connexion.execute(query)
            if result.fetchone()[0] == 1:
                return 1
            else:
                return 2
        except Exception as e:
            print(e)
            return None
