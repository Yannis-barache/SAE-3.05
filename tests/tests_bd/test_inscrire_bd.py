"""
Module de test de la classe InscrireBD
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'tests/tests_bd'))

from test_bd import TestBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/BD'))

from inscrire_bd import InscrireBD


class TestInscrireBD(TestBD, unittest.TestCase):
    """
    Classe de test de la classe InscrireBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    def test_constructeur(self):
        """
        Test du constructeur de la classe InscrireBD
        """
        self.assertIsInstance(self.modele.get_inscrire_bd(), InscrireBD)

    def test_get_all_inscrire(self):
        """
        Test de la méthode get_all_inscrire
        """
        inscrires = self.modele.get_inscrire_bd().get_all_inscrire()
        self.assertIsInstance(inscrires, list)
        self.modele.fermer_connexion()
