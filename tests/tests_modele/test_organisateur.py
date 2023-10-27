"""
Module de test de la classe Organisateur
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from organisateur import Organisateur


class TestOrganisateur(unittest.TestCase):
    """
    Classe de test de la classe Organisateur
    """

    def test_constructeur(self):
        """
        Test du constructeur de la classe Organisateur
        """
        organisateur = Organisateur(1, 'Baptiste', 'Chédeville',
                                    'baptiste.chedevill@gmail.com', 'mdp',
                                    'baptched')
        self.assertIsInstance(organisateur, Organisateur)

    def test_get_id(self):
        """
        Test de la fonction get_id de la classe Organisateur
        """
        organisateur = Organisateur(1, 'Baptiste', 'Chédeville',
                                    'baptiste.chedevill@gmail.com', 'mdp',
                                    'baptched')
        self.assertEqual(organisateur.get_id(), 1)

    def test_get_nom(self):
        """
        Test de la fonction get_nom de la classe Organisateur
        """
        organisateur = Organisateur(1, 'Baptiste', 'Chédeville',
                                    'baptiste.chedevill@gmail.com', 'mdp',
                                    'baptched')
        self.assertEqual(organisateur.get_nom(), 'Baptiste')

    def test_get_prenom(self):
        """
        Test de la fonction get_prenom de la classe Organisateur
        """
        organisateur = Organisateur(1, 'Baptiste', 'Chédeville',
                                    'baptiste.chedevill@gmail.com', 'mdp',
                                    'baptched')
        self.assertEqual(organisateur.get_prenom(), 'Chédeville')

    def test_get_adresse_mail(self):
        """
        Test de la fonction get_adresse_mail de la classe Organisateur
        """
        organisateur = Organisateur(1, 'Baptiste', 'Chédeville',
                                    'baptiste.chedevill@gmail.com', 'mdp',
                                    'baptched')
        self.assertEqual(organisateur.get_adresse_mail(),
                         'baptiste.chedevill@gmail.com')

    def test_get_mdp(self):
        """
        Test de la fonction get_mdp de la classe Organisateur
        """
        organisateur = Organisateur(1, 'Baptiste', 'Chédeville',
                                    'baptiste.chedevill@gmail.com', 'mdp',
                                    'baptched')
        self.assertEqual(organisateur.get_mdp(), 'mdp')

    def test_get_nom_utilisateur(self):
        """
        Test de la fonction get_nom_utilisateur de la classe Organisateur
        """
        organisateur = Organisateur(1, 'Baptiste', 'Chédeville',
                                    'baptiste.chedevill@gmail.com', 'mdp',
                                    'baptched')
        self.assertEqual(organisateur.get_nom_utilisateur(), 'baptched')

    def test_set_id(self):
        """
        Test de la fonction set_id de la classe Organisateur
        """
        organisateur = Organisateur(1, 'Baptiste', 'Chédeville',
                                    'baptiste.chedevill@gmail.com', 'mdp',
                                    'baptched')
        organisateur.set_id(2)

    def test_set_nom(self):
        """
        Test de la fonction set_nom de la classe Organisateur
        """
        organisateur = Organisateur(1, 'Baptiste', 'Chédeville',
                                    'baptiste.chedevill@gmail.com', 'mdp',
                                    'baptched')
        organisateur.set_nom('Chedeville')
        self.assertEqual(organisateur.get_nom(), 'Chedeville')

    def test_set_prenom(self):
        """
        Test de la fonction set_prenom de la classe Organisateur
        """
        organisateur = Organisateur(1, 'Baptiste', 'Chédeville',
                                    'baptiste.chedevill@gmail.com', 'mdp',
                                    'baptched')
        organisateur.set_prenom('Erix')
        self.assertEqual(organisateur.get_prenom(), 'Erix')

    def test_set_adresse_mail(self):
        """
        Test de la fonction set_adresse_mail de la classe Organisateur
        """
        organisateur = Organisateur(1, 'Baptiste', 'Chédeville',
                                    'baptiste.chedevill@gmail.com', 'mdp',
                                    'baptched')
        organisateur.set_adresse_mail('b.gmail.com')
        self.assertEqual(organisateur.get_adresse_mail(), 'b.gmail.com')

    def test_set_mdp(self):
        """
        Test de la fonction set_mdp de la classe Organisateur
        """
        organisateur = Organisateur(1, 'Baptiste', 'Chédeville',
                                    'baptiste.chedevill@gmail.com', 'mdp',
                                    'baptched')
        organisateur.set_mdp('mdp2')
        self.assertEqual(organisateur.get_mdp(), 'mdp2')

    def test_set_nom_utilisateur(self):
        """
        Test de la fonction set_nom_utilisateur de la classe Organisateur
        """
        organisateur = Organisateur(1, 'Baptiste', 'Chédeville',
                                    'baptiste.chedevill@gmail.com', 'mdp',
                                    'baptched')
        organisateur.set_nom_utilisateur('baptched2')
        self.assertEqual(organisateur.get_nom_utilisateur(), 'baptched2')

    def test_str(self):
        """
        Test de la fonction __str__ de la classe Organisateur
        """
        organisateur = Organisateur(1, 'Baptiste', 'Chédeville',
                                    'baptiste.chedevill@gmail.com', 'mdp',
                                    'baptched')
        sortie = ('Organisateur : 1 - Baptiste - Chédeville - '
                  'baptiste.chedevill@gmail.com - mdp - baptched |')
        self.assertEqual(str(organisateur), sortie)
