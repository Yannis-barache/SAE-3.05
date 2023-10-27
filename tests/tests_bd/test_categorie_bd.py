"""
Module de test de la classe CategorieBD
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/BD'))

from categorie_bd import CategorieBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from modele_appli import ModeleAppli
from categorie import Categorie

class TestCategorieBD(unittest.TestCase):
    """
    Classe de test de la classe CategorieBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    def test_constructeur(self):
        """
        Test du constructeur de la classe CategorieBD
        """
        modele = ModeleAppli()
        self.assertIsInstance(modele.get_categorie_bd(), CategorieBD)

    def test_get_all_categorie(self):
        """
        Test de la méthode get_all_categorie
        """
        modele = ModeleAppli()
        categories = modele.get_categorie_bd().get_all_categorie()
        self.assertIsInstance(categories, list)

    def test_get_categorie_by_id(self):
        """
        Test de la méthode get_categorie_by_id
        """
        modele = ModeleAppli()
        categorie = modele.get_categorie_bd().get_categorie_by_id(1)
        self.assertIsInstance(categorie, Categorie)
        categorie = modele.get_categorie_bd().get_categorie_by_id(-1)
        self.assertIsNone(categorie)
