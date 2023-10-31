"""
Module de test de la classe ClubBD
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'tests/tests_bd'))

from test_bd import TestBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/BD'))

from club_bd import ClubBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from club import Club


class TestClubBD(TestBD, unittest.TestCase):
    """
    Classe de test de la classe ClubBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    def test_constructeur(self):
        """
        Test du constructeur de la classe ClubBD
        """
        self.assertIsInstance(self.modele.get_club_bd(), ClubBD)

    def test_get_all_club(self):
        """
        Test de la méthode get_all_club
        """
        clubs = self.modele.get_club_bd().get_all_club()
        self.assertIsInstance(clubs, list)

    def test_get_club_by_id(self):
        """
        Test de la méthode get_club_by_id
        """
        club = self.modele.get_club_bd().get_club_by_id(1)
        self.assertIsInstance(club, Club)
        club = self.modele.get_club_bd().get_club_by_id(-1)
        self.assertIsNone(club)
        self.modele.fermer_connexion()
