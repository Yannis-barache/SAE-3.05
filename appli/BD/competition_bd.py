"""
Fichier qui contient les requêtes SQL pour la table COMPETITION
"""

import sys
import os
from sqlalchemy.sql.expression import text

from categorie_bd import CategorieBD
from equipe_bd import EquipeBD
from lieu_bd import LieuBD
from arme_bd import ArmeBD
from inscrire_bd import InscrireBD
from inscrire_arbitre_bd import InscrireArbitreBD
from match_bd import MatchBD
from poule_bd import PouleBD
from escrimeur_bd import EscrimeurBD
from phase_bd import PhaseBD
from piste_bd import PisteBD
from phase_finale_bd import PhaseFinaleBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from competition import Competition
from phase import Phase


class CompetitionBD:
    """
    Classe CompetitionBD
    """

    def __init__(self, connexion):
        self.__connexion = connexion

    def get_competition_by_id_match(self, id_match: int):
        """
        Fonction qui retourne une competition en fonction de l'id d'un match
        :param id_match: id du match
        :return: competition
        """
        try:
            query = text(
                f'SELECT idCompetition FROM PHASE natural join MATCHS WHERE idMatch = {id_match}'
            )
            result = self.__connexion.execute(query)
            for (id_competition, ) in result:
                return self.get_competition_by_id(id_competition)
            return None
        except Exception as e:
            print(e)
            return None

    def get_all_competition(self):
        """
        Fonction qui retourne toutes les competitions
        :return: liste de competition
        """
        try:
            query = text(
                'SELECT idCompetition, nomCompetition, dateCompetition, '
                'dateFinInscription, saisonCompetition,idLieu, idArme, '
                'idCategorie, coefficientCompetition, isEquipe FROM COMPETITION'
            )

            result = self.__connexion.execute(query)
            competitions = []
            print(result)
            for (id_competition, nom, date, date_fin, saison, id_lieu, id_arme,
                 id_categorie, coefficient, is_equipe) in result:
                categorie = CategorieBD(
                    self.__connexion).get_categorie_by_id(id_categorie)
                lieu = LieuBD(self.__connexion).get_lieu_by_id(id_lieu)
                arme = ArmeBD(self.__connexion).get_arme_by_id(id_arme)
                competitions.append(
                    Competition(id_competition, nom, date, date_fin, saison,
                                lieu, arme, categorie, coefficient, is_equipe))
            return competitions
        except Exception as e:
            print(e)
            return None

    def get_all_competition2(self):
        """
        Fonction qui retourne toutes les competitions
        :return: liste de competition
        """
        try:
            query = text(
                'SELECT idCompetition, nomCompetition, dateCompetition, '
                'dateFinInscription, saisonCompetition,idLieu, idArme, '
                'idCategorie, coefficientCompetition, isEquipe FROM COMPETITION'
            )
            result = self.__connexion.execute(query)
            competitions = []
            for (id_competition, nom, date, date_fin, saison, id_lieu, id_arme,
                 id_categorie, coefficient, is_equipe) in result:
                categorie = CategorieBD(
                    self.__connexion).get_categorie_by_id(id_categorie)
                lieu = LieuBD(self.__connexion).get_lieu_by_id(id_lieu)
                arme = ArmeBD(self.__connexion).get_arme_by_id(id_arme)
                nombre_escrimeurs = InscrireBD(
                    self.__connexion).get_nb_escrimeurs_competition(
                        id_competition)
                nombre_arbitres = InscrireArbitreBD(
                    self.__connexion).get_nb_arbitres_competition(
                        id_competition)
                nombre_poule = PouleBD(
                    self.__connexion).nb_poule_compet(id_competition)
                exist_phase_final = PhaseFinaleBD(
                    self.__connexion).exist_phase_finale(id_competition)
                competitions.append(
                    (Competition(id_competition, nom, date, date_fin, saison,
                                 lieu, arme, categorie, coefficient,
                                 is_equipe), nombre_escrimeurs,
                     nombre_arbitres, nombre_poule, exist_phase_final))
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
                'idCategorie, coefficientCompetition, isEquipe '
                'FROM COMPETITION NATURAL JOIN ARBITRER '
                'WHERE idEscrimeur =' + str(id_e))
            result = self.__connexion.execute(query)
            competitions = []
            for (id_competition, nom, date, date_fin, saison, id_lieu, id_arme,
                 id_categorie, coefficient, is_equipe) in result:
                categorie = CategorieBD(
                    self.__connexion).get_categorie_by_id(id_categorie)
                lieu = LieuBD(self.__connexion).get_lieu_by_id(id_lieu)
                arme = ArmeBD(self.__connexion).get_arme_by_id(id_arme)
                competitions.append(
                    Competition(id_competition, nom, date, date_fin, saison,
                                lieu, arme, categorie, coefficient, is_equipe))
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
                'idCategorie, coefficientCompetition, isEquipe FROM COMPETITION '
                'WHERE idCompetition =' + str(id_c))
            result = self.__connexion.execute(query)
            for (id_competition, nom, date, date_fin, saison, id_lieu, id_arme,
                 id_categorie, coefficient, is_equipe) in result:
                return Competition(id_competition, nom, date, date_fin, saison,
                                   id_lieu, id_arme, id_categorie, coefficient,
                                   is_equipe)
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
            competition_nom = competition.get_nom().replace("'", "''")
            query = text(
                f"INSERT INTO COMPETITION (nomCompetition, dateCompetition, "
                f"dateFinInscription, saisonCompetition,idLieu, idArme, "
                f"idCategorie, coefficientCompetition, isEquipe) VALUES "
                f"('{competition_nom}', '{competition.get_date()}', "
                f"'{competition.get_date_fin_inscription()}', "
                f"'{competition.get_saison()}', {competition.get_lieu().get_id()}, "
                f"{competition.get_arme().get_id()}, "
                f"{competition.get_categorie().get_id()}, {competition.get_coefficient()}, {competition.get_is_equipe()}"
            )
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None

    def delete_competition(self, id_comp: int):
        """
        Fonction qui supprime une competition
        :param id_comp: id de la competition
        """
        try:
            query = text(
                f"DELETE FROM COMPETITION WHERE idCompetition = {id_comp}")
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None

    def update_competition(self, competition: Competition):
        """
        Fonction qui met à jour une competition
        :param competition: competition
        """
        try:
            query = text(
                f"UPDATE COMPETITION SET nomCompetition = '{competition.get_nom()}', "
                f"dateCompetition = '{competition.get_date()}', "
                f"dateFinInscription = '{competition.get_date_fin_inscription()}', "
                f"saisonCompetition = '{competition.get_saison()}', "
                f"idLieu = {competition.get_lieu().get_id()}, "
                f"idArme = {competition.get_arme().get_id()}, "
                f"idCategorie = {competition.get_categorie().get_id()}, "
                f"coefficientCompetition = {competition.get_coefficient()}, "
                f"isEquipe = {competition.get_is_equipe()}"
                f"WHERE idCompetition = {competition.get_id()}")
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

    def generate_poule_compet(self, id_compet: int, heure_debut: float):
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
                    matchs = poule.generer_matchs(poules.get(poule),
                                                  heure_debut)
                    for match in matchs:
                        match_bd.insert_match(match)
            return poules
        except Exception as e:
            print(e)
            return None

    def generate_phase_finale(self, id_compet: int, heure_debut: float):
        """
        Fonction qui permet de générer la phase finale d'une compétition

        Args:
            id_compet (int): id de la compétition
        
        Returns:
            int: id de la phase finale
        """
        comp = self.get_competition_by_id(id_compet)
        if not comp.get_is_equipe():
            try:
                escrimeur_bd = EscrimeurBD(self.__connexion)
                les_poules = PouleBD(
                    self.__connexion).get_poules_by_compet(id_compet)
                les_inscriptions_arbitres = InscrireArbitreBD(
                    self.__connexion).get_arbitre_by_id_competition(id_compet)
                les_arbitres = []
                for inscrire in les_inscriptions_arbitres:
                    les_arbitres.append(
                        escrimeur_bd.get_escrimeur_by_id(
                            inscrire.get_id_escrimeur()))
                les_pistes = PisteBD(
                    self.__connexion).get_pistes_by_id_competition(
                        comp.get_lieu().get_id())
                phase_finale, les_matchs = Competition.generer_phase_finale(
                    les_poules, les_arbitres, heure_debut, les_pistes)
                phase = Phase(-1, id_compet)
                id_phase = PhaseBD(self.__connexion).insert_phase(phase)
                phase_finale.set_id_phase_f(id_phase)
                PhaseFinaleBD(
                    self.__connexion).insert_phase_finale(phase_finale)
                for match in les_matchs:
                    match.set_id_phase(id_phase)
                    MatchBD(self.__connexion).insert_match(match)
                return id_phase
            except Exception as e:
                print(e)
                return None
        else:
            try:
                escrimeur_bd = EscrimeurBD(self.__connexion)
                equipe_bd = EquipeBD(self.__connexion)
                les_equipes = equipe_bd.get_all_equipe_by_competition(
                    id_compet)
                les_inscriptions_arbitres = InscrireArbitreBD(
                    self.__connexion).get_arbitre_by_id_competition(id_compet)
                les_arbitres = []
                for inscrire in les_inscriptions_arbitres:
                    les_arbitres.append(
                        escrimeur_bd.get_escrimeur_by_id(
                            inscrire.get_id_escrimeur()))
                les_pistes = PisteBD(
                    self.__connexion).get_pistes_by_id_competition(
                        comp.get_lieu().get_id())
                phase_finale, les_matchs = Competition.generer_phase_finale_equipe(
                    les_equipes, les_arbitres, heure_debut, les_pistes)
                phase = Phase(-1, id_compet)
                id_phase = PhaseBD(self.__connexion).insert_phase(phase)
                phase_finale.set_id_phase_f(id_phase)
                PhaseFinaleBD(
                    self.__connexion).insert_phase_finale(phase_finale)
                for match in les_matchs:
                    match.set_id_phase(id_phase)
                    MatchBD(self.__connexion).insert_match(match)
                return id_phase
            except Exception as e:
                print(e)
                return None

    def get_competition_by_phase(self, id_phase) -> Competition | None:
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
            return None
        except Exception as e:
            print(e)
            return None

    def get_competition_equipe(self):
        try:
            query = text(
                'SELECT idCompetition, nomCompetition, dateCompetition, '
                'dateFinInscription, saisonCompetition,idLieu, idArme, '
                'idCategorie, coefficientCompetition, isEquipe FROM COMPETITION'
                ' where isEquipe=1'
            )

            result = self.__connexion.execute(query)
            competitions = []
            for (id_competition, nom, date, date_fin, saison, id_lieu, id_arme,
                 id_categorie, coefficient, is_equipe) in result:
                categorie = CategorieBD(
                    self.__connexion).get_categorie_by_id(id_categorie)
                lieu = LieuBD(self.__connexion).get_lieu_by_id(id_lieu)
                arme = ArmeBD(self.__connexion).get_arme_by_id(id_arme)
                competition =Competition(id_competition, nom, date, date_fin, saison,
                                lieu, arme, categorie, coefficient, is_equipe)
                competitions.append(competition)
            return competitions
        except Exception as e:
            print(e)
            return None

if __name__ == "__main__":
    from modele_appli import ModeleAppli
    modele = ModeleAppli()
    competitions = modele.get_competition_bd()
    competitions.generate_poule_compet(8, 10)
