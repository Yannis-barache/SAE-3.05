"""
Teste le modèle de l'application.
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from modele_appli import ModeleAppli

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

class TestModeleAppli(unittest.TestCase):
    """
    Classe de test de la classe ModeleAppli
    """

    def test_constructeur(self):
        """
        Teste le constructeur
        """
        modele = ModeleAppli()
        self.assertIsInstance(modele, ModeleAppli)

    def test_get_arme_bd(self):
        """
        Teste la méthode get_arme_bd
        """
        modele = ModeleAppli()
        self.assertIsInstance(modele.get_arme_bd(), ArmeBD)

    def test_get_categorie_bd(self):
        """
        Teste la méthode get_categorie_bd
        """
        modele = ModeleAppli()
        self.assertIsInstance(modele.get_categorie_bd(), CategorieBD)

    def test_get_club_bd(self):
        """
        Teste la méthode get_club_bd
        """
        modele = ModeleAppli()
        self.assertIsInstance(modele.get_club_bd(), ClubBD)

    def test_get_competition_bd(self):
        """
        Teste la méthode get_competition_bd
        """
        modele = ModeleAppli()
        self.assertIsInstance(modele.get_competition_bd(), CompetitionBD)

    def test_get_escrimeur_bd(self):
        """
        Teste la méthode get_escrimeur_bd
        """
        modele = ModeleAppli()
        self.assertIsInstance(modele.get_escrimeur_bd(), EscrimeurBD)

    def test_get_inscrire_arbitre_bd(self):
        """
        Teste la méthode get_inscrire_arbitre_bd
        """
        modele = ModeleAppli()
        self.assertIsInstance(modele.get_inscrire_arbitre_bd(), InscrireArbitreBD)

    def test_get_inscrire_bd(self):
        """
        Teste la méthode get_inscrire_bd
        """
        modele = ModeleAppli()
        self.assertIsInstance(modele.get_inscrire_bd(), InscrireBD)

    def test_get_lieu_bd(self):
        """
        Teste la méthode get_lieu_bd
        """
        modele = ModeleAppli()
        self.assertIsInstance(modele.get_lieu_bd(), LieuBD)

    def test_get_match_bd(self):
        """
        Teste la méthode get_match_bd
        """
        modele = ModeleAppli()
        self.assertIsInstance(modele.get_match_bd(), MatchBD)

    def test_get_organisateur_bd(self):
        """
        Teste la méthode get_organisateur_bd
        """
        modele = ModeleAppli()
        self.assertIsInstance(modele.get_organisateur_bd(), OrganisateurBD)

    def test_get_phase_bd(self):
        """
        Teste la méthode get_phase_bd
        """
        modele = ModeleAppli()
        self.assertIsInstance(modele.get_phase_bd(), PhaseBD)

    def test_get_phase_finale_bd(self):
        """
        Teste la méthode get_phase_finale_bd
        """
        modele = ModeleAppli()
        self.assertIsInstance(modele.get_phase_finale_bd(), PhaseFinaleBD)

    def test_get_poule_bd(self):
        """
        Teste la méthode get_poule_bd
        """
        modele = ModeleAppli()
        self.assertIsInstance(modele.get_poule_bd(), PouleBD)

    def test_get_touche_bd(self):
        """
        Teste la méthode get_touche_bd
        """
        modele = ModeleAppli()
        self.assertIsInstance(modele.get_touche_bd(), ToucheBD)
