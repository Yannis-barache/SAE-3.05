"""
Module contenant la classe PhaseFinal
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from phase_final import PhaseFinal
from match import Match
from escrimeur import Escrimeur
from categorie import Categorie
from club import Club


class TestPhaseFinal(unittest.TestCase):
    """
    Classe de test de la classe PhaseFinal

    Args:
        unittest (TestCase): Classe de base pour les tests unitaires intégrés
    """

    def test_constructeur(self):
        """
        Test du constructeur de la classe PhaseFinal
        """
        phase_final = PhaseFinal(1)
        self.assertIsInstance(phase_final, PhaseFinal)

    def test_get_id_phase_f(self):
        """
        Test de la fonction get_id_phase_f de la classe PhaseFinal
        """
        phase_final = PhaseFinal(1)
        self.assertEqual(phase_final.get_id_phase_f(), 1)

    def test_get_les_matchs(self):
        """
        Test de la fonction get_les_matchs de la classe PhaseFinal
        """
        phase_final = PhaseFinal(1)
        self.assertEqual(phase_final.get_les_matchs(), [])

    def test_set_id_phase_f(self):
        """
        Test de la fonction set_id_phase_final de la classe PhaseFinal
        """
        phase_final = PhaseFinal(1)
        phase_final.set_id_phase_f(2)
        self.assertEqual(phase_final.get_id_phase_f(), 2)

    def test_est_finis(self):
        """
        Test de la fonction est_finis de la classe PhaseFinal
        """
        phase_final = PhaseFinal(1)
        self.assertFalse(phase_final.est_finis())
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
        phase_final.set_match(match)
        self.assertFalse(phase_final.est_finis())

    def test_str(self):
        """
        Test de la fonction __str__ de la classe PhaseFinal
        """
        phase_final = PhaseFinal(1)
        self.assertEqual(str(phase_final), 'Phase finale : 1 |')
