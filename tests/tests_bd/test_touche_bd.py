"""
Module de test de la classe ToucheBD
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'tests/tests_bd'))

from test_bd import TestBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/BD'))

from touche_bd import ToucheBD


class TestToucheBD(TestBD, unittest.TestCase):
    """
    Classe de test de la classe ToucheBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    def test_constructeur(self):
        """
        Test du constructeur de la classe ToucheBD
        """
        self.assertIsInstance(self.modele.get_touche_bd(), ToucheBD)

    def test_get_all_touche(self):
        """
        Test de la méthode get_all_touche
        """
        touches = self.modele.get_touche_bd().get_all_touche()
        self.assertIsInstance(touches, list)
        self.modele.fermer_connexion()
