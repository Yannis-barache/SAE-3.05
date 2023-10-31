"""
Module de test de la classe ArmeBD
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/BD'))

from arme_bd import ArmeBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from modele_appli import ModeleAppli
from arme import Arme


class TestArmeBD(unittest.TestCase):
    """
    Classe de test de la classe ArmeBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    @classmethod
    def setUpClass(cls):
        cls.modele = ModeleAppli()
        cls.arme_bd = cls.modele.get_arme_bd()

    def test_constructeur(self):
        """
        Test du constructeur de la classe ArmeBD
        """
        self.assertIsInstance(self.arme_bd, ArmeBD)

    def test_get_all_arme(self):
        """
        Test de la méthode get_all_arme
        """
        armes = self.arme_bd.get_all_arme()
        self.assertIsInstance(armes, list)

    def test_get_arme_by_id(self):
        """
        Test de la méthode get_arme_by_id
        """
        arme = self.arme_bd.get_arme_by_id(1)
        self.assertIsInstance(arme, Arme)
        arme = self.arme_bd.get_arme_by_id(-1)
        self.assertIsNone(arme)
