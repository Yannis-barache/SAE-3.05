"""
Module de test de la classe PouleBD
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'tests/tests_bd'))

from test_bd import TestBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/BD'))

from poule_bd import PouleBD


class TestPouleBD(TestBD, unittest.TestCase):
    """
    Classe de test de la classe PouleBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    def test_constructeur(self):
        """
        Test du constructeur de la classe PouleBD
        """
        self.assertIsInstance(self.modele.get_poule_bd(), PouleBD)

    def test_get_all_poule(self):
        """
        Test de la méthode get_all_poule
        """
        poules = self.modele.get_poule_bd().get_all_poule()
        self.assertIsInstance(poules, list)
        self.modele.fermer_connexion()
