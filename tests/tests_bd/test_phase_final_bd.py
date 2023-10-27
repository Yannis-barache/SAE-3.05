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

    def test_constructeur(self):
        """
        Test du constructeur de la classe PhaseFinaleBD
        """
        modele = ModeleAppli()
        self.assertIsInstance(modele.get_phase_finale_bd(), PhaseFinaleBD)

    def test_get_all_phase_final(self):
        """
        Test de la méthode get_all_phase_final
        """
        modele = ModeleAppli()
        phase_finales = modele.get_phase_finale_bd().get_all_phase_final()
        self.assertIsInstance(phase_finales, list)