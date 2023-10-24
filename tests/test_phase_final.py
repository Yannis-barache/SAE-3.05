"""
Module contenant la classe PhaseFinal
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from phase_final import PhaseFinal


class TestPhaseFinal(unittest.TestCase):
    """
    Classe de test de la classe PhaseFinal

    Args:
        unittest (TestCase): Classe de base pour les tests unitaires intégrés
    """

    def test_constructeur(self):
        """
        Test du constructeur de la classe PhaseFinal
        """
        phase_final = PhaseFinal(1)
        self.assertIsInstance(phase_final, PhaseFinal)

    def test_get_id_phase_f(self):
        """
        Test de la fonction get_id_phase_f de la classe PhaseFinal
        """
        phase_final = PhaseFinal(1)
        self.assertEqual(phase_final.get_id_phase_f(), 1)

    def test_set_id_phase_f(self):
        """
        Test de la fonction set_id_phase_final de la classe PhaseFinal
        """
        phase_final = PhaseFinal(1)
        phase_final.set_id_phase_f(2)
        self.assertEqual(phase_final.get_id_phase_f(), 2)

    def test_str(self):
        """
        Test de la fonction __str__ de la classe PhaseFinal
        """
        phase_final = PhaseFinal(1)
        self.assertEqual(str(phase_final), '1')
