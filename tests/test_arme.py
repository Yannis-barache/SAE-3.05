"""
Module de test de la classe Arme
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from arme import Arme


class TestArme(unittest.TestCase):
    """
    Classe de test de la classe Arme
    """

    def test_constructeur(self):
        """
        Test du constructeur de la classe Arme
        """
        arme = Arme(1, 'Epée Homme', 'M')
        self.assertIsInstance(arme, Arme)

    def test_get_id(self):
        """
        Test de la fonction get_id de la classe Arme
        """
        arme = Arme(1, 'Epée Homme', 'M')
        self.assertEqual(arme.get_id(), 1)

    def test_get_nom(self):
        """
        Test de la fonction get_nom de la classe Arme
        """
        arme = Arme(1, 'Epée Homme', 'M')
        self.assertEqual(arme.get_nom(), 'Epée Homme')

    def test_set_id(self):
        """
        Test de la fonction set_id de la classe Arme
        """
        arme = Arme(1, 'Epée Homme', 'M')
        arme.set_id(2)
        self.assertEqual(arme.get_id(), 2)

    def test_set_nom(self):
        """
        Test de la fonction set_nom de la classe Arme
        """
        arme = Arme(1, 'Epée Homme', 'M')
        arme.set_nom('Epée Femme')
        self.assertEqual(arme.get_nom(), 'Epée Femme')

    def test_str(self):
        """
        Test de la fonction __str__ de la classe Arme
        """
        arme = Arme(1, 'Epée Homme', 'M')
        self.assertEqual(str(arme), 'Arme : 1 - Epée Homme - M |')
