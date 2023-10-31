"""
Module de test de la classe PhaseBD
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'tests/tests_bd'))

from test_bd import TestBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/BD'))

from phase_bd import PhaseBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from phase import Phase


class TestPhaseBD(TestBD, unittest.TestCase):
    """
    Classe de test de la classe PhaseBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    def test_constructeur(self):
        """
        Test du constructeur de la classe PhaseBD
        """
        self.assertIsInstance(self.modele.get_phase_bd(), PhaseBD)

    def test_get_all_phase(self):
        """
        Test de la méthode get_all_phase
        """
        phases = self.modele.get_phase_bd().get_all_phase()
        self.assertIsInstance(phases, list)

    def test_get_phase_by_id(self):
        """
        Test de la méthode get_phase_by_id
        """
        phase = self.modele.get_phase_bd().get_phase_by_id(1)
        self.assertIsInstance(phase, Phase)
        phase = self.modele.get_phase_bd().get_phase_by_id(-1)
        self.assertIsNone(phase)
        self.modele.fermer_connexion()
