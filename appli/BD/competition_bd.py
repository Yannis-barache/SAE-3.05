from appli.modele.competition import Competition
from sqlalchemy.sql.expression import text
from appli.BD.categorie_bd import CategorieBD
from appli.BD.lieu_bd import LieuBD
from appli.BD.arme_bd import ArmeBD


class CompetitionBD:
    def __int__(self, connexion):
        self.__connexion = connexion

    def get_all_competition(self):
        query = text("SELECT idCompetition, nomCompetition, dateCompetition, dateFinInscription, "
                     "saisonCompetition,idLieu, idArme, idCategorie,"
                     "coefficientCompetition FROM COMPETITION")
        result = self.__connexion.execute(query)
        competitions = []
        for id_competition, nom, date, date_fin, saison, id_lieu, id_arme, id_categorie, coefficient in result:
            categorie = CategorieBD.get_categorie_by_id(self, id_categorie)
            lieu = LieuBD.get_lieu_by_id(self, id_lieu)
            arme = ArmeBD.get_arme_by_id(self, id_arme)
            competitions.append(Competition(id_competition, nom, date, date_fin, saison, lieu, arme, categorie, coefficient))
        return competitions


    def get_competition_by_id(self, id):
        query = text("SELECT idCompetition, nomCompetition, dateCompetition, dateFinInscription, "
                     "saisonCompetition,idLieu, idArme, idCategorie,"
                     "coefficientCompetition FROM COMPETITION WHERE idCompetition = :id")
        result = self.__connexion.execute(query, id=id)
        for id_competition, nom, date, date_fin, saison, id_lieu, id_arme, id_categorie, coefficient in result:
            categorie = CategorieBD.get_categorie_by_id(self, id_categorie)
            lieu = LieuBD.get_lieu_by_id(self, id_lieu)
            arme = ArmeBD.get_arme_by_id(self, id_arme)
            return Competition(id_competition, nom, date, date_fin, saison, lieu, arme, categorie, coefficient)
        return None
