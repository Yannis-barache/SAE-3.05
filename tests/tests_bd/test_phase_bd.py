"""
Module de test de la classe PhaseBD
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/BD'))

from phase_bd import PhaseBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from modele_appli import ModeleAppli
from phase import Phase

class TestPhaseBD(unittest.TestCase):
    """
    Classe de test de la classe PhaseBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    def test_constructeur(self):
        """
        Test du constructeur de la classe PhaseBD
        """
        modele = ModeleAppli()
        self.assertIsInstance(modele.get_phase_bd(), PhaseBD)

    def test_get_all_phase(self):
        """
        Test de la méthode get_all_phase
        """
        modele = ModeleAppli()
        phases = modele.get_phase_bd().get_all_phase()
        self.assertIsInstance(phases, list)

    def test_get_phase_by_id(self):
        """
        Test de la méthode get_phase_by_id
        """
        modele = ModeleAppli()
        phase = modele.get_phase_bd().get_phase_by_id(1)
        self.assertIsInstance(phase, Phase)
        phase = modele.get_phase_bd().get_phase_by_id(-1)
        self.assertIsNone(phase)
