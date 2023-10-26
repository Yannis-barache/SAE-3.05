"""
Module contenant la classe Poule
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from poule import Poule
from escrimeur import Escrimeur
from match import Match
from competition import Competition
from club import Club
from touche import Touche


class TestPoule(unittest.TestCase):
    """
    Classe de test de la classe Poule

    Args:
        unittest (TestCase): Classe de base pour les tests unitaires intégrés
    """

    def test_constructeur(self):
        """
        Test du constructeur de la classe Poule
        """
        poule = Poule(1)
        self.assertIsInstance(poule, Poule)

    def test_get_id(self):
        """
        Test de la fonction get_id de la classe Poule
        """
        poule = Poule(1)
        self.assertEqual(poule.get_id(), 1)

    def test_get_les_matchs(self):
        """
        Test de la fonction get_les_matchs de la classe Poule
        """
        poule = Poule(1)
        self.assertEqual(poule.get_les_matchs(), [])

    def test_get_les_escrimeurs(self):
        """
        Test de la fonction get_les_escrimeurs de la classe Poule
        """
        poule = Poule(1)
        self.assertEqual(poule.get_les_escrimeurs(), [])

    def test_set_id(self):
        """
        Test de la fonction set_id de la classe Poule
        """
        poule = Poule(1)
        poule.set_id(2)
        self.assertEqual(poule.get_id(), 2)

    def test_set_les_matchs(self):
        """
        Test de la fonction set_les_matchs de la classe Poule
        """
        poule = Poule(1)
        escrimeur1 = Escrimeur(1, 'nom', 'prenom', 'sexe', 'date_naissance',
                               'mdp', 'email', 'telephone', 'licence', None,
                               None)
        escrimeur2 = Escrimeur(2, 'nom2', 'prenom2', 'sexe2',
                               'date_naissance2', 'mdp2', 'email2',
                               'telephone2', 'licence2', None, None)
        arbitre = Escrimeur(3, 'nom3', 'prenom3', 'sexe3', 'date_naissance3',
                            'mdp3', 'email3', 'telephone3', 'licence3', None,
                            None)
        match1 = Match(1, 1, escrimeur1, escrimeur2, arbitre, 10, False)
        poule.set_les_matchs([match1])
        self.assertEqual(poule.get_les_matchs(), [match1])

    def test_generer_matchs(self):
        """
        Test de la fonction generer_matchs de la classe Poule
        """
        poule = Poule(1)
        arbitre = Escrimeur(1, 'nom', 'prenom', 'sexe', 'date_naissance',
                            'mdp', 'email', 'telephone', 'licence', None, None)
        escrimeur1 = Escrimeur(2, 'nom', 'prenom', 'sexe', 'date_naissance',
                               'mdp', 'email', 'telephone', 'licence', None,
                               None)
        escrimeur2 = Escrimeur(3, 'nom', 'prenom', 'sexe', 'date_naissance',
                               'mdp', 'email', 'telephone', 'licence', None,
                               None)
        escrimeur3 = Escrimeur(4, 'nom', 'prenom', 'sexe', 'date_naissance',
                               'mdp', 'email', 'telephone', 'licence', None,
                               None)
        escrimeur4 = Escrimeur(5, 'nom', 'prenom', 'sexe', 'date_naissance',
                               'mdp', 'email', 'telephone', 'licence', None,
                               None)
        infos = (arbitre, [escrimeur1, escrimeur2, escrimeur3, escrimeur4])
        heure_debut = 10.5
        self.assertEqual(len(poule.generer_matchs(infos, heure_debut)), 6)

    def test_get_match_by_escrimeurs(self):
        """
        Test de la fonction get_match_by_escrimeurs de la classe Poule
        """
        poule = Poule(1)
        escrimeur1 = Escrimeur(1, 'nom', 'prenom', 'sexe', 'date_naissance',
                               'mdp', 'email', 'telephone', 'licence', None,
                               None)
        escrimeur2 = Escrimeur(2, 'nom2', 'prenom2', 'sexe2',
                               'date_naissance2', 'mdp2', 'email2',
                               'telephone2', 'licence2', None, None)
        arbitre = Escrimeur(3, 'nom3', 'prenom3', 'sexe3', 'date_naissance3',
                            'mdp3', 'email3', 'telephone3', 'licence3', None,
                            None)
        match1 = Match(1, 1, escrimeur1, escrimeur2, arbitre, 10, False)
        poule.set_les_matchs([match1])
        self.assertEqual(poule.get_match_by_escrimeurs(escrimeur1, escrimeur2),
                         match1)
        self.assertEqual(poule.get_match_by_escrimeurs(arbitre, escrimeur1),
                         None)

    def test_generer_pdf(self):
        """
        Test de la fonction generer_pdf de la classe Poule
        """
        club = Club(1, 'nom', 'adresse', 'pays')
        club2 = Club(2, 'nom2', 'adresse2', 'pays2')
        escrimeur1 = Escrimeur(1, 'nom', 'prenom', 'sexe', 'date_naissance',
                               'pseudo', 'mdp', 'licence', 1, club, None)
        escrimeur2 = Escrimeur(2, 'nom2', 'prenom2', 'sexe2',
                               'date_naissance2', 'pseudo2', 'mdp2',
                               'licence2', 2, club, None)
        escrimeur3 = Escrimeur(3, 'nom3', 'prenom3', 'sexe3',
                               'date_naissance3', 'pseudo3', 'mdp3',
                               'licence3', 3, club, None)
        escrimeur4 = Escrimeur(4, 'nom4', 'prenom4', 'sexe4',
                               'date_naissance4', 'pseudo4', 'mdp4',
                               'licence4', 4, club, None)
        escrimeur5 = Escrimeur(5, 'nom5', 'prenom5', 'sexe5',
                               'date_naissance5', 'pseudo5', 'mdp5',
                               'licence5', 5, club, None)
        escrimeur6 = Escrimeur(6, 'nom6', 'prenom6', 'sexe6',
                               'date_naissance6', 'pseudo6', 'mdp6',
                               'licence6', 6, club2, None)
        escrimeur7 = Escrimeur(7, 'nom7', 'prenom7', 'sexe7',
                               'date_naissance7', 'pseudo7', 'mdp7',
                               'licence7', 7, club2, None)
        escrimeur8 = Escrimeur(8, 'nom8', 'prenom8', 'sexe8',
                               'date_naissance8', 'pseudo8', 'mdp8',
                               'licence8', 8, club2, None)
        escrimeur9 = Escrimeur(9, 'nom9', 'prenom9', 'sexe9',
                               'date_naissance9', 'pseudo9', 'mdp9',
                               'licence9', 9, club2, None)
        escrimeur10 = Escrimeur(10, 'nom10', 'prenom10', 'sexe10',
                                'date_naissance10', 'pseudo10', 'mdp10',
                                'licence10', 10, club, None)

        arbitre1 = Escrimeur(11, 'nom11', 'prenom11', 'sexe11',
                             'date_naissance11', 'pseudo10', 'mdp11',
                             'licence11', 11, club, None)
        arbitre2 = Escrimeur(12, 'nom12', 'prenom12', 'sexe12',
                             'date_naissance12', 'pseudo10', 'mdp12',
                             'licence12', 12, club2, None)

        les_escrimeurs = [
            escrimeur1, escrimeur2, escrimeur3, escrimeur4, escrimeur5,
            escrimeur6, escrimeur7, escrimeur8, escrimeur9, escrimeur10
        ]
        les_arbitres = [arbitre1, arbitre2]

        poules = Competition.generation_poule(les_escrimeurs, les_arbitres)
        for poule in poules:
            matchs = poule.generer_matchs(poules.get(poule), 10.5)
            liste = []
            for match in matchs:
                escrimeur11 = match.get_escrimeur1()
                escrimeur22 = match.get_escrimeur2()
                touche = Touche(match, escrimeur11, 1)
                touche2 = Touche(match, escrimeur22, 2)
                touche3 = Touche(match, escrimeur11, 3)
                match.ajouter_touche(touche)
                match.ajouter_touche(touche2)
                match.ajouter_touche(touche3)
                match.set_finis(True)
                liste.append(match)
            poule.generer_pdf()

    def test_str(self):
        """
        Test de la fonction __str__ de la classe Poule
        """
        poule = Poule(1)
        self.assertEqual(str(poule), '1')
