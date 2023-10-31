"""
Module de test de la classe ArmeBD
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'tests/tests_bd'))

from test_bd import TestBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/BD'))

from arme_bd import ArmeBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from arme import Arme


class TestArmeBD(TestBD, unittest.TestCase):
    """
    Classe de test de la classe ArmeBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    def test_constructeur(self):
        """
        Test du constructeur de la classe ArmeBD
        """
        self.assertIsInstance(self.modele.get_arme_bd(), ArmeBD)

    def test_get_all_arme(self):
        """
        Test de la méthode get_all_arme
        """
        armes = self.modele.get_arme_bd().get_all_arme()
        self.assertIsInstance(armes, list)

    def test_get_arme_by_id(self):
        """
        Test de la méthode get_arme_by_id
        """
        arme = self.modele.get_arme_bd().get_arme_by_id(1)
        self.assertIsInstance(arme, Arme)
        arme = self.modele.get_arme_bd().get_arme_by_id(-1)
        self.assertIsNone(arme)
        self.modele.fermer_connexion()

