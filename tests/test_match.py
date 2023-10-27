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
        club = Club(1, 'Club 1', 'Adresse 1', 'mdp')
        categorie = Categorie(1, 'U19')
        escrimeur1 = Escrimeur(1, 'Chédeville', 'Baptiste', 'M', '2004-14-05',
                               'baptched', 'mdp', 'AB21', 1, club, categorie,
                               False)
        escrimeur2 = Escrimeur(2, 'Evelin', 'Colomban', 'M', '2004-14-05',
                               'clb', 'mdp', 'AB11', 2, club, categorie, False)
        arbitre = Escrimeur(3, 'Dubois', 'Yann', 'M', '2004-14-05', 'yannou',
                            'mdp', 'AB01', 3, club, categorie, True)
        match = Match(1, 1, escrimeur1, escrimeur2, arbitre, 10.0, False)
        self.assertIsInstance(match, Match)

    def test_get_id(self):
        """
        Test de la fonction get_id de la classe Match
        """
        club = Club(1, 'Club 1', 'Adresse 1', 'mdp')
        categorie = Categorie(1, 'U19')
        escrimeur1 = Escrimeur(1, 'Chédeville', 'Baptiste', 'M', '2004-14-05',
                               'baptched', 'mdp', 'AB21', 1, club, categorie,
                               False)
        escrimeur2 = Escrimeur(2, 'Evelin', 'Colomban', 'M', '2004-14-05',
                               'clb', 'mdp', 'AB11', 2, club, categorie, False)
        arbitre = Escrimeur(3, 'Dubois', 'Yann', 'M', '2004-14-05', 'yannou',
                            'mdp', 'AB01', 3, club, categorie, True)
        match = Match(1, 1, escrimeur1, escrimeur2, arbitre, 10.0, False)
        self.assertEqual(match.get_id(), 1)

    def test_get_id_phase(self):
        """
        Test de la fonction get_id_phase de la classe Match
        """
        categorie = Categorie(1, 'U19')
        club = Club(1, 'Club 1', 'Adresse 1', 'mdp')
        escrimeur1 = Escrimeur(1, 'Chédeville', 'Baptiste', 'M', '2004-14-05',
                               'baptched', 'mdp', 'AB21', 1, club, categorie,
                               False)
        escrimeur2 = Escrimeur(2, 'Evelin', 'Colomban', 'M', '2004-14-05',
                               'clb', 'mdp', 'AB11', 2, club, categorie, False)
        arbitre = Escrimeur(3, 'Dubois', 'Yann', 'M', '2004-14-05', 'yannou',
                            'mdp', 'AB01', 3, club, categorie, True)
        match = Match(1, 1, escrimeur1, escrimeur2, arbitre, 10.0, False)
        self.assertEqual(match.get_id_phase(), 1)

    def test_get_escrimeur1(self):
        """
        Test de la fonction get_escrimeur1 de la classe Match
        """
        categorie = Categorie(1, 'U19')
        club = Club(1, 'Club 1', 'Adresse 1', 'mdp')
        escrimeur1 = Escrimeur(1, 'Chédeville', 'Baptiste', 'M', '2004-14-05',
                               'baptched', 'mdp', 'AB21', 1, club, categorie,
                               False)
        escrimeur2 = Escrimeur(2, 'Evelin', 'Colomban', 'M', '2004-14-05',
                               'clb', 'mdp', 'AB11', 2, club, categorie, False)
        arbitre = Escrimeur(3, 'Dubois', 'Yann', 'M', '2004-14-05', 'yannou',
                            'mdp', 'AB01', 3, club, categorie, True)
        match = Match(1, 1, escrimeur1, escrimeur2, arbitre, 10.0, False)
        self.assertEqual(match.get_escrimeur1(), escrimeur1)

    def test_get_escrimeur2(self):
        """
        Test de la fonction get_escrimeur2 de la classe Match
        """
        categorie = Categorie(1, 'U19')
        club = Club(1, 'Club 1', 'Adresse 1', 'mdp')
        escrimeur1 = Escrimeur(1, 'Chédeville', 'Baptiste', 'M', '2004-14-05',
                               'baptched', 'mdp', 'AB21', 1, club, categorie,
                               False)
        escrimeur2 = Escrimeur(2, 'Evelin', 'Colomban', 'M', '2004-14-05',
                               'clb', 'mdp', 'AB11', 2, club, categorie, False)
        arbitre = Escrimeur(3, 'Dubois', 'Yann', 'M', '2004-14-05', 'yannou',
                            'mdp', 'AB01', 3, club, categorie, True)
        match = Match(1, 1, escrimeur1, escrimeur2, arbitre, 10.0, False)
        self.assertEqual(match.get_escrimeur2(), escrimeur2)

    def test_get_arbitre(self):
        """
        Test de la fonction get_arbitre de la classe Match
        """
        categorie = Categorie(1, 'U19')
        club = Club(1, 'Club 1', 'Adresse 1', 'mdp')
        escrimeur1 = Escrimeur(1, 'Chédeville', 'Baptiste', 'M', '2004-14-05',
                               'baptched', 'mdp', 'AB21', 1, club, categorie,
                               False)
        escrimeur2 = Escrimeur(2, 'Evelin', 'Colomban', 'M', '2004-14-05',
                               'clb', 'mdp', 'AB11', 2, club, categorie, False)
        arbitre = Escrimeur(3, 'Dubois', 'Yann', 'M', '2004-14-05', 'yannou',
                            'mdp', 'AB01', 3, club, categorie, True)
        match = Match(1, 1, escrimeur1, escrimeur2, arbitre, 10.0, False)
        self.assertEqual(match.get_arbitre(), arbitre)

    def test_get_heure(self):
        """
        Test de la fonction get_heure de la classe Match
        """
        club = Club(1, 'Club 1', 'Adresse 1', 'mdp')
        categorie = Categorie(1, 'U19')
        escrimeur1 = Escrimeur(1, 'Chédeville', 'Baptiste', 'M', '2004-05-14',
                               'baptched', 'mdp', 'AB21', 1, club, categorie,
                               False)
        escrimeur2 = Escrimeur(2, 'Evelin', 'Colomban', 'M', '2005-05-14',
                               'clb', 'mdp', 'AB11', 2, club, categorie, False)
        arbitre = Escrimeur(3, 'Dubois', 'Yann', 'M', '2006-05-14', 'yannou',
                            'mdp', 'AB01', 3, club, categorie, True)
        match = Match(1, 1, escrimeur1, escrimeur2, arbitre, 10.0, False)
        self.assertEqual(match.get_heure(), 10.0)

    def test_set_id(self):
        """
        Test de la fonction set_id de la classe Match
        """
        categorie = Categorie(1, 'U19')
        club = Club(1, 'Club 1', 'Adresse 1', 'mdp')
        escrimeur1 = Escrimeur(1, 'Chédeville', 'Baptiste', 'M', '2004-14-05',
                               'baptched', 'mdp', 'AB21', 1, club, categorie,
                               False)
        escrimeur2 = Escrimeur(2, 'Evelin', 'Colomban', 'M', '2004-14-05',
                               'clb', 'mdp', 'AB11', 2, club, categorie, False)
        arbitre = Escrimeur(3, 'Dubois', 'Yann', 'M', '2004-14-05', 'yannou',
                            'mdp', 'AB01', 3, club, categorie, True)
        match = Match(1, 1, escrimeur1, escrimeur2, arbitre, 10.0, False)
        match.set_id(2)
        self.assertEqual(match.get_id(), 2)

    def test_set_id_phase(self):
        """
        Test de la fonction set_id_phase de la classe Match
        """
        categorie = Categorie(1, 'U19')
        club = Club(1, 'Club 1', 'Adresse 1', 'mdp')
        escrimeur1 = Escrimeur(1, 'Chédeville', 'Baptiste', 'M', '2004-14-05',
                               'baptched', 'mdp', 'AB21', 1, club, categorie,
                               False)
        escrimeur2 = Escrimeur(2, 'Evelin', 'Colomban', 'M', '2004-14-05',
                               'clb', 'mdp', 'AB11', 2, club, categorie, False)
        arbitre = Escrimeur(3, 'Dubois', 'Yann', 'M', '2004-14-05', 'yannou',
                            'mdp', 'AB01', 3, club, categorie, True)
        match = Match(1, 1, escrimeur1, escrimeur2, arbitre, 10.0, False)
        match.set_id_phase(2)
        self.assertEqual(match.get_id_phase(), 2)

    def test_set_escrimeur1(self):
        """
        Test de la fonction set_escrimeur1 de la classe Match
        """
        categorie = Categorie(1, 'U19')
        club = Club(1, 'Club 1', 'Adresse 1', 'mdp')
        escrimeur1 = Escrimeur(1, 'Chédeville', 'Baptiste', 'M', '2004-14-05',
                               'baptched', 'mdp', 'AB21', 1, club, categorie,
                               False)
        escrimeur2 = Escrimeur(2, 'Evelin', 'Colomban', 'M', '2004-14-05',
                               'clb', 'mdp', 'AB11', 2, club, categorie, False)
        arbitre = Escrimeur(3, 'Dubois', 'Yann', 'M', '2004-14-05', 'yannou',
                            'mdp', 'AB01', 3, club, categorie, True)
        match = Match(1, 1, escrimeur1, escrimeur2, arbitre, 10.0, False)
        match.set_escrimeur1(escrimeur2)
        self.assertEqual(match.get_escrimeur1(), escrimeur2)

    def test_set_escrimeur2(self):
        """
        Test de la fonction set_escrimeur2 de la classe Match
        """
        categorie = Categorie(1, 'U19')
        club = Club(1, 'Club 1', 'Adresse 1', 'mdp')
        escrimeur1 = Escrimeur(1, 'Chédeville', 'Baptiste', 'M', '2004-14-05',
                               'baptched', 'mdp', 'AB21', 1, club, categorie,
                               False)
        escrimeur2 = Escrimeur(2, 'Evelin', 'Colomban', 'M', '2004-14-05',
                               'clb', 'mdp', 'AB11', 2, club, categorie, False)
        arbitre = Escrimeur(3, 'Dubois', 'Yann', 'M', '2004-14-05', 'yannou',
                            'mdp', 'AB01', 3, club, categorie, True)
        match = Match(1, 1, escrimeur1, escrimeur2, arbitre, 10.0, False)
        match.set_escrimeur2(escrimeur1)
        self.assertEqual(match.get_escrimeur2(), escrimeur1)

    def test_set_arbitre(self):
        """
        Test de la fonction set_arbitre de la classe Match
        """
        categorie = Categorie(1, 'U19')
        club = Club(1, 'Club 1', 'Adresse 1', 'mdp')
        escrimeur1 = Escrimeur(1, 'Chédeville', 'Baptiste', 'M', '2004-14-05',
                               'baptched', 'mdp', 'AB21', 1, club, categorie,
                               False)
        escrimeur2 = Escrimeur(2, 'Evelin', 'Colomban', 'M', '2004-14-05',
                               'clb', 'mdp', 'AB11', 2, club, categorie, False)
        arbitre = Escrimeur(3, 'Dubois', 'Yann', 'M', '2004-14-05', 'yannou',
                            'mdp', 'AB01', 3, club, categorie, True)
        arbitre2 = Escrimeur(4, 'Dupont', 'Jean', 'M', '2004-14-05', 'jdupont',
                             'mdp', 'AB02', 4, club, categorie, True)
        match = Match(1, 1, escrimeur1, escrimeur2, arbitre, 10.0, False)
        match.set_arbitre(arbitre2)
        self.assertEqual(match.get_arbitre(), arbitre2)

    def test_set_heure(self):
        """
        Test de la fonction set_heure de la classe Match
        """
        club = Club(1, 'Club 1', 'Adresse 1', 'mdp')
        categorie = Categorie(1, 'U19')
        escrimeur1 = Escrimeur(1, 'Chédeville', 'Baptiste', 'M', '2004-05-14',
                               'baptched', 'mdp', 'AB21', 1, club, categorie,
                               False)
        escrimeur2 = Escrimeur(2, 'Evelin', 'Colomban', 'M', '2005-05-14',
                               'clb', 'mdp', 'AB11', 2, club, categorie, False)
        arbitre = Escrimeur(3, 'Dubois', 'Yann', 'M', '2006-05-14', 'yannou',
                            'mdp', 'AB01', 3, club, categorie, True)
        match = Match(1, 1, escrimeur1, escrimeur2, arbitre, 10.0, False)
        match.set_heure(11.0)
        self.assertEqual(match.get_heure(), 11.0)

    def test_str(self):
        """
        Test de la fonction __str__ de la classe Match
        """
        categorie = Categorie(1, 'U19')
        club = Club(1, 'Club 1', 'Adresse 1', 'mdp')
        escrimeur1 = Escrimeur(1, 'Chédeville', 'Baptiste', 'M', '2004-14-05',
                               'baptched', 'mdp', 'AB21', 1, club, categorie,
                               False)
        escrimeur2 = Escrimeur(2, 'Evelin', 'Colomban', 'M', '2004-14-05',
                               'clb', 'mdp', 'AB11', 2, club, categorie, False)
        arbitre = Escrimeur(3, 'Dubois', 'Yann', 'M', '2004-14-05', 'yannou',
                            'mdp', 'AB01', 3, club, categorie, True)
        match = Match(1, 1, escrimeur1, escrimeur2, arbitre, 10.0, True)
        sortie = (
            'Match : 1 - 1 - Escrimeur : 1 - Chédeville - Baptiste - 2004-14-05 - '
            'baptched - mdp - '
            'AB21 - 1 - Club : 1 - Club 1 - Adresse 1 - mdp | - Catégorie : '
            '1 - U19 | - False | - Escrimeur'
            ' : 2 - Evelin - Colomban - 2004-14-05 - clb - mdp - AB11 - 2 - '
            'Club : 1 - Club 1 - Adresse 1 - mdp '
            '| - Catégorie : 1 - U19 | - False | - Escrimeur : 3 - Dubois - '
            'Yann - 2004-14-05 - yannou - mdp - AB01 '
            '- 3 - Club : 1 - Club 1 - Adresse 1 - mdp | - Catégorie : 1 - U19 '
            '| - True | - 10.0 - True|')
        self.assertEqual(str(match), sortie)
