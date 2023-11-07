"""
Module de test de la classe ConnexionBD
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from connexion_bd import ConnexionBD


class TestConnexionBD(unittest.TestCase):
    """
    Classe de test de la classe ConnexionBD

    Args:
        unittest (TestCase): classe de base pour les tests unitaires intégrés
    """

    @classmethod
    def setUpClass(cls):
        cls.connexion = ConnexionBD()

    def test_creation_connexion(self):
        """
        Test de la création d'une connexion
        """
        self.assertIsNotNone(self.connexion)

    def test_ouverture_connexion(self):
        """
        Test de l'ouverture d'une connexion
        """
        self.connexion.ouvrir_connexion()
        self.assertIsNotNone(self.connexion.get_connexion())
        with self.assertRaises(Exception):
            self.connexion.ouvrir_connexion(False)

    def test_fermeture_connexion(self):
        """
        Test de la fermeture d'une connexion
        """
        self.connexion.fermer_connexion()
        self.assertIsNotNone(self.connexion.get_connexion())

    def test_get_connexion(self):
        """
        Test de la récupération de la connexion
        """
        self.connexion.ouvrir_connexion()
        self.assertIsNotNone(self.connexion.get_connexion())
