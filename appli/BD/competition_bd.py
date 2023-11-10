"""
Fichier qui contient les requêtes SQL pour la table COMPETITION
"""

import sys
import os
from sqlalchemy.sql.expression import text
from categorie_bd import CategorieBD
from lieu_bd import LieuBD
from arme_bd import ArmeBD
from escrimeur_bd import EscrimeurBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from competition import Competition
from match import Match


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
        for (id_match, id_tireur1, id_tireur2, id_phase, idArbitre,idPiste, heureMatch, fini ) in result:
            Escrimeur1 = EscrimeurBD(self.__connexion).get_escrimeur_by_id(id_tireur1)
            Escrimeur2 = EscrimeurBD(self.__connexion).get_escrimeur_by_id(id_tireur2)
            arbitre = EscrimeurBD(self.__connexion).get_escrimeur_by_id(idArbitre)
            matchs.append(Match(id_match,id_phase, Escrimeur1, Escrimeur2, arbitre, heureMatch, fini))
        
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
