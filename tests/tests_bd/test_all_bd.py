"""
Module qui fais les tests de toutes les classes de la base de données
Reunit tous les tests de la base de données en un seul 
fichier pour gagner du temps lors de l'execution des tests
"""

import sys
import os
import unittest
from unittest.mock import Mock

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

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from modele_appli import ModeleAppli
from arme import Arme
from categorie import Categorie
from club import Club
from competition import Competition
from escrimeur import Escrimeur
from inscrire_arbitre import InscrireArbitre
from lieu import Lieu
from match import Match
from phase import Phase
from touche import Touche
from poule import Poule
from inscrire import Inscrire
from phase_final import PhaseFinal
from organisateur import Organisateur

modele = ModeleAppli()


class TestArmeBD(unittest.TestCase):
    """
    Classe de test de la classe ArmeBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    @classmethod
    def setUpClass(cls):
        cls.modele = modele
        cls.arme_bd = cls.modele.get_arme_bd()

    def test_constructeur(self):
        """
        Test du constructeur de la classe ArmeBD
        """
        self.assertIsInstance(self.arme_bd, ArmeBD)

    def test_get_all_arme(self):
        """
        Test de la méthode get_all_arme
        """
        armes = self.arme_bd.get_all_arme()
        self.assertIsInstance(armes, list)

    def test_get_arme_by_id(self):
        """
        Test de la méthode get_arme_by_id
        """
        arme = self.arme_bd.get_arme_by_id(1)
        self.assertIsInstance(arme, Arme)
        arme = self.arme_bd.get_arme_by_id(-1)
        self.assertIsNone(arme)
        try:
            self.arme_bd.get_arme_by_id("a")
        except Exception as e:
            self.assertIsInstance(e, TypeError)


class TestCategorieBD(unittest.TestCase):
    """
    Classe de test de la classe CategorieBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    @classmethod
    def setUpClass(cls):
        cls.modele = modele
        cls.categorie_bd = cls.modele.get_categorie_bd()

    def test_constructeur(self):
        """
        Test du constructeur de la classe CategorieBD
        """
        self.assertIsInstance(self.categorie_bd, CategorieBD)

    def test_get_all_categorie(self):
        """
        Test de la méthode get_all_categorie
        """
        categories = self.categorie_bd.get_all_categorie()
        self.assertIsInstance(categories, list)

    def test_get_categorie_by_id(self):
        """
        Test de la méthode get_categorie_by_id
        """
        categorie = self.categorie_bd.get_categorie_by_id(1)
        self.assertIsInstance(categorie, Categorie)
        categorie = self.categorie_bd.get_categorie_by_id(-1)
        self.assertIsNone(categorie)
        try:
            self.categorie_bd.get_categorie_by_id("a")
        except Exception as e:
            self.assertIsInstance(e, TypeError)


class TestClubBD(unittest.TestCase):
    """
    Classe de test de la classe ClubBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    @classmethod
    def setUpClass(cls):
        cls.modele = modele
        cls.club_bd = cls.modele.get_club_bd()

    def test_constructeur(self):
        """
        Test du constructeur de la classe ClubBD
        """
        self.assertIsInstance(self.club_bd, ClubBD)

    def test_get_all_club(self):
        """
        Test de la méthode get_all_club
        """
        clubs = self.club_bd.get_all_club()
        self.assertIsInstance(clubs, list)

    def test_get_club_by_id(self):
        """
        Test de la méthode get_club_by_id
        """
        club = self.club_bd.get_club_by_id(1)
        self.assertIsInstance(club, Club)
        club = self.club_bd.get_club_by_id(-1)
        self.assertIsNone(club, Club)
        try:
            self.club_bd.get_club_by_id("a")
        except Exception as e:
            self.assertIsInstance(e, TypeError)

    def test_insert_club(self):
        """
        Test de la méthode insert_club
        """
        club = Club(-1, "test", "test", "test")
        self.club_bd.insert_club(club)
        try:
            self.club_bd.insert_club("a")
        except Exception as e:
            self.assertIsInstance(e, TypeError)

    def test_delete_club(self):
        """
        Test de la méthode delete_club
        """
        self.club_bd.delete_club(-1)
        try:
            self.club_bd.delete_club("a")
        except Exception as e:
            self.assertIsInstance(e, TypeError)

    def test_delete_club_by_nom(self):
        """
        Test de la méthode delete_club_by_nom
        """
        self.club_bd.delete_club_by_nom("test")
        try:
            self.club_bd.delete_club_by_nom(1)
        except Exception as e:
            self.assertIsInstance(e, TypeError)

    def test_login_club(self):
        """
        Test de la méthode login_club
        """
        club = self.club_bd.login_club("TUC Escrime", "lessaucisses")
        self.assertIsInstance(club, Club)
        club = self.club_bd.login_club("test", "test2")
        self.assertIsNone(club)
        try:
            self.club_bd.login_club(club, club)
        except Exception as e:
            self.assertIsInstance(e, TypeError)


class TestCompetitionBD(unittest.TestCase):
    """
    Classe de test de la classe CompetitionBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    @classmethod
    def setUpClass(cls):
        cls.modele = modele
        cls.competition_bd = cls.modele.get_competition_bd()

    def test_constructeur(self):
        """
        Test du constructeur de la classe CompetitionBD
        """
        self.assertIsInstance(self.competition_bd, CompetitionBD)

    def test_get_all_competition(self):
        """
        Test de la méthode get_all_competition
        """
        competitions = self.competition_bd.get_all_competition()
        self.assertIsInstance(competitions, list)

    def test_get_competition_by_id(self):
        """
        Test de la méthode get_competition_by_id
        """
        competition = self.competition_bd.get_competition_by_id(1)
        self.assertIsInstance(competition, Competition)
        competition = self.competition_bd.get_competition_by_id(-1)
        self.assertIsNone(competition)
        try:
            self.competition_bd.get_competition_by_id("a")
        except Exception as e:
            self.assertIsInstance(e, TypeError)

    def test_insert_competition(self):
        """
        Test de la méthode insert_competition
        """
        categorie = Categorie(1, "test")
        arme = Arme(1, "test", "test")
        lieu = Lieu(1, "test", "test")
        competition = Competition(-1, "test", "test", "test", "test", lieu,
                                  arme, categorie, 0.5)
        self.competition_bd.insert_competition(competition)
        try:
            self.competition_bd.insert_competition("a")
        except Exception as e:
            self.assertIsInstance(e, TypeError)

    def test_delete_competition_by_name(self):
        """
        Test de la méthode delete_competition_by_name
        """
        competition = Competition(-1, "test", "test", "test", "test", None,
                                  None, None, 0.5)
        self.competition_bd.delete_competition_by_name(competition)
        try:
            self.competition_bd.delete_competition_by_name("a")
        except Exception as e:
            self.assertIsInstance(e, TypeError)


class TestEscrimeurBD(unittest.TestCase):
    """
    Classe de test de la classe EscrimeurBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    @classmethod
    def setUpClass(cls):
        cls.modele = modele
        cls.escrimeur_bd = cls.modele.get_escrimeur_bd()

    def test_constructeur(self):
        """
        Test du constructeur de la classe EscrimeurBD
        """
        self.assertIsInstance(self.escrimeur_bd, EscrimeurBD)

    def test_get_all_escrimeur(self):
        """
        Test de la méthode get_all_escrimeur
        """
        escrimeurs = self.escrimeur_bd.get_all_escrimeur()
        self.assertIsInstance(escrimeurs, list)

    def test_get_escrimeur_by_id(self):
        """
        Test de la méthode get_escrimeur_by_id
        """
        escrimeur = self.escrimeur_bd.get_escrimeur_by_id(1)
        self.assertIsInstance(escrimeur, Escrimeur)
        escrimeur = self.escrimeur_bd.get_escrimeur_by_id(-1)
        self.assertIsNone(escrimeur)
        try:
            self.escrimeur_bd.get_escrimeur_by_id("a")
        except Exception as e:
            self.assertIsInstance(e, TypeError)

    def test_insert_escrimeur(self):
        """
        Test de la méthode insert_escrimeur
        """
        categorie = Categorie(1, "test")
        club = Club(1, "test", "test", "test")
        escrimeur = Escrimeur(-1, "test", "test", "test", "test", "test",
                              "test", "test", None, club, categorie, False)
        escrimeur2 = Escrimeur(-1, "test", "test", "test", "test", "test",
                               "test", "test2", 12, club, categorie, False)
        self.escrimeur_bd.insert_escrimeur(escrimeur)
        self.escrimeur_bd.insert_escrimeur(escrimeur2)
        with self.assertRaises(Exception):
            self.escrimeur_bd.insert_escrimeur("a")

    def test_delete_escrimeur_by_nom(self):
        """
        Test de la méthode delete_escrimeur_by_nom
        """
        self.escrimeur_bd.delete_escrimeur_by_nom("test")
        try:
            self.escrimeur_bd.delete_escrimeur_by_nom(1)
        except Exception as e:
            self.assertIsInstance(e, TypeError)

    def test_login_escrimeur(self):
        """
        Test de la méthode login_escrimeur
        """
        escrimeur = self.escrimeur_bd.login_escrimeur("33333333", "chedeville")
        self.assertIsInstance(escrimeur, Escrimeur)
        escrimeur = self.escrimeur_bd.login_escrimeur("a", "a")
        self.assertIsNone(escrimeur)
        try:
            self.escrimeur_bd.login_escrimeur(1, "test")
        except Exception as e:
            self.assertIsInstance(e, TypeError)


class TestInscrireArbitreBD(unittest.TestCase):
    """
    Classe de test de la classe InscrireArbitreBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    @classmethod
    def setUpClass(cls):
        cls.modele = modele
        cls.inscrire_arbitre_bd = cls.modele.get_inscrire_arbitre_bd()

    def test_constructeur(self):
        """
        Test du constructeur de la classe InscrireArbitreBD
        """
        self.assertIsInstance(self.inscrire_arbitre_bd, InscrireArbitreBD)

    def test_get_all_inscrire_arbitre(self):
        """
        Test de la méthode get_all_inscrire_arbitre
        """
        inscrire_arbitres = self.inscrire_arbitre_bd.get_all_arbitre()
        self.assertIsInstance(inscrire_arbitres, list)

    def test_get_inscrire_arbitre_by_id(self):
        """
        Test de la méthode get_inscrire_arbitre_by_id
        """
        inscrire_arbitre = self.inscrire_arbitre_bd.get_arbitre_by_id(1)
        self.assertIsInstance(inscrire_arbitre, InscrireArbitre)
        inscrire_arbitre = self.inscrire_arbitre_bd.get_arbitre_by_id(-1)
        self.assertIsNone(inscrire_arbitre)
        try:
            self.inscrire_arbitre_bd.get_arbitre_by_id("a")
        except Exception as e:
            self.assertIsInstance(e, TypeError)

    def test_insert_arbitre(self):
        """
        Test de la méthode insert_arbitre
        """
        inscription = InscrireArbitre(4, 6)
        self.inscrire_arbitre_bd.insert_arbitre(inscription)
        try:
            self.inscrire_arbitre_bd.insert_arbitre("a")
        except Exception as e:
            self.assertIsInstance(e, TypeError)

    def test_delete_arbitre(self):
        """
        Test de la méthode delete_arbitre
        """
        inscription = InscrireArbitre(4, 6)
        self.inscrire_arbitre_bd.delete_arbitre(inscription)
        try:
            self.inscrire_arbitre_bd.delete_arbitre("a")
        except Exception as e:
            self.assertIsInstance(e, TypeError)


class TestInscrireBD(unittest.TestCase):
    """
    Classe de test de la classe InscrireBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    @classmethod
    def setUpClass(cls):
        cls.modele = modele
        cls.inscrire_bd = cls.modele.get_inscrire_bd()

    def test_constructeur(self):
        """
        Test du constructeur de la classe InscrireBD
        """
        self.assertIsInstance(self.inscrire_bd, InscrireBD)

    def test_insert_inscrire(self):
        """
        Test de la méthode insert_inscrire
        """
        inscription = Inscrire(1, 1)
        inscription2 = Inscrire(1, 2)
        self.inscrire_bd.insert_inscrire(inscription)
        self.inscrire_bd.insert_inscrire(inscription2)
        try:
            self.inscrire_bd.insert_inscrire("a")
        except Exception as e:
            self.assertIsInstance(e, TypeError)

    def test_get_all_inscrire(self):
        """
        Test de la méthode get_all_inscrire
        """
        inscrires = self.inscrire_bd.get_all_inscrire()
        self.assertIsInstance(inscrires, list)

    def test_delete_inscrire(self):
        """
        Test de la méthode delete_inscrire
        """
        inscription = Inscrire(1, 1)
        self.inscrire_bd.delete_inscrire(inscription)
        try:
            self.inscrire_bd.delete_inscrire("a")
        except Exception as e:
            self.assertIsInstance(e, TypeError)


class TestLieuBD(unittest.TestCase):
    """
    Classe de test de la classe LieuBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    @classmethod
    def setUpClass(cls):
        cls.modele = modele
        cls.lieu_bd = cls.modele.get_lieu_bd()

    def test_constructeur(self):
        """
        Test du constructeur de la classe LieuBD
        """
        self.assertIsInstance(self.lieu_bd, LieuBD)

    def test_get_all_lieu(self):
        """
        Test de la méthode get_all_lieu
        """
        lieus = self.lieu_bd.get_all_lieu()
        self.assertIsInstance(lieus, list)

    def test_get_lieu_by_id(self):
        """
        Test de la méthode get_lieu_by_id
        """
        lieu = self.lieu_bd.get_lieu_by_id(1)
        self.assertIsInstance(lieu, Lieu)
        lieu = self.lieu_bd.get_lieu_by_id(-1)
        self.assertIsNone(lieu)
        try:
            self.lieu_bd.get_lieu_by_id("a")
        except Exception as e:
            self.assertIsInstance(e, TypeError)

    def test_insert_lieu(self):
        """
        Test de la méthode insert_lieu
        """
        lieu = Lieu(-1, "test", "test")
        self.lieu_bd.insert_lieu(lieu)
        try:
            self.lieu_bd.insert_lieu("a")
        except Exception as e:
            self.assertIsInstance(e, TypeError)

    def test_delete_lieu_by_adresse(self):
        """
        Test de la méthode delete_lieu_by_adresse
        """
        self.lieu_bd.delete_lieu_by_addresse(Lieu(-1, "test", "test"))
        try:
            self.lieu_bd.delete_lieu_by_addresse("a")
        except Exception as e:
            self.assertIsInstance(e, TypeError)


class TestMatchBD(unittest.TestCase):
    """
    Classe de test de la classe MatchBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    @classmethod
    def setUpClass(cls):
        cls.modele = modele
        cls.match_bd = cls.modele.get_match_bd()

    def test_constructeur(self):
        """
        Test du constructeur de la classe MatchBD
        """
        self.assertIsInstance(self.match_bd, MatchBD)

    def test_get_all_match(self):
        """
        Test de la méthode get_all_match
        """
        matchs = self.match_bd.get_all_match()
        self.assertIsInstance(matchs, list)

    def test_get_match_by_id(self):
        """
        Test de la méthode get_match_by_id
        """
        match = self.match_bd.get_match_by_id(1)
        self.assertIsInstance(match, Match)
        match = self.match_bd.get_match_by_id(-1)
        self.assertIsNone(match)
        try:
            self.match_bd.get_match_by_id("a")
        except Exception as e:
            self.assertIsInstance(e, TypeError)

    def test_insert_match(self):
        """
        Test de la méthode insert_match
        """
        escrimeur1 = Escrimeur(1, "test", "test", "test", "test", "test",
                               "test", "test", None, None, None, False)
        escrimeur2 = Escrimeur(2, "test", "test", "test", "test", "test",
                               "test", "test", None, None, None, False)
        arbitre = Escrimeur(3, "test", "test", "test", "test", "test", "test",
                            "test", None, None, None, True)
        match = Match(-1, 1, escrimeur1, escrimeur2, arbitre, 10.3, False)
        self.match_bd.insert_match(match)
        try:
            self.match_bd.insert_match("a")
        except Exception as e:
            self.assertIsInstance(e, TypeError)

    def test_delete_match_by_arbitre(self):
        """
        Test de la méthode delete_match_by_arbitre
        """
        self.match_bd.delete_match_by_arbitre(3)
        try:
            self.match_bd.delete_match_by_arbitre("a")
        except Exception as e:
            self.assertIsInstance(e, TypeError)


class TestOrganisateurBD(unittest.TestCase):
    """
    Classe de test de la classe OrganisateurBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    @classmethod
    def setUpClass(cls):
        cls.modele = modele
        cls.organisateur_bd = cls.modele.get_organisateur_bd()

    def test_constructeur(self):
        """
        Test du constructeur de la classe OrganisateurBD
        """
        self.assertIsInstance(self.organisateur_bd, OrganisateurBD)

    def test_get_all_organisateur(self):
        """
        Test de la méthode get_all_organisateur
        """
        organisateurs = self.organisateur_bd.get_all_organisateur()
        self.assertIsInstance(organisateurs, list)

    def test_login_organisateur(self):
        """
        Test de la méthode login_organisateur
        """
        organisateur = self.organisateur_bd.login_organisateur(
            "chedeville", "baptiste")
        self.assertIsInstance(organisateur, Organisateur)
        organisateur = self.organisateur_bd.login_organisateur("test", "test2")
        self.assertIsNone(organisateur)
        try:
            self.organisateur_bd.login_organisateur(1, "test")
        except Exception as e:
            self.assertIsInstance(e, TypeError)


class TestPhaseBD(unittest.TestCase):
    """
    Classe de test de la classe PhaseBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    @classmethod
    def setUpClass(cls):
        cls.modele = modele
        cls.phase_bd = cls.modele.get_phase_bd()

    def test_constructeur(self):
        """
        Test du constructeur de la classe PhaseBD
        """
        self.assertIsInstance(self.phase_bd, PhaseBD)

    def test_get_all_phase(self):
        """
        Test de la méthode get_all_phase
        """
        phases = self.phase_bd.get_all_phase()
        self.assertIsInstance(phases, list)

    def test_get_phase_by_id(self):
        """
        Test de la méthode get_phase_by_id
        """
        phase = self.phase_bd.get_phase_by_id(1)
        self.assertIsInstance(phase, Phase)
        phase = self.phase_bd.get_phase_by_id(-1)
        self.assertIsNone(phase)
        try:
            self.phase_bd.get_phase_by_id("a")
        except Exception as e:
            self.assertIsInstance(e, TypeError)

    def test_insert_phase(self):
        """
        Test de la méthode insert_phase
        """
        phase = Phase(-1, 1)
        self.phase_bd.insert_phase(phase)
        try:
            self.phase_bd.insert_phase("a")
        except Exception as e:
            self.assertIsInstance(e, TypeError)

    def test_insert_phase_by_id(self):
        """
        Test de la méthode insert_phase_by_id
        """
        phase = Phase(-10, 1)
        self.phase_bd.insert_phase_by_id(phase)
        try:
            self.phase_bd.insert_phase_by_id("a")
        except Exception as e:
            self.assertIsInstance(e, TypeError)

    def test_delete_phase_by_id(self):
        """
        Test de la méthode insert_phase_by_id
        """
        self.phase_bd.delete_phase_by_id(-10)
        try:
            self.phase_bd.delete_phase_by_id("a")
        except Exception as e:
            self.assertIsInstance(e, TypeError)


class TestPhaseFinaleBD(unittest.TestCase):
    """
    Classe de test de la classe PhaseFinalBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    @classmethod
    def setUpClass(cls):
        cls.modele = modele
        cls.phase_finale_bd = cls.modele.get_phase_finale_bd()
        cls.phase_bd = cls.modele.get_phase_bd()

    def test_constructeur(self):
        """
        Test du constructeur de la classe PhaseFinaleBD
        """
        self.assertIsInstance(self.phase_finale_bd, PhaseFinaleBD)

    def test_get_all_phase_final(self):
        """
        Test de la méthode get_all_phase_final
        """
        phase_finales = self.phase_finale_bd.get_all_phase_final()
        self.assertIsInstance(phase_finales, list)

    def test_insert_phase_finale(self):
        """
        Test de la méthode insert_phase_finale
        """
        self.phase_bd.insert_phase_by_id(Phase(-10, 1))
        self.phase_finale_bd.insert_phase_finale(PhaseFinal(-10))
        phase_finale = PhaseFinal(-1)
        self.assertIsNone(
            self.phase_finale_bd.insert_phase_finale(phase_finale))
        try:
            self.phase_finale_bd.insert_phase_finale("a")
        except Exception as e:
            self.assertIsInstance(e, TypeError)

    def test_delete_phase_finale(self):
        """
        Test de la méthode delete_phase_finale
        """
        phase_finale = PhaseFinal(-10)
        self.phase_finale_bd.delete_phase_finale(phase_finale)
        phase_finale = PhaseFinal(-1)
        self.assertIsNone(
            self.phase_finale_bd.delete_phase_finale(phase_finale))
        try:
            self.phase_finale_bd.delete_phase_finale("a")
        except Exception as e:
            self.assertIsInstance(e, TypeError)
        self.phase_bd.delete_phase_by_id(-10)


class TestPouleBD(unittest.TestCase):
    """
    Classe de test de la classe PouleBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    @classmethod
    def setUpClass(cls):
        cls.modele = modele
        cls.poule_bd = cls.modele.get_poule_bd()
        cls.phase_bd = cls.modele.get_phase_bd()

    def test_constructeur(self):
        """
        Test du constructeur de la classe PouleBD
        """
        self.assertIsInstance(self.poule_bd, PouleBD)

    def test_get_all_poule(self):
        """
        Test de la méthode get_all_poule
        """
        poules = self.poule_bd.get_all_poule()
        self.assertIsInstance(poules, list)

    def test_insert_poule(self):
        """
        Test de la méthode insert_poule
        """
        self.phase_bd.insert_phase_by_id(Phase(-11, 1))
        self.poule_bd.insert_poule(Poule(-11))
        poule = Poule(-1)
        self.assertIsNone(self.poule_bd.insert_poule(poule))
        try:
            self.poule_bd.insert_poule("a")
        except Exception as e:
            self.assertIsInstance(e, TypeError)

    def test_delete_poule(self):
        """
        Test de la méthode delete_poule
        """
        poule = Poule(-11)
        self.poule_bd.delete_poule(poule)
        poule = Poule(-1)
        self.assertIsNone(self.poule_bd.delete_poule(poule))
        try:
            self.poule_bd.delete_poule("a")
        except Exception as e:
            self.assertIsInstance(e, TypeError)
        self.phase_bd.delete_phase_by_id(-11)


class TestToucheBD(unittest.TestCase):
    """
    Classe de test de la classe ToucheBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    @classmethod
    def setUpClass(cls):
        cls.modele = modele
        cls.touche_bd = cls.modele.get_touche_bd()

    def test_constructeur(self):
        """
        Test du constructeur de la classe ToucheBD
        """
        self.assertIsInstance(self.touche_bd, ToucheBD)

    def test_get_all_touche(self):
        """
        Test de la méthode get_all_touche
        """
        touches = self.touche_bd.get_all_touche()
        self.assertIsInstance(touches, list)

    def test_insert_touche(self):
        """
        Test de la méthode insert_touche
        """
        match = Match(9, None, None, None, None, None, None)
        escrimeur = Escrimeur(6, None, None, None, None, None, None, None,
                              None, None, None, None)
        touche = Touche(match, escrimeur, 1)
        self.touche_bd.insert_touche(touche)
        try:
            self.touche_bd.insert_touche("a")
        except Exception as e:
            self.assertIsInstance(e, TypeError)

    def test_delete_touche(self):
        """
        Test de la méthode delete_touche
        """
        match = Match(9, None, None, None, None, None, None)
        escrimeur = Escrimeur(6, None, None, None, None, None, None, None,
                              None, None, None, None)
        touche = Touche(match, escrimeur, 1)
        self.touche_bd.delete_touche(touche, 1)
        try:
            self.touche_bd.delete_touche("a", 1)
        except Exception as e:
            self.assertIsInstance(e, TypeError)


class TestModeleAppli(unittest.TestCase):
    """
    Classe de test de la classe ModeleAppli
    """

    @classmethod
    def setUpClass(cls):
        cls.modele = modele

    def test_constructeur(self):
        """
        Teste le constructeur
        """
        self.assertIsInstance(self.modele, ModeleAppli)

    def test_get_arme_bd(self):
        """
        Teste la méthode get_arme_bd
        """
        self.assertIsInstance(self.modele.get_arme_bd(), ArmeBD)

    def test_get_categorie_bd(self):
        """
        Teste la méthode get_categorie_bd
        """
        self.assertIsInstance(self.modele.get_categorie_bd(), CategorieBD)

    def test_get_club_bd(self):
        """
        Teste la méthode get_club_bd
        """
        self.assertIsInstance(self.modele.get_club_bd(), ClubBD)

    def test_get_competition_bd(self):
        """
        Teste la méthode get_competition_bd
        """
        self.assertIsInstance(self.modele.get_competition_bd(), CompetitionBD)

    def test_get_escrimeur_bd(self):
        """
        Teste la méthode get_escrimeur_bd
        """
        self.assertIsInstance(self.modele.get_escrimeur_bd(), EscrimeurBD)

    def test_get_inscrire_arbitre_bd(self):
        """
        Teste la méthode get_inscrire_arbitre_bd
        """
        self.assertIsInstance(self.modele.get_inscrire_arbitre_bd(),
                              InscrireArbitreBD)

    def test_get_inscrire_bd(self):
        """
        Teste la méthode get_inscrire_bd
        """
        self.assertIsInstance(self.modele.get_inscrire_bd(), InscrireBD)

    def test_get_lieu_bd(self):
        """
        Teste la méthode get_lieu_bd
        """
        self.assertIsInstance(self.modele.get_lieu_bd(), LieuBD)

    def test_get_match_bd(self):
        """
        Teste la méthode get_match_bd
        """
        self.assertIsInstance(self.modele.get_match_bd(), MatchBD)

    def test_get_organisateur_bd(self):
        """
        Teste la méthode get_organisateur_bd
        """
        self.assertIsInstance(self.modele.get_organisateur_bd(),
                              OrganisateurBD)

    def test_get_phase_bd(self):
        """
        Teste la méthode get_phase_bd
        """
        self.assertIsInstance(self.modele.get_phase_bd(), PhaseBD)

    def test_get_phase_finale_bd(self):
        """
        Teste la méthode get_phase_finale_bd
        """
        self.assertIsInstance(self.modele.get_phase_finale_bd(), PhaseFinaleBD)

    def test_get_poule_bd(self):
        """
        Teste la méthode get_poule_bd
        """
        self.assertIsInstance(self.modele.get_poule_bd(), PouleBD)

    def test_get_touche_bd(self):
        """
        Teste la méthode get_touche_bd
        """
        self.assertIsInstance(self.modele.get_touche_bd(), ToucheBD)


class TestException(TestClubBD):
    """
    Classe pour tester les exceptions des méthodes de la BD

    """

    @classmethod
    def setUpClass(cls):
        cls.modele2 = ModeleAppli()
        cls.club_bd2 = cls.modele2.get_club_bd()
        cls.arme_bd2 = cls.modele2.get_arme_bd()
        cls.categorie_bd2 = cls.modele2.get_categorie_bd()
        cls.cometition_bd2 = cls.modele2.get_competition_bd()
        cls.escripeur_bd2 = cls.modele2.get_escrimeur_bd()
        cls.inscrire_arbitre_bd2 = cls.modele2.get_inscrire_arbitre_bd()
        cls.touche_bd2 = cls.modele2.get_touche_bd()
        cls.organisateur_bd2 = cls.modele2.get_organisateur_bd()
        cls.poule_bd2 = cls.modele2.get_poule_bd()
        cls.phase_finale_bd2 = cls.modele2.get_phase_finale_bd()
        cls.phase_bd2 = cls.modele2.get_phase_bd()
        cls.match_bd2 = cls.modele2.get_match_bd()
        cls.lieu_bd2 = cls.modele2.get_lieu_bd()
        cls.inscrire_bd2 = cls.modele2.get_inscrire_bd()
        mock_connexion = Mock()
        mock_connexion.execute.side_effect = Exception(
            "Une erreur s'est produite lors de l'exécution de la requête")
        cls.club_bd2._ClubBD__connexion = mock_connexion
        cls.arme_bd2._ArmeBD__connexion = mock_connexion
        cls.categorie_bd2._CategorieBD__connexion = mock_connexion
        cls.cometition_bd2._CompetitionBD__connexion = mock_connexion
        cls.escripeur_bd2._EscrimeurBD__connexion = mock_connexion
        cls.inscrire_arbitre_bd2._InscrireArbitreBD__connexion = mock_connexion
        cls.touche_bd2._ToucheBD__connexion = mock_connexion
        cls.organisateur_bd2._OrganisateurBD__connexion = mock_connexion
        cls.poule_bd2._PouleBD__connexion = mock_connexion
        cls.phase_finale_bd2._PhaseFinaleBD__connexion = mock_connexion
        cls.phase_bd2._PhaseBD__connexion = mock_connexion
        cls.match_bd2._MatchBD__connexion = mock_connexion
        cls.lieu_bd2._LieuBD__connexion = mock_connexion
        cls.inscrire_bd2._InscrireBD__connexion = mock_connexion

    @classmethod
    def tearDownClass(cls):
        cls.modele2.close_connexion()

    def test_get_all_club(self):
        """
        Test de l'exception de la méthode get_all_club
        """
        clubs = self.club_bd2.get_all_club()
        self.assertIsNone(clubs)

    def test_get_all_arme(self):
        """
        Test de l'exception de la méthode get_all_arme
        """
        armes = self.arme_bd2.get_all_arme()
        self.assertIsNone(armes)

    def test_get_all_categorie(self):
        """
        Test de l'exception de la méthode get_all_categorie
        """
        categories = self.categorie_bd2.get_all_categorie()
        self.assertIsNone(categories)

    def test_get_all_competition(self):
        """
        Test de l'exception de la méthode get_all_competition
        """
        competitions = self.cometition_bd2.get_all_competition()
        self.assertIsNone(competitions)

    def test_get_all_escrimeur(self):
        """
        Test de l'exception de la méthode get_all_escrimeur
        """
        escrimeurs = self.escripeur_bd2.get_all_escrimeur()
        self.assertIsNone(escrimeurs)

    def test_get_all_arbitre(self):
        """
        Test de l'exception de la méthode get_all_arbitre
        """
        arbitres = self.inscrire_arbitre_bd2.get_all_arbitre()
        self.assertIsNone(arbitres)

    def test_get_all_touche(self):
        """
        Test de l'exception de la méthode get_all_touche
        """
        touches = self.touche_bd2.get_all_touche()
        self.assertIsNone(touches)

    def test_get_all_organisateur(self):
        """
        Test de l'exception de la méthode get_all_organisateur
        """
        organisateurs = self.organisateur_bd2.get_all_organisateur()
        self.assertIsNone(organisateurs)

    def test_get_all_poule(self):
        """
        Test de l'exception de la méthode get_all_poule
        """
        poules = self.poule_bd2.get_all_poule()
        self.assertIsNone(poules)

    def test_get_all_phase_final(self):
        """
        Test de l'exception de la méthode get_all_phase_final
        """
        phase_finales = self.phase_finale_bd2.get_all_phase_final()
        self.assertIsNone(phase_finales)

    def test_get_all_phase(self):
        """
        Test de l'exception de la méthode get_all_phase
        """
        phases = self.phase_bd2.get_all_phase()
        self.assertIsNone(phases)

    def test_get_all_match(self):
        """
        Test de l'exception de la méthode get_all_match
        """
        matchs = self.match_bd2.get_all_match()
        self.assertIsNone(matchs)

    def test_get_all_lieu(self):
        """
        Test de l'exception de la méthode get_all_lieu
        """
        lieus = self.lieu_bd2.get_all_lieu()
        self.assertIsNone(lieus)

    def test_get_all_inscrire(self):
        """
        Test de l'exception de la méthode get_all_inscrire
        """
        inscrires = self.inscrire_bd2.get_all_inscrire()
        self.assertIsNone(inscrires)
