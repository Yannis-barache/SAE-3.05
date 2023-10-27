"""
Module de test de la classe MatchBD
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/BD'))

from match_bd import MatchBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from modele_appli import ModeleAppli
from match import Match

class TestMatchBD(unittest.TestCase):
    """
    Classe de test de la classe MatchBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    def test_constructeur(self):
        """
        Test du constructeur de la classe MatchBD
        """
        modele = ModeleAppli()
        self.assertIsInstance(modele.get_match_bd(), MatchBD)

    def test_get_all_match(self):
        """
        Test de la méthode get_all_match
        """
        modele = ModeleAppli()
        matchs = modele.get_match_bd().get_all_match()
        self.assertIsInstance(matchs, list)

    def test_get_match_by_id(self):
        """
        Test de la méthode get_match_by_id
        """
        modele = ModeleAppli()
        match = modele.get_match_bd().get_match_by_id(1)
        self.assertIsInstance(match, Match)
        match = modele.get_match_bd().get_match_by_id(-1)
        self.assertIsNone(match)
