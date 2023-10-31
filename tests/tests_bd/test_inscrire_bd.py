"""
Module de test de la classe InscrireBD
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/BD'))

from inscrire_bd import InscrireBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from modele_appli import ModeleAppli


class TestInscrireBD(unittest.TestCase):
    """
    Classe de test de la classe InscrireBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    @classmethod
    def setUpClass(cls):
        cls.modele = ModeleAppli()
        cls.inscrire_bd = cls.modele.get_inscrire_bd()

    def test_constructeur(self):
        """
        Test du constructeur de la classe InscrireBD
        """
        self.assertIsInstance(self.inscrire_bd, InscrireBD)

    def test_get_all_inscrire(self):
        """
        Test de la méthode get_all_inscrire
        """
        inscrires = self.inscrire_bd.get_all_inscrire()
        self.assertIsInstance(inscrires, list)
