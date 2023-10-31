"""
Module de test de la classe CompetitionBD
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/BD'))

from competition_bd import CompetitionBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from modele_appli import ModeleAppli
from competition import Competition


class TestCompetitionBD(unittest.TestCase):
    """
    Classe de test de la classe CompetitionBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    @classmethod
    def setUpClass(cls):
        cls.modele = ModeleAppli()
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
