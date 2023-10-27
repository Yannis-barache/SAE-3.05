"""
Fichier qui contient les requêtes SQL pour la table COMPETITION
"""

from sqlalchemy.sql.expression import text
from appli.modele.competition import Competition
from appli.BD.categorie_bd import CategorieBD
from appli.BD.lieu_bd import LieuBD
from appli.BD.arme_bd import ArmeBD


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
                "SELECT idCompetition, nomCompetition, dateCompetition, "
                "dateFinInscription, saisonCompetition,idLieu, idArme, "
                "idCategorie, coefficientCompetition FROM COMPETITION")
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

    def get_competition_by_id(self, id_c: int):
        """
        Fonction qui retourne une competition en fonction de son id
        :param id_c: id de la competition
        :return: competition
        """
        try:
            query = text(
                "SELECT idCompetition, nomCompetition, dateCompetition, "
                "dateFinInscription, saisonCompetition,idLieu, idArme, "
                "idCategorie, coefficientCompetition FROM COMPETITION "
                "WHERE idCompetition =" + str(id_c))
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
