"""
Module de test de la classe Match
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from match import Match
from club import Club
from escrimeur import Escrimeur
from categorie import Categorie


class TestMatch(unittest.TestCase):
    """
    Classe de test de la classe Match

    Args:
        unittest (TestCase): Classe de base pour les tests unitaires intégrés
    """

    def test_constructeur(self):
        """
        Test du constructeur de la classe Match
        """
        club = Club(1, 'Club 1', 'Adresse 1')
        categorie = Categorie(1, 'U19')
        escrimeur1 = Escrimeur(1, 'Chédeville', 'Baptiste', 'M', '2004-14-05',
                               'baptched', 'baptiste.chedeville@gmail.com',
                               'mdp', 'AB21', 1, club, categorie)
        escrimeur2 = Escrimeur(2, 'Evelin', 'Colomban', 'M', '2004-14-05',
                               'clb', 'Evelin.Colomban@gmail.com', 'mdp',
                               'AB11', 2, club, categorie)
        match = Match(1, 1, escrimeur1, escrimeur2)
        self.assertIsInstance(match, Match)

    def test_get_id(self):
        """
        Test de la fonction get_id de la classe Match
        """
        club = Club(1, 'Club 1', 'Adresse 1')
        categorie = Categorie(1, 'U19')
        escrimeur1 = Escrimeur(1, 'Chédeville', 'Baptiste', 'M', '2004-14-05',
                               'baptched', 'baptiste.chedeville@gmail.com',
                               'mdp', 'AB21', 1, club, categorie)
        escrimeur2 = Escrimeur(2, 'Evelin', 'Colomban', 'M', '2004-14-05',
                               'clb', 'Evelin.Colomban@gmail.com', 'mdp',
                               'AB11', 2, club, categorie)
        match = Match(1, 1, escrimeur1, escrimeur2)
        self.assertEqual(match.get_id(), 1)

    def test_get_id_phase(self):
        """
        Test de la fonction get_id_phase de la classe Match
        """
        categorie = Categorie(1, 'U19')
        club = Club(1, 'Club 1', 'Adresse 1')
        escrimeur1 = Escrimeur(1, 'Chédeville', 'Baptiste', 'M', '2004-14-05',
                               'baptched', 'baptiste.chedeville@gmail.com',
                               'mdp', 'AB21', 1, club, categorie)
        escrimeur2 = Escrimeur(2, 'Evelin', 'Colomban', 'M', '2004-14-05',
                               'clb', 'Evelin.Colomban@gmail.com', 'mdp',
                               'AB11', 2, club, categorie)
        match = Match(1, 1, escrimeur1, escrimeur2)
        self.assertEqual(match.get_id_phase(), 1)

    def test_get_escrimeur1(self):
        """
        Test de la fonction get_escrimeur1 de la classe Match
        """
        categorie = Categorie(1, 'U19')
        club = Club(1, 'Club 1', 'Adresse 1')
        escrimeur1 = Escrimeur(1, 'Chédeville', 'Baptiste', 'M', '2004-14-05',
                               'baptched', 'baptiste.chedeville@gmail.com',
                               'mdp', 'AB21', 1, club, categorie)
        escrimeur2 = Escrimeur(2, 'Evelin', 'Colomban', 'M', '2004-14-05',
                               'clb', 'Evelin.Colomban@gmail.com', 'mdp',
                               'AB11', 2, club, categorie)
        match = Match(1, 1, escrimeur1, escrimeur2)
        self.assertEqual(match.get_escrimeur1(), escrimeur1)

    def test_get_escrimeur2(self):
        """
        Test de la fonction get_escrimeur2 de la classe Match
        """
        categorie = Categorie(1, 'U19')
        club = Club(1, 'Club 1', 'Adresse 1')
        escrimeur1 = Escrimeur(1, 'Chédeville', 'Baptiste', 'M', '2004-14-05',
                               'baptched', 'baptiste.chedeville@gmail.com',
                               'mdp', 'AB21', 1, club, categorie)
        escrimeur2 = Escrimeur(2, 'Evelin', 'Colomban', 'M', '2004-14-05',
                               'clb', 'Evelin.Colomban@gmail.com', 'mdp',
                               'AB11', 2, club, categorie)
        match = Match(1, 1, escrimeur1, escrimeur2)
        self.assertEqual(match.get_escrimeur2(), escrimeur2)

    def test_set_id(self):
        """
        Test de la fonction set_id de la classe Match
        """
        categorie = Categorie(1, 'U19')
        club = Club(1, 'Club 1', 'Adresse 1')
        escrimeur1 = Escrimeur(1, 'Chédeville', 'Baptiste', 'M', '2004-14-05',
                               'baptched', 'baptiste.chedeville@gmail.com',
                               'mdp', 'AB21', 1, club, categorie)
        escrimeur2 = Escrimeur(2, 'Evelin', 'Colomban', 'M', '2004-14-05',
                               'clb', 'Evelin.Colomban@gmail.com', 'mdp',
                               'AB11', 2, club, categorie)
        match = Match(1, 1, escrimeur1, escrimeur2)
        match.set_id(2)
        self.assertEqual(match.get_id(), 2)

    def test_set_id_phase(self):
        """
        Test de la fonction set_id_phase de la classe Match
        """
        categorie = Categorie(1, 'U19')
        club = Club(1, 'Club 1', 'Adresse 1')
        escrimeur1 = Escrimeur(1, 'Chédeville', 'Baptiste', 'M', '2004-14-05',
                               'baptched', 'baptiste.chedeville@gmail.com',
                               'mdp', 'AB21', 1, club, categorie)
        escrimeur2 = Escrimeur(2, 'Evelin', 'Colomban', 'M', '2004-14-05',
                               'clb', 'Evelin.Colomban@gmail.com', 'mdp',
                               'AB11', 2, club, categorie)
        match = Match(1, 1, escrimeur1, escrimeur2)
        match.set_id_phase(2)
        self.assertEqual(match.get_id_phase(), 2)

    def test_set_escrimeur1(self):
        """
        Test de la fonction set_escrimeur1 de la classe Match
        """
        categorie = Categorie(1, 'U19')
        club = Club(1, 'Club 1', 'Adresse 1')
        escrimeur1 = Escrimeur(1, 'Chédeville', 'Baptiste', 'M', '2004-14-05',
                               'baptched', 'baptiste.chedeville@gmail.com',
                               'mdp', 'AB21', 1, club, categorie)
        escrimeur2 = Escrimeur(2, 'Evelin', 'Colomban', 'M', '2004-14-05',
                               'clb', 'Evelin.Colomban@gmail.com', 'mdp',
                               'AB11', 2, club, categorie)
        match = Match(1, 1, escrimeur1, escrimeur2)
        match.set_escrimeur1(escrimeur2)
        self.assertEqual(match.get_escrimeur1(), escrimeur2)

    def test_set_escrimeur2(self):
        """
        Test de la fonction set_escrimeur2 de la classe Match
        """
        categorie = Categorie(1, 'U19')
        club = Club(1, 'Club 1', 'Adresse 1')
        escrimeur1 = Escrimeur(1, 'Chédeville', 'Baptiste', 'M', '2004-14-05',
                               'baptched', 'baptiste.chedeville@gmail.com',
                               'mdp', 'AB21', 1, club, categorie)
        escrimeur2 = Escrimeur(2, 'Evelin', 'Colomban', 'M', '2004-14-05',
                               'clb', 'Evelin.Colomban@gmail.com', 'mdp',
                               'AB11', 2, club, categorie)
        match = Match(1, 1, escrimeur1, escrimeur2)
        match.set_escrimeur2(escrimeur1)
        self.assertEqual(match.get_escrimeur2(), escrimeur1)

    def test_str(self):
        """
        Test de la fonction __str__ de la classe Match
        """
        categorie = Categorie(1, 'U19')
        club = Club(1, 'Club 1', 'Adresse 1')
        escrimeur1 = Escrimeur(1, 'Chédeville', 'Baptiste', 'M', '2004-14-05',
                               'baptched', 'baptiste.chedeville@gmail.com',
                               'mdp', 'AB21', 1, club, categorie)
        escrimeur2 = Escrimeur(2, 'Evelin', 'Colomban', 'M', '2004-14-05',
                               'clb', 'Evelin.Colomban@gmail.com', 'mdp',
                               'AB11', 2, club, categorie)
        match = Match(1, 1, escrimeur1, escrimeur2)
        self.assertEqual(
            str(match),
            '1 - 1 - 1 - Chédeville - Baptiste - 2004-14-05 - baptched - '
            'baptiste.chedeville@gmail.com - mdp - AB21 - 1 - 1 - Club 1 - Adresse 1 - '
            '1 - U19 - 2 - Evelin - Colomban - 2004-14-05 - clb - '
            'Evelin.Colomban@gmail.com - mdp - AB11 - 2 - 1 - Club 1 - Adresse 1 - 1 - U19'
        )
