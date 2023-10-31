"""
Module de test de la classe PhaseFinaleBD
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/BD'))

from phase_finale_bd import PhaseFinaleBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from modele_appli import ModeleAppli


class TestPhaseFinaleBD(unittest.TestCase):
    """
    Classe de test de la classe PhaseFinalBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    @classmethod
    def setUpClass(cls):
        cls.modele = ModeleAppli()
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
