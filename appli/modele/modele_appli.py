"""
Module qui gère les données de l'application
"""

from connexion_bd import ConnexionBD
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/BD'))

from arme_bd import ArmeBD
from categorie_bd import CategorieBD
from club_bd import ClubBD
from competition_bd import CompetitionBD
from escrimeur_bd import EscrimeurBD
from inscrire_arbitre_bd import InscrireArbitreBD
from inscrire_bd import InscrireBD
from lieu_bd import LieuBD
from match_bd import MatchBD
from organisateur_bd import OrganisateurBD
from phase_bd import PhaseBD
from phase_finale_bd import PhaseFinaleBD
from poule_bd import PouleBD
from touche_bd import ToucheBD
from piste_bd import PisteBD
from equipe_bd import EquipeBD


class ModeleAppli:
    """
    Classe qui gère les données de l'application
    """

    def __init__(self):
        self.__connexion = ConnexionBD()
        self.__arme_bd = ArmeBD(self.__connexion.get_connexion())
        self.__categorie_bd = CategorieBD(self.__connexion.get_connexion())
        self.__club_bd = ClubBD(self.__connexion.get_connexion())
        self.__competition_bd = CompetitionBD(self.__connexion.get_connexion())
        self.__escrimeur_bd = EscrimeurBD(self.__connexion.get_connexion())
        self.__inscrire_arbitre_bd = InscrireArbitreBD(
            self.__connexion.get_connexion())
        self.__inscrire_bd = InscrireBD(self.__connexion.get_connexion())
        self.__lieu_bd = LieuBD(self.__connexion.get_connexion())
        self.__match_bd = MatchBD(self.__connexion.get_connexion())
        self.__organisateur_bd = OrganisateurBD(
            self.__connexion.get_connexion())
        self.__phase_bd = PhaseBD(self.__connexion.get_connexion())
        self.__phase_final_bd = PhaseFinaleBD(self.__connexion.get_connexion())
        self.__poule_bd = PouleBD(self.__connexion.get_connexion())
        self.__touche_bd = ToucheBD(self.__connexion.get_connexion())
        self.__piste_bd = PisteBD(self.__connexion.get_connexion())
        self.__equipe_bd = EquipeBD(self.__connexion.get_connexion())

    def get_equipe_bd(self) -> EquipeBD:
        """
        Retourne l'objet qui gère les interactions avec la table equipe

        Returns :
            EquipeBD : l'objet qui gère les interactions avec la table equipe
        """
        return self.__equipe_bd

    def get_arme_bd(self) -> ArmeBD:
        """
        Retourne l'objet qui gère les interactions avec la table arme

        Returns :
            ArmeBD : l'objet qui gère les interactions avec la table arme
        """
        return self.__arme_bd

    def get_categorie_bd(self) -> CategorieBD:
        """
        Retourne l'objet qui gère les interactions avec la table categorie

        Returns :
            CategorieBD : l'objet qui gère les interactions avec la table categorie
        """
        return self.__categorie_bd

    def get_club_bd(self) -> ClubBD:
        """
        Retourne l'objet qui gère les interactions avec la table club

        Returns :
            ClubBD : l'objet qui gère les interactions avec la table club
        """
        return self.__club_bd

    def get_competition_bd(self) -> CompetitionBD:
        """
        Retourne l'objet qui gère les interactions avec la table competition

        Returns :
            CompetitionBD : l'objet qui gère les interactions avec la table competition
        """
        return self.__competition_bd

    def get_escrimeur_bd(self) -> EscrimeurBD:
        """
        Retourne l'objet qui gère les interactions avec la table escrimeur

        Returns :
            EscrimeurBD : l'objet qui gère les interactions avec la table escrimeur
        """
        return self.__escrimeur_bd

    def get_inscrire_arbitre_bd(self) -> InscrireArbitreBD:
        """
        Retourne l'objet qui gère les interactions avec la table inscrire_arbitre

        Returns :
            InscrireArbitreBD : l'objet qui gère les interactions avec la table inscrire_arbitre
        """
        return self.__inscrire_arbitre_bd

    def get_inscrire_bd(self) -> InscrireBD:
        """
        Retourne l'objet qui gère les interactions avec la table inscrire

        Returns :
            InscrireBD : l'objet qui gère les interactions avec la table inscrire
        """
        return self.__inscrire_bd

    def get_lieu_bd(self) -> LieuBD:
        """
        Retourne l'objet qui gère les interactions avec la table lieu

        Returns :
            LieuBD : l'objet qui gère les interactions avec la table lieu
        """
        return self.__lieu_bd

    def get_match_bd(self) -> MatchBD:
        """
        Retourne l'objet qui gère les interactions avec la table match

        Returns :
            MatchBD : l'objet qui gère les interactions avec la table match

        """
        return self.__match_bd

    def get_organisateur_bd(self) -> OrganisateurBD:
        """
        Retourne l'objet qui gère les interactions avec la table organisateur

        Returns :
            OrganisateurBD : l'objet qui gère les interactions avec la table organisateur

        """
        return self.__organisateur_bd

    def get_phase_bd(self) -> PhaseBD:
        """
        Retourne l'objet qui gère les interactions avec la table phase

        Returns :
            PhaseBD : l'objet qui gère les interactions avec la table phase
        """
        return self.__phase_bd

    def get_phase_finale_bd(self) -> PhaseFinaleBD:
        """
        Retourne l'objet qui gère les interactions avec la table phase_finale

        Returns :
            PhaseFinaleBD : l'objet qui gère les interactions avec la table phase_finale
        """
        return self.__phase_final_bd

    def get_poule_bd(self) -> PouleBD:
        """
        Retourne l'objet qui gère les interactions avec la table poule

        Returns :
            PouleBD : l'objet qui gère les interactions avec la table poule
        """
        return self.__poule_bd

    def get_touche_bd(self) -> ToucheBD:
        """
        Retourne l'objet qui gère les interactions avec la table touche

        Returns :
            ToucheBD : l'objet qui gère les interactions avec la table touche
        """
        return self.__touche_bd

    def get_piste_bd(self) -> PisteBD:
        """
        Retourne l'objet qui gère les interactions avec la table piste

        Returns :
            PisteBD : l'objet qui gère les interactions avec la table piste
        """
        return self.__piste_bd

    def ouvrir_connexion(self):
        """
        ddd
        """
        self.__connexion.ouvrir_connexion()

    def close_connexion(self):
        """
        Ferme la connexion à la base de données
        """
        self.__connexion.fermer_connexion()
