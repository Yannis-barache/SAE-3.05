"""
Module de test de la classe LieuBD
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/BD'))

from lieu_bd import LieuBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from modele_appli import ModeleAppli
from lieu import Lieu


class TestLieuBD(unittest.TestCase):
    """
    Classe de test de la classe LieuBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    @classmethod
    def setUpClass(cls):
        cls.modele = ModeleAppli()
        cls.lieu_bd = cls.modele.get_lieu_bd()

    def test_constructeur(self):
        """
        Test du constructeur de la classe LieuBD
        """
        self.assertIsInstance(self.lieu_bd, LieuBD)

    def test_get_all_lieu(self):
        """
        Test de la méthode get_all_lieu
        """
        lieus = self.lieu_bd.get_all_lieu()
        self.assertIsInstance(lieus, list)

    def test_get_lieu_by_id(self):
        """
        Test de la méthode get_lieu_by_id
        """
        lieu = self.lieu_bd.get_lieu_by_id(1)
        self.assertIsInstance(lieu, Lieu)
        lieu = self.lieu_bd.get_lieu_by_id(-1)
        self.assertIsNone(lieu)
