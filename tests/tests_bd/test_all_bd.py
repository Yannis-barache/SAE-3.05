"""
Module qui fais les tests de toutes les classes de la base de données
Reunit tous les tests de la base de données en un seul 
fichier pour gagner du temps lors de l'execution des tests
"""

import sys
import os
import unittest

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
        self.assertIsNone(club)


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

    def test_get_all_inscrire(self):
        """
        Test de la méthode get_all_inscrire
        """
        inscrires = self.inscrire_bd.get_all_inscrire()
        self.assertIsInstance(inscrires, list)


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
