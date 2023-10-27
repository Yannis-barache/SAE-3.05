"""
Module de test de la classe Lieu
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from lieu import Lieu


class TestLieu(unittest.TestCase):
    """
    Classe de test de la classe Lieu

    Args:
        unittest (TestCase): Classe de base pour les tests unitaires
    """

    def test_constructeur(self):
        """
        Test du constructeur de la classe Lieu
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        self.assertIsInstance(lieu, Lieu)

    def test_get_id(self):
        """
        Test de la fonction get_id de la classe Lieu
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        self.assertEqual(lieu.get_id(), 1)

    def test_get_description(self):
        """
        Test de la fonction get_description de la classe Lieu
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        self.assertEqual(lieu.get_description(), 'Une grande ville')

    def test_get_adresse(self):
        """
        Test de la fonction get_adresse de la classe Lieu
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        self.assertEqual(lieu.get_adresse(), 'Paris France')

    def test_set_id(self):
        """
        Test de la fonction set_id de la classe Lieu
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        lieu.set_id(2)
        self.assertEqual(lieu.get_id(), 2)

    def test_set_description(self):
        """
        Test de la fonction set_description de la classe Lieu
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        lieu.set_description('Une petite ville')
        self.assertEqual(lieu.get_description(), 'Une petite ville')

    def test_set_adresse(self):
        """
        Test de la fonction set_adresse de la classe Lieu
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        lieu.set_adresse('Lyon France')
        self.assertEqual(lieu.get_adresse(), 'Lyon France')

    def test_str(self):
        """
        Test de la fonction __str__ de la classe Lieu
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        self.assertEqual(str(lieu), 'Lieu : Une grande ville Paris France 1 |')
