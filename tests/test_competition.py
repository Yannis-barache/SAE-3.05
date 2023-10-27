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
from escrimeur import Escrimeur
from exceptions import PasAssezDArbitres


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
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5)
        self.assertIsInstance(competition, Competition)

    def test_get_id(self):
        """
        Test de la fonction get_id de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5)
        self.assertEqual(competition.get_id(), 1)

    def test_get_nom(self):
        """
        Test de la fonction get_nom de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5)
        self.assertEqual(competition.get_nom(), 'Escrime comp')

    def test_get_date(self):
        """
        Test de la fonction get_date de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5)
        self.assertEqual(competition.get_date(), '14-05-2004')

    def test_get_date_fin_inscription(self):
        """
        Test de la fonction get_date_fin_inscription de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5)
        self.assertEqual(competition.get_date_fin_inscription(), '14-05-2004')

    def test_get_saison(self):
        """
        Test de la fonction get_saison de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5)
        self.assertEqual(competition.get_saison(), 'été')

    def test_get_lieu(self):
        """
        Test de la fonction get_lieu de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5)
        self.assertEqual(competition.get_lieu(), lieu)

    def test_get_arme(self):
        """
        Test de la fonction get_arme de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5)
        self.assertEqual(competition.get_arme(), arme)

    def test_get_categorie(self):
        """
        Test de la fonction get_categorie de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5)
        self.assertEqual(competition.get_categorie(), categorie)

    def test_get_coeficient(self):
        """
        Test de la fonction get_coeficient de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(2, 'U20')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2005',
                                  '14-05-2005', 'hiver', lieu, arme, categorie,
                                  0.5)
        self.assertEqual(competition.get_coeficient(), 0.5)

    def test_set_id(self):
        """
        Test de la fonction set_id de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5)
        competition.set_id(2)
        self.assertEqual(competition.get_id(), 2)

    def test_set_nom(self):
        """
        Test de la fonction set_nom de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5)
        competition.set_nom('Escrime comp2')
        self.assertEqual(competition.get_nom(), 'Escrime comp2')

    def test_set_date(self):
        """
        Test de la fonction set_date de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5)
        competition.set_date('15-05-2004')
        self.assertEqual(competition.get_date(), '15-05-2004')

    def test_set_date_fin_inscription(self):
        """
        Test de la fonction set_date_fin_inscription de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5)
        competition.set_date_fin_inscription('15-05-2004')
        self.assertEqual(competition.get_date_fin_inscription(), '15-05-2004')

    def test_set_saison(self):
        """
        Test de la fonction set_saison de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5)
        competition.set_saison('hiver')
        self.assertEqual(competition.get_saison(), 'hiver')

    def test_set_lieu(self):
        """
        Test de la fonction set_lieu de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        lieu2 = Lieu(2, 'Une grande ville', 'Lyon France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5)
        competition.set_lieu(lieu2)
        self.assertEqual(competition.get_lieu(), lieu2)

    def test_set_arme(self):
        """
        Test de la fonction set_arme de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(1, 'U17')
        arme = Arme(1, 'Epée Homme', 'M')
        arme2 = Arme(2, 'Epée Femme', 'F')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5)
        competition.set_arme(arme2)
        self.assertEqual(competition.get_arme(), arme2)

    def test_set_categorie(self):
        """
        Test de la fonction set_categorie de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(2, 'U20')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5)
        competition.set_categorie(categorie)
        self.assertEqual(competition.get_categorie(), categorie)

    def test_set_coeficient(self):
        """
        Test de la fonction set_coeficient de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(2, 'U20')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2005',
                                  '14-05-2005', 'hiver', lieu, arme, categorie,
                                  0.5)
        competition.set_coeficient(0.6)
        self.assertEqual(competition.get_coeficient(), 0.6)

    def test_generation_poule(self):
        """
        Test de la fonction generation_poule de la classe Competition
        """
        escrimeur1 = Escrimeur(1, 'Chédeville', 'Baptiste', 'M', '2004-14-05',
                               'baptched', 'mdp', 'AB21', 1, None, None, False)
        escrimeur2 = Escrimeur(2, 'Evelin', 'Colomban', 'M', '2004-14-05',
                               'clb', 'mdp', 'AB11', 2, None, None, False)
        escrimeur3 = Escrimeur(3, 'Dubois', 'Yann', 'M', '2004-14-05',
                               'yannou', 'mdp', 'AB01', 3, None, None, False)
        escrimeur4 = Escrimeur(4, 'Dupont', 'Jean', 'M', '2004-14-05',
                               'jeanjean', 'mdp', 'AB02', 4, None, None, False)
        escrimeur5 = Escrimeur(5, 'Dupont', 'Jean', 'M', '2004-14-05',
                               'jeanjean', 'mdp', 'AB03', 5, None, None, False)
        escrimeur6 = Escrimeur(6, 'Dupont', 'Jean', 'M', '2004-14-05',
                               'jeanjean', 'mdp', 'AB04', 6, None, None, False)
        escrimeur7 = Escrimeur(7, 'Dupont', 'Jean', 'M', '2004-14-05',
                               'jeanjean', 'mdp', 'AB05', 7, None, None, False)
        escrimeur8 = Escrimeur(8, 'Dupont', 'Jean', 'M', '2004-14-05',
                               'jeanjean', 'mdp', 'AB06', 8, None, None, False)
        escrimeur9 = Escrimeur(9, 'Dupont', 'Jean', 'M', '2004-14-05',
                               'jeanjean', 'mdp', 'AB07', 9, None, None, False)
        escrimeur10 = Escrimeur(10, 'Dupont', 'Jean', 'M', '2004-14-05',
                                'jeanjean', 'mdp', 'AB08', 10, None, None,
                                False)

        arbitre1 = Escrimeur(11, 'Dupont', 'Jean', 'M', '2004-14-05',
                             'jeanjean', 'mdp', 'AB09', 11, None, None, True)
        arbitre2 = Escrimeur(12, 'Dupont', 'Jean', 'M', '2004-14-05',
                             'jeanjean', 'mdp', 'AB10', 12, None, None, False)

        liste_escrimeur = [
            escrimeur1, escrimeur2, escrimeur3, escrimeur4, escrimeur5,
            escrimeur6, escrimeur7, escrimeur8, escrimeur9, escrimeur10
        ]
        liste_arbitre = [arbitre1, arbitre2]

        dico = Competition.generation_poule(liste_escrimeur, liste_arbitre)
        self.assertEqual(len(dico), 2)
        dico2 = Competition.generation_poule(liste_escrimeur, [])
        self.assertEqual(dico2, None)

    def test_trie_classement_initial(self):
        """
        Test de la fonction trie_classement_initial de la classe Competition
        """
        escrimeur1 = Escrimeur(1, 'Chédeville', 'Baptiste', 'M', '2004-14-05',
                               'baptched', 'mdp', 'AB21', 1, None, None, False)
        escrimeur2 = Escrimeur(2, 'Evelin', 'Colomban', 'M', '2004-14-05',
                               'clb', 'mdp', 'AB11', 2, None, None, False)
        escrimeur3 = Escrimeur(3, 'Dubois', 'Yann', 'M', '2004-14-05',
                               'yannou', 'mdp', 'AB01', 3, None, None, False)
        escrimeur4 = Escrimeur(4, 'Dupont', 'Jean', 'M', '2004-14-05',
                               'jeanjean', 'mdp', 'AB02', 4, None, None, False)
        liste_trie = [escrimeur1, escrimeur2, escrimeur3, escrimeur4]
        liste_non_trie = [escrimeur4, escrimeur3, escrimeur2, escrimeur1]
        self.assertEqual(
            Competition.trie_classement_inital(liste_non_trie.copy()),
            liste_trie)

    def test_nombre_poule(self):
        """
        Test de la fonction nombre_poule de la classe Competition
        """
        assert Competition.nombre_poule(10, 2) == (2, 5)
        assert Competition.nombre_poule(11, 2) == (2, 6)
        with self.assertRaises(PasAssezDArbitres):
            Competition.nombre_poule(10, 1)

    def test_str(self):
        """
        Test de la fonction __str__ de la classe Competition
        """
        lieu = Lieu(1, 'Une grande ville', 'Paris France')
        categorie = Categorie(2, 'U20')
        arme = Arme(1, 'Epée Homme', 'M')
        competition = Competition(1, 'Escrime comp', '14-05-2004',
                                  '14-05-2004', 'été', lieu, arme, categorie,
                                  0.5)
        sortie = (
            'Competition : 1, Escrime comp, 14-05-2004, 14-05-2004, été, '
            'Lieu : Une grande ville Paris France 1 |, Arme : 1 - '
            'Epée Homme - M |, Catégorie : 2 - U20 | |')
        self.assertEqual(str(competition), sortie)
