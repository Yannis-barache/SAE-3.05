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

    def test_creation_connexion(self):
        """
        Test de la création d'une connexion
        """
        connexion = ConnexionBD()
        self.assertIsNotNone(connexion)

    def test_ouverture_connexion(self):
        """
        Test de l'ouverture d'une connexion
        """
        connexion = ConnexionBD()
        connexion.ouvrir_connexion()
        self.assertIsNotNone(connexion.get_connexion())
        with self.assertRaises(Exception):
            connexion.ouvrir_connexion(False)

    def test_fermeture_connexion(self):
        """
        Test de la fermeture d'une connexion
        """
        connexion = ConnexionBD()
        connexion.fermer_connexion()
        self.assertIsNotNone(connexion.get_connexion())

    def test_get_connexion(self):
        """
        Test de la récupération de la connexion
        """
        connexion = ConnexionBD()
        connexion.ouvrir_connexion()
        self.assertIsNotNone(connexion.get_connexion())
