"""
Module de test de la classe ToucheBD
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/BD'))

from touche_bd import ToucheBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from modele_appli import ModeleAppli


class TestToucheBD(unittest.TestCase):
    """
    Classe de test de la classe ToucheBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    def test_constructeur(self):
        """
        Test du constructeur de la classe ToucheBD
        """
        modele = ModeleAppli()
        self.assertIsInstance(modele.get_touche_bd(), ToucheBD)

    def test_get_all_touche(self):
        """
        Test de la méthode get_all_touche
        """
        modele = ModeleAppli()
        touches = modele.get_touche_bd().get_all_touche()
        self.assertIsInstance(touches, list)