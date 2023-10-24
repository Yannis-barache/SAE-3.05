"""
Module de test de la classe Escrimeur
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from escrimeur import Escrimeur
from club import Club


class TestEscrimeur(unittest.TestCase):
    """
    Classe de test de la classe Escrimeur
    """

    def test_constructeur(self):
        """
        Test du constructeur de la classe Escrimeur
        """
        club = Club(1, 'Club 1', 'Adresse 1')
        escrimeur = Escrimeur(1, 'Chédeville', 'Baptiste', '2004-14-05',
                              'baptched', 'baptiste.chedeville@gmail.com',
                              'mdp', 'AB21', 1, club)
        self.assertIsInstance(escrimeur, Escrimeur)

    def test_get_id(self):
        """
        Test de la fonction get_id de la classe Escrimeur
        """
        club = Club(1, 'Club 1', 'Adresse 1')
        escrimeur = Escrimeur(1, 'Chédeville', 'Baptiste', '2004-14-05',
                              'baptched', 'baptiste.chedeville@gmail.com',
                              'mdp', 'AB21', 1, club)
        self.assertEqual(escrimeur.get_id(), 1)

    def test_get_nom(self):
        """
        Test de la fonction get_nom de la classe Escrimeur
        """
        club = Club(1, 'Club 1', 'Adresse 1')
        escrimeur = Escrimeur(1, 'Chédeville', 'Baptiste', '2004-14-05',
                              'baptched', 'baptiste.chedeville@gmail.com',
                              'mdp', 'AB21', 1, club)
        self.assertEqual(escrimeur.get_nom(), 'Chédeville')

    def test_get_prenom(self):
        club = Club(1, 'Club 1', 'Adresse 1')
        escrimeur = Escrimeur(1, 'Chédeville', 'Baptiste', '2004-14-05',
                              'baptched', 'baptiste.chedeville@gmail.com',
                              'mdp', 'AB21', 1, club)
        self.assertEqual(escrimeur.get_prenom(), 'Baptiste')

    def test_get_date_naissance(self):
        club = Club(1, 'Club 1', 'Adresse 1')
        escrimeur = Escrimeur(1, 'Chédeville', 'Baptiste', '2004-14-05',
                              'baptched', 'baptiste.chedeville@gmail.com',
                              'mdp', 'AB21', 1, club)
        self.assertEqual(escrimeur.get_date_naissance(), '2004-14-05')

    def test_get_nom_utilisateur(self):
        club = Club(1, 'Club 1', 'Adresse 1')
        escrimeur = Escrimeur(1, 'Chédeville', 'Baptiste', '2004-14-05',
                              'baptched', 'baptiste.chedeville@gmail.com',
                              'mdp', 'AB21', 1, club)
        self.assertEqual(escrimeur.get_nom_utilisateur(), 'baptched')

    def test_get_adresse_mail(self):
        club = Club(1, 'Club 1', 'Adresse 1')
        escrimeur = Escrimeur(1, 'Chédeville', 'Baptiste', '2004-14-05',
                              'baptched', 'baptiste.chedeville@gmail.com',
                              'mdp', 'AB21', 1, club)
        self.assertEqual(escrimeur.get_adresse_mail(),
                         'baptiste.chedeville@gmail.com')

    def test_get_mdp(self):
        club = Club(1, 'Club 1', 'Adresse 1')
        escrimeur = Escrimeur(1, 'Chédeville', 'Baptiste', '2004-14-05',
                              'baptched', 'baptiste.chedeville@gmail.com',
                              'mdp', 'AB21', 1, club)
        self.assertEqual(escrimeur.get_mdp(), 'mdp')

    def test_get_licence(self):
        club = Club(1, 'Club 1', 'Adresse 1')
        escrimeur = Escrimeur(1, 'Chédeville', 'Baptiste', '2004-14-05',
                              'baptched', 'baptiste.chedeville@gmail.com',
                              'mdp', 'AB21', 1, club)
        self.assertEqual(escrimeur.get_licence(), 'AB21')

    def test_get_classement(self):
        club = Club(1, 'Club 1', 'Adresse 1')
        escrimeur = Escrimeur(1, 'Chédeville', 'Baptiste', '2004-14-05',
                              'baptched', 'baptiste.chedeville@gmail.com',
                              'mdp', 'AB21', 1, club)
        self.assertEqual(escrimeur.get_classement(), 1)

    def test_get_club(self):
        club = Club(1, 'Club 1', 'Adresse 1')
        escrimeur = Escrimeur(1, 'Chédeville', 'Baptiste', '2004-14-05',
                              'baptched', 'baptiste.chedeville@gmail.com',
                              'mdp', 'AB21', 1, club)
        self.assertEqual(escrimeur.get_club(), club)

    def test_set_id(self):
        """
        Test de la fonction set_id de la classe Escrimeur
        """
        club = Club(1, 'Club 1', 'Adresse 1')
        escrimeur = Escrimeur(1, 'Chédeville', 'Baptiste', '2004-14-05',
                              'baptched', 'baptiste.chedeville@gmail.com',
                              'mdp', 'AB21', 1, club)
        escrimeur.set_id(2)
        self.assertEqual(escrimeur.get_id(), 2)

    def test_set_nom(self):
        """
        Test de la fonction set_nom de la classe Escrimeur
        """
        club = Club(1, 'Club 1', 'Adresse 1')
        escrimeur = Escrimeur(2, 'Chédeville', 'Baptiste', '2004-14-05',
                              'baptched', 'baptiste.chedeville@gmail.com',
                              'mdp', 'AB21', 1, club)
        escrimeur.set_nom('Chedeville')
        self.assertEqual(escrimeur.get_nom(), 'Chedeville')

    def test_set_prenom(self):
        """
        Test de la fonction set_prenom de la classe Escrimeur
        """
        club = Club(1, 'Club 1', 'Adresse 1')
        escrimeur = Escrimeur(2, 'Chédeville', 'Baptiste', '2004-14-05',
                              'baptched', 'baptiste.chedeville@gmail.com',
                              'mdp', 'AB21', 1, club)
        escrimeur.set_prenom('Eric')
        self.assertEqual(escrimeur.get_prenom(), 'Eric')

    def test_set_date_naissance(self):
        """
        Test de la fonction set_date_naissance de la classe Escrimeur
        """
        club = Club(1, 'Club 1', 'Adresse 1')
        escrimeur = Escrimeur(2, 'Chédeville', 'Baptiste', '2004-14-05',
                              'baptched', 'baptiste.chedeville@gmail.com',
                              'mdp', 'AB21', 1, club)
        escrimeur.set_date_naissance('2004-05-14')
        self.assertEqual(escrimeur.get_date_naissance(), '2004-05-14')

    def test_set_nom_utilisateur(self):
        """
        Test de la fonction set_nom_utilisateur de la classe Escrimeur
        """
        club = Club(1, 'Club 1', 'Adresse 1')
        escrimeur = Escrimeur(2, 'Chédeville', 'Baptiste', '2004-14-05',
                              'baptched', 'baptiste.chedeville@gmail.com',
                              'mdp', 'AB21', 1, club)
        escrimeur.set_nom_utilisateur('bapt')
        self.assertEqual(escrimeur.get_nom_utilisateur(), 'bapt')

    def test_set_adresse_mail(self):
        """
        Test de la fonction set_adresse_mail de la classe Escrimeur
        """
        club = Club(1, 'Club 1', 'Adresse 1')
        escrimeur = Escrimeur(2, 'Chédeville', 'Baptiste', '2004-14-05',
                              'baptched', 'baptiste.chedeville@gmail.com',
                              'mdp', 'AB21', 1, club)
        escrimeur.set_adresse_mail('baptiste@gmail.com')
        self.assertEqual(escrimeur.get_adresse_mail(), 'baptiste@gmail.com')

    def test_set_mdp(self):
        """
        Test de la fonction set_mdp de la classe Escrimeur
        """
        club = Club(1, 'Club 1', 'Adresse 1')
        escrimeur = Escrimeur(2, 'Chédeville', 'Baptiste', '2004-14-05',
                              'baptched', 'baptiste.chedeville@gmail.com',
                              'mdp', 'AB21', 1, club)
        escrimeur.set_mdp('motdepasse')
        self.assertEqual(escrimeur.get_mdp(), 'motdepasse')

    def test_set_licence(self):
        """
        Test de la fonction set_licence de la classe Escrimeur
        """
        club = Club(1, 'Club 1', 'Adresse 1')
        escrimeur = Escrimeur(2, 'Chédeville', 'Baptiste', '2004-14-05',
                              'baptched', 'baptiste.chedeville@gmail.com',
                              'mdp', 'AB21', 1, club)
        escrimeur.set_licence('AB22')
        self.assertEqual(escrimeur.get_licence(), 'AB22')

    def test_set_classement(self):
        """
        Test de la fonction set_classement de la classe Escrimeur
        """
        club = Club(1, 'Club 1', 'Adresse 1')
        escrimeur = Escrimeur(2, 'Chédeville', 'Baptiste', '2004-14-05',
                              'baptched', 'baptiste.chedeville@gmail.com',
                              'mdp', 'AB21', 1, club)
        escrimeur.set_classement('2')
        self.assertEqual(escrimeur.get_classement(), '2')

    def test_set_club(self):
        """
        Test de la fonction set_club de la classe Escrimeur
        """
        club1 = Club(1, 'Club 1', 'Adresse 1')
        club2 = Club(2, 'Club 2', 'Adresse 2')
        escrimeur = Escrimeur(2, 'Chédeville', 'Baptiste', '2004-14-05',
                              'baptched', 'baptiste.chedeville@gmail.com',
                              'mdp', 'AB21', 1, club1)
        escrimeur.set_club(club2)
        self.assertEqual(escrimeur.get_club(), club2)

    def test_str(self):
        """
        Test de la fonction __str__ de la classe Escrimeur
        """
        club = Club(1, 'Club 1', 'Adresse 1')
        escrimeur = Escrimeur(2, 'Chédeville', 'Baptiste', '2004-14-05',
                              'baptched', 'baptiste.chedeville@gmail.com',
                              'mdp', 'AB21', 1, club)
        self.assertEqual(
            str(escrimeur),
            '2 - Chédeville - Baptiste - 2004-14-05 - baptched - '
            'baptiste.chedeville@gmail.com - mdp - AB21 - 1 - 1 - Club 1 - Adresse 1'
        )
