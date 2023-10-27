"""
Module de test de la classe Club
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from club import Club


class TestClub(unittest.TestCase):
    """
    Classe de test de la classe Club
    """

    def test_constructeur(self):
        """
        Test du constructeur de la classe Club
        """
        club = Club(1, 'Club 1', 'Adresse 1', 'mdp')
        self.assertIsInstance(club, Club)

    def test_get_id(self):
        """
        Test de la fonction get_id de la classe Club
        """
        club = Club(1, 'Club 1', 'Adresse 1', 'mdp')
        self.assertEqual(club.get_id(), 1)

    def test_get_nom(self):
        """
        Test de la fonction get_nom de la classe Club
        """
        club = Club(1, 'Club 1', 'Adresse 1', 'mdp')
        self.assertEqual(club.get_nom(), 'Club 1')

    def test_get_adresse(self):
        """
        Test de la fonction get_adresse de la classe Club
        """
        club = Club(1, 'Club 1', 'Adresse 1', 'mdp')
        self.assertEqual(club.get_adresse(), 'Adresse 1')

    def test_get_mdp(self):
        """
        Test de la fonction get_mdp de la classe Club
        """
        club = Club(1, 'Club 1', 'Adresse 1', 'mdp')
        self.assertEqual(club.get_mdp(), 'mdp')

    def test_set_id(self):
        """
        Test de la fonction set_id de la classe Club
        """
        club = Club(1, 'Club 1', 'Adresse 1', 'mdp')
        club.set_id(2)
        self.assertEqual(club.get_id(), 2)

    def test_set_nom(self):
        """
        Test de la fonction set_nom de la classe Club
        """
        club = Club(1, 'Club 1', 'Adresse 1', 'mdp')
        club.set_nom('Club 2')
        self.assertEqual(club.get_nom(), 'Club 2')

    def test_set_adresse(self):
        """
        Test de la fonction set_adresse de la classe Club
        """
        club = Club(1, 'Club 1', 'Adresse 1', 'mdp')
        club.set_adresse('Adresse 2')
        self.assertEqual(club.get_adresse(), 'Adresse 2')

    def test_set_mdp(self):
        """
        Test de la fonction set_mdp de la classe Club
        """
        club = Club(1, 'Club 1', 'Adresse 1', 'mdp')
        club.set_mdp('mdp2')
        self.assertEqual(club.get_mdp(), 'mdp2')

    def test_str(self):
        """
        Test de la fonction __str__ de la classe Club
        """
        club = Club(1, 'Club 1', 'Adresse 1', 'mdp')
        self.assertEqual(str(club), 'Club : 1 - Club 1 - Adresse 1 - mdp |')
