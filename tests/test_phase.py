"""
Module de test de la classe Phase
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from phase import Phase


class TestPhase(unittest.TestCase):
    """
    Classe de test de la classe Phase

    Args:
        unittest (TestCase): Classe de base pour les tests unitaires intégrés
    """

    def test_constructeur(self):
        """
        Test du constructeur de la classe Phase
        """
        phase = Phase(1, 1)
        self.assertIsInstance(phase, Phase)

    def test_get_id(self):
        """
        Test de la fonction get_id de la classe Phase
        """
        phase = Phase(1, 1)
        self.assertEqual(phase.get_id_phase(), 1)

    def test_get_id_comp(self):
        """
        Test de la fonction get_id_comp de la classe Phase
        """
        phase = Phase(1, 1)
        self.assertEqual(phase.get_id_comp(), 1)

    def test_set_id(self):
        """
        Test de la fonction set_id de la classe Phase
        """
        phase = Phase(1, 1)
        phase.set_id_phase(2)
        self.assertEqual(phase.get_id_phase(), 2)

    def test_set_id_comp(self):
        """
        Test de la fonction set_id_comp de la classe Phase
        """
        phase = Phase(1, 1)
        phase.set_id_comp(2)
        self.assertEqual(phase.get_id_comp(), 2)

    def test_str(self):
        """
        Test de la fonction __str__ de la classe Phase
        """
        phase = Phase(1, 1)
        self.assertEqual(str(phase), 'Phase : 1 - 1 |')
