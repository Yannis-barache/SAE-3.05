"""
Module de test de la classe Competition
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from competition import Competition
from categorie import Categorie
from arme import Arme
from lieu import Lieu


class TestCompetition(unittest.TestCase):
    """
    Classe de test de la classe Competition

    Args:
        unittest (TestCase): Classe de base pour les tests unitaires intégrés
    """

    def test_constructeur(self):
        """
        Test du constructeur de la classe Competition
        """
        lieu = Lieu(1, 'Paris', 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie)
        self.assertIsInstance(competition, Competition)

    def test_get_id(self):
        """
        Test de la fonction get_id de la classe Competition
        """
        lieu = Lieu(1, 'Paris', 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie)
        self.assertEqual(competition.get_id(), 1)

    def test_get_nom(self):
        """
        Test de la fonction get_nom de la classe Competition
        """
        lieu = Lieu(1, 'Paris', 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie)
        self.assertEqual(competition.get_nom(), 'Escrime comp')

    def test_get_date(self):
        """
        Test de la fonction get_date de la classe Competition
        """
        lieu = Lieu(1, 'Paris', 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie)
        self.assertEqual(competition.get_date(), '14-05-2004')

    def test_get_date_fin_inscription(self):
        """
        Test de la fonction get_date_fin_inscription de la classe Competition
        """
        lieu = Lieu(1, 'Paris', 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie)
        self.assertEqual(competition.get_date_fin_inscription(), '14-05-2004')

    def test_get_saison(self):
        """
        Test de la fonction get_saison de la classe Competition
        """
        lieu = Lieu(1, 'Paris', 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie)
        self.assertEqual(competition.get_saison(), 'été')

    def test_get_lieu(self):
        """
        Test de la fonction get_lieu de la classe Competition
        """
        lieu = Lieu(1, 'Paris', 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie)
        self.assertEqual(competition.get_lieu(), lieu)

    def test_get_arme(self):
        """
        Test de la fonction get_arme de la classe Competition
        """
        lieu = Lieu(1, 'Paris', 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie)
        self.assertEqual(competition.get_arme(), arme)

    def test_get_categorie(self):
        """
        Test de la fonction get_categorie de la classe Competition
        """
        lieu = Lieu(1, 'Paris', 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie)
        self.assertEqual(competition.get_categorie(), categorie)

    def test_set_id(self):
        """
        Test de la fonction set_id de la classe Competition
        """
        lieu = Lieu(1, 'Paris', 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie)
        competition.set_id(2)
        self.assertEqual(competition.get_id(), 2)

    def test_set_nom(self):
        """
        Test de la fonction set_nom de la classe Competition
        """
        lieu = Lieu(1, 'Paris', 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie)
        competition.set_nom('Escrime comp2')
        self.assertEqual(competition.get_nom(), 'Escrime comp2')

    def test_set_date(self):
        """
        Test de la fonction set_date de la classe Competition
        """
        lieu = Lieu(1, 'Paris', 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie)
        competition.set_date('15-05-2004')
        self.assertEqual(competition.get_date(), '15-05-2004')

    def test_set_date_fin_inscription(self):
        """
        Test de la fonction set_date_fin_inscription de la classe Competition
        """
        lieu = Lieu(1, 'Paris', 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie)
        competition.set_date_fin_inscription('15-05-2004')
        self.assertEqual(competition.get_date_fin_inscription(), '15-05-2004')

    def test_set_saison(self):
        """
        Test de la fonction set_saison de la classe Competition
        """
        lieu = Lieu(1, 'Paris', 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie)
        competition.set_saison('hiver')
        self.assertEqual(competition.get_saison(), 'hiver')

    def test_set_lieu(self):
        """
        Test de la fonction set_lieu de la classe Competition
        """
        lieu = Lieu(1, 'Paris', 'Une grande ville', 'Paris France')
        lieu2 = Lieu(2, 'Lyon', 'Une grande ville', 'Lyon France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie)
        competition.set_lieu(lieu2)
        self.assertEqual(competition.get_lieu(), lieu2)

    def test_set_arme(self):
        """
        Test de la fonction set_arme de la classe Competition
        """
        lieu = Lieu(1, 'Paris', 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme')
        arme2 = Arme(2, 'Epée Femme')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie)
        competition.set_arme(arme2)
        self.assertEqual(competition.get_arme(), arme2)

    def test_set_categorie(self):
        """
        Test de la fonction set_categorie de la classe Competition
        """
        lieu = Lieu(1, 'Paris', 'Une grande ville', 'Paris France')
        categorie = Categorie(2, 'U20')
        arme = Arme(1, 'Epée Homme')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie)
        competition.set_categorie(categorie)
        self.assertEqual(competition.get_categorie(), categorie)

    def test_str(self):
        """
        Test de la fonction __str__ de la classe Competition
        """
        lieu = Lieu(1, 'Paris', 'Une grande ville', 'Paris France')
        categorie = Categorie(2, 'U20')
        arme = Arme(1, 'Epée Homme')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie)
        self.assertEqual(
            str(competition),
            'Competition: 1, Escrime comp, 14-05-2004, 14-05-2004, été, '
            'id : 1 nom : Paris description : Une grande ville adresse : Paris France, '
            '1 - Epée Homme, 2 - U20')
