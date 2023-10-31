"""
Module de test de la classe PouleBD
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/BD'))

from poule_bd import PouleBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from modele_appli import ModeleAppli


class TestPouleBD(unittest.TestCase):
    """
    Classe de test de la classe PouleBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    @classmethod
    def setUpClass(cls):
        cls.modele = ModeleAppli()
        cls.poule_bd = cls.modele.get_poule_bd()

    def test_constructeur(self):
        """
        Test du constructeur de la classe PouleBD
        """
        self.assertIsInstance(self.poule_bd, PouleBD)

    def test_get_all_poule(self):
        """
        Test de la méthode get_all_poule
        """
        poules = self.poule_bd.get_all_poule()
        self.assertIsInstance(poules, list)
