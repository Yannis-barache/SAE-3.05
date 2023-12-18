"""
Module de test de la classe Touche
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from match import Match
from club import Club
from escrimeur import Escrimeur
from categorie import Categorie
from touche import Touche


class TestTouche(unittest.TestCase):
    """
    Classe de test de la classe Touche

    Args:
        unittest (TestCase): Classe de base pour les tests unitaires intégrés
    """

    def test_constructeur(self):
        """
        Test du constructeur de la classe Touche
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
        match = Match(1, 1, escrimeur1, escrimeur2, arbitre, 10.0, False, None)
        touche = Touche(match, escrimeur1, 1)
        self.assertIsInstance(touche, Touche)

    def test_get_match(self):
        """
        Test de la fonction get_match de la classe Touche
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
        match = Match(1, 1, escrimeur1, escrimeur2, arbitre, 10.0, False, None)
        touche = Touche(match, escrimeur1, 1)
        self.assertEqual(touche.get_match(), match)

    def test_get_escrimeur(self):
        """
        Test de la fonction get_escrimeur de la classe Touche
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
        match = Match(1, 1, escrimeur1, escrimeur2, arbitre, 10.0, False, None)
        touche = Touche(match, escrimeur1, 1)
        self.assertEqual(touche.get_escrimeur(), escrimeur1)

    def test_get_numero(self):
        """
        Test de la fonction get_numero de la classe Touche
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
        match = Match(1, 1, escrimeur1, escrimeur2, arbitre, 10.0, False, None)
        touche = Touche(match, escrimeur1, 1)
        self.assertEqual(touche.get_numero(), 1)

    def test_set_match(self):
        """
        Test de la fonction set_match de la classe Touche
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
        match = Match(1, 1, escrimeur1, escrimeur2, arbitre, 10.0, False, None)
        match2 = Match(2, 1, escrimeur1, escrimeur2, arbitre, 10.0, False,
                       None)
        touche = Touche(match, escrimeur1, 1)
        touche.set_match(match2)
        self.assertEqual(touche.get_match(), match2)

    def test_set_escrimeur(self):
        """
        Test de la fonction set_escrimeur de la classe Touche
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
        match = Match(1, 1, escrimeur1, escrimeur2, arbitre, 10.0, False, None)
        touche = Touche(match, escrimeur1, 1)
        touche.set_escrimeur(escrimeur2)
        self.assertEqual(touche.get_escrimeur(), escrimeur2)

    def test_set_numero(self):
        """
        Test de la fonction set_numero de la classe Touche
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
        match = Match(1, 1, escrimeur1, escrimeur2, arbitre, 10.0, False, None)
        touche = Touche(match, escrimeur1, 1)
        touche.set_numero(2)
        self.assertEqual(touche.get_numero(), 2)

    def test_str(self):
        """
        Test de la fonction __str__ de la classe Touche
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
        match = Match(1, 1, escrimeur1, escrimeur2, arbitre, 10.0, False, None)
        touche = Touche(match, escrimeur1, 1)
        sortie = (
            'Touche : Match : 1 - 1 - Escrimeur : 1 - Chédeville - Baptiste - '
            '2004-14-05 - '
            'baptched - mdp - AB21 - 1 - Club : 1 - Club 1 - Adresse 1 - mdp | - '
            'Catégorie : 1 - U19 | - False | - '
            'Escrimeur : 2 - Evelin - Colomban - 2004-14-05 - clb - mdp - AB11 - 2 - Club : '
            '1 - Club 1 - Adresse 1 - mdp | - Catégorie : 1 - U19 | - False | - '
            'Escrimeur : 3 - Dubois - Yann - 2004-14-05 - yannou - mdp - AB01 - 3 - Club : 1 - '
            'Club 1 - Adresse 1 - mdp | - Catégorie : 1 - U19 | - True | - '
            '10.0 - False| - Escrimeur : 1 - Chédeville - Baptiste - '
            '2004-14-05 - baptched - mdp - '
            'AB21 - 1 - Club : 1 - Club 1 - Adresse 1 - mdp | - Catégorie : '
            '1 - U19 | - False | - 1  |')
        self.assertEqual(str(touche), sortie)
