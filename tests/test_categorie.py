"""
Module de test de la classe Categorie
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from categorie import Categorie


class TestCategorie(unittest.TestCase):
    """
    Classe de test de la classe Categorie

    Args:
        unittest (TestCase): Classe de base pour les tests unitaires
    """

    def test_constructeur(self):
        """
        Test du constructeur de la classe Categorie
        """
        categorie = Categorie(1, 'U17')
        self.assertIsInstance(categorie, Categorie)

    def test_get_id(self):
        """
        Test de la fonction get_id de la classe Categorie
        """
        categorie = Categorie(1, 'U17')
        self.assertEqual(categorie.get_id(), 1)

    def test_get_nom(self):
        """
        Test de la fonction get_nom de la classe Categorie
        """
        categorie = Categorie(1, 'U17')
        self.assertEqual(categorie.get_nom(), 'U17')

    def test_set_id(self):
        """
        Test de la fonction set_id de la classe Categorie
        """
        categorie = Categorie(1, 'U17')
        categorie.set_id(2)
        self.assertEqual(categorie.get_id(), 2)

    def test_set_nom(self):
        """
        Test de la fonction set_nom de la classe Categorie
        """
        categorie = Categorie(1, 'U17')
        categorie.set_nom('U19')
        self.assertEqual(categorie.get_nom(), 'U19')

    def test_str(self):
        """
        Test de la fonction __str__ de la classe Categorie
        """
        categorie = Categorie(1, 'U17')
        self.assertEqual(str(categorie), 'Catégorie : 1 - U17 |')
