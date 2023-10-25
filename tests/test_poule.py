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

    def test_set_id(self):
        """
        Test de la fonction set_id de la classe Poule
        """
        poule = Poule(1)
        poule.set_id(2)
        self.assertEqual(poule.get_id(), 2)

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

    def test_str(self):
        """
        Test de la fonction __str__ de la classe Poule
        """
        poule = Poule(1)
        self.assertEqual(str(poule), '1')
