"""
Fichier qui contient les requêtes SQL pour la table COMPETITION
"""

import sys
import os
from sqlalchemy.sql.expression import text
from categorie_bd import CategorieBD
from lieu_bd import LieuBD
from arme_bd import ArmeBD
from inscrire_bd import InscrireBD
from inscrire_arbitre_bd import InscrireArbitreBD
from match_bd import MatchBD
from poule_bd import PouleBD
from escrimeur_bd import EscrimeurBD
from phase_bd import PhaseBD
from piste_bd import PisteBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from competition import Competition
from match import Match
from phase import Phase


class CompetitionBD:
    """
    Classe CompetitionBD
    """

    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_competition(self):
        """
        Fonction qui retourne toutes les competitions
        :return: liste de competition
        """
        try:
            query = text(
                'SELECT idCompetition, nomCompetition, dateCompetition, '
                'dateFinInscription, saisonCompetition,idLieu, idArme, '
                'idCategorie, coefficientCompetition FROM COMPETITION')

            result = self.__connexion.execute(query)
            competitions = []
            for (id_competition, nom, date, date_fin, saison, id_lieu, id_arme,
                 id_categorie, coefficient) in result:
                categorie = CategorieBD(
                    self.__connexion).get_categorie_by_id(id_categorie)
                lieu = LieuBD(self.__connexion).get_lieu_by_id(id_lieu)
                arme = ArmeBD(self.__connexion).get_arme_by_id(id_arme)
                competitions.append(
                    Competition(id_competition, nom, date, date_fin, saison,
                                lieu, arme, categorie, coefficient))
            return competitions
        except Exception as e:
            print(e)
            return None

    def get_all_matchs(self, id_competition: int):
        query = text("SELECT * FROM MATCHS WHERE IDPHASE IN ( SELECT IDPHASE FROM PHASE WHERE IDCOMPETITION="+str(id_competition)+")")
        result = self.__connexion.execute(query)

        matchs = []
        for (id_match, id_tireur1, id_tireur2, id_phase, id_arbitre,id_piste, heure_match, fini) in result:
            escrimeur_n1 = EscrimeurBD(self.__connexion).get_escrimeur_by_id(id_tireur1)
            escrimeur_n2 = EscrimeurBD(self.__connexion).get_escrimeur_by_id(id_tireur2)
            arbitre = EscrimeurBD(self.__connexion).get_escrimeur_by_id(id_arbitre)
            piste = PisteBD(self.__connexion).get_piste_by_id(id_piste)
            matchs.append(Match(id_match,id_phase, escrimeur_n1, escrimeur_n2, arbitre, heure_match, fini,piste))

        return matchs


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
                'idCategorie, coefficientCompetition FROM COMPETITION '
                'WHERE idCompetition =' + str(id_c))
            result = self.__connexion.execute(query)
            for (id_competition, nom, date, date_fin, saison, id_lieu, id_arme,
                 id_categorie, coefficient) in result:
                categorie = CategorieBD(
                    self.__connexion).get_categorie_by_id(id_categorie)
                lieu = LieuBD(self.__connexion).get_lieu_by_id(id_lieu)
                arme = ArmeBD(self.__connexion).get_arme_by_id(id_arme)
                return Competition(id_competition, nom, date, date_fin, saison,
                                   lieu, arme, categorie, coefficient)
            return None
        except Exception as e:
            print(e)
            return None

    def get_competition_by_arbitre(self, id_e: int):
        """
        Fonction qui retourne une competition en fonction de son id
        :param id_e: id de l'escrimeur
        :return: competition
        """
        try:
            query = text(
                  'SELECT idCompetition, nomCompetition, dateCompetition, '
                'dateFinInscription, saisonCompetition,idLieu, idArme, '
                'idCategorie, coefficientCompetition '
                'FROM COMPETITION NATURAL JOIN ARBITRER '
                'WHERE idEscrimeur =' + str(id_e))
            result = self.__connexion.execute(query)
            competitions = []
            for (id_competition, nom, date, date_fin, saison, id_lieu, id_arme,
                 id_categorie, coefficient) in result:
                categorie = CategorieBD(
                    self.__connexion).get_categorie_by_id(id_categorie)
                lieu = LieuBD(self.__connexion).get_lieu_by_id(id_lieu)
                arme = ArmeBD(self.__connexion).get_arme_by_id(id_arme)
                competitions.append(Competition(id_competition, nom, date, date_fin, saison,
                                   lieu, arme, categorie, coefficient))
            return competitions
        except Exception as e:
            print(e)
            return None

    def get_competition_by_id_s(self, id_c: int):
        """
        Fonction qui retourne une competition en fonction de son id sans les objets
        :param id_c: id de la competition
        :return: competition
        """
        try:
            query = text(
                'SELECT idCompetition, nomCompetition, dateCompetition, '
                'dateFinInscription, saisonCompetition,idLieu, idArme, '
                'idCategorie, coefficientCompetition FROM COMPETITION '
                'WHERE idCompetition =' + str(id_c))
            result = self.__connexion.execute(query)
            for (id_competition, nom, date, date_fin, saison, id_lieu, id_arme,
                 id_categorie, coefficient) in result:
                return Competition(id_competition, nom, date, date_fin, saison,
                                   id_lieu, id_arme, id_categorie, coefficient)
            return None
        except Exception as e:
            print(e)
            return None

    def insert_competition(self, competition: Competition):
        """
        Fonction qui insère une competition
        :param competition : competition
        """
        try:
            query = text(
                f"INSERT INTO COMPETITION (nomCompetition, dateCompetition, "
                f"dateFinInscription, saisonCompetition,idLieu, idArme, "
                f"idCategorie, coefficientCompetition) VALUES "
                f"('{competition.get_nom()}', '{competition.get_date()}', "
                f"'{competition.get_date_fin_inscription()}', "
                f"'{competition.get_saison()}', {competition.get_lieu().get_id()}, "
                f"{competition.get_arme().get_id()}, "
                f"{competition.get_categorie().get_id()}, {competition.get_coefficient()})"
            )
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None

    def delete_competition_by_name(self, cometition: Competition):
        """
        Fonction qui supprime une competition en fonction de son nom
        :param nom: nom de la competition
        """
        try:
            query = text(
                f"DELETE FROM COMPETITION WHERE nomCompetition = '{cometition.get_nom()}'"
            )
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None

    def generate_poule_compet(self, id_compet: int):
        """
        Fonction qui génère les poules d'une compétition
        :param id_compet: id de la compétition
        """
        try:
            inscire_bd = InscrireBD(self.__connexion)
            inscrire_arbitre = InscrireArbitreBD(self.__connexion)
            match_bd = MatchBD(self.__connexion)
            poule_bd = PouleBD(self.__connexion)
            phase_bd = PhaseBD(self.__connexion)
            escrimeur_bd = EscrimeurBD(self.__connexion)
            piste_bd = PisteBD(self.__connexion)
            la_compet = self.get_competition_by_id(id_compet)
            les_inscriptions = inscire_bd.get_all_inscrit_compet(la_compet)
            les_escrimeurs = []
            for inscrire in les_inscriptions:
                les_escrimeurs.append(
                    escrimeur_bd.get_escrimeur_by_id(
                        inscrire.get_id_escrimeur()))
            les_inscriptions_arbitres = inscrire_arbitre.get_arbitre_by_competition(
                la_compet)
            les_arbitres = []
            for inscrire in les_inscriptions_arbitres:
                les_arbitres.append(
                    escrimeur_bd.get_escrimeur_by_id(
                        inscrire.get_id_escrimeur()))
            poules = Competition.generation_poule(les_escrimeurs, les_arbitres)
            les_pistes = piste_bd.get_piste_by_lieu(la_compet.get_lieu())
            if poules is not None:
                for poule in poules:
                    phase = Phase(-1, id_compet)
                    id_phase = phase_bd.insert_phase(phase)
                    poule.set_id(id_phase)
                    poule.set_les_pistes(les_pistes)
                    poule_bd.insert_poule(poule)
                    matchs = poule.generer_matchs(poules.get(poule), 10.5)
                    for match in matchs:
                        match_bd.insert_match(match)
            return poules
        except Exception as e:
            print(e)
            return None
