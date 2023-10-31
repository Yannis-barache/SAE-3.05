"""
Module de test de la classe PhaseFinaleBD
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'tests/tests_bd'))

from test_bd import TestBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/BD'))

from phase_finale_bd import PhaseFinaleBD

class TestPhaseFinaleBD(TestBD, unittest.TestCase):
    """
    Classe de test de la classe PhaseFinalBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    def test_constructeur(self):
        """
        Test du constructeur de la classe PhaseFinaleBD
        """
        self.assertIsInstance(self.modele.get_phase_finale_bd(), PhaseFinaleBD)

    def test_get_all_phase_final(self):
        """
        Test de la méthode get_all_phase_final
        """
        phase_finales = self.modele.get_phase_finale_bd().get_all_phase_final()
        self.assertIsInstance(phase_finales, list)
        self.modele.fermer_connexion()
