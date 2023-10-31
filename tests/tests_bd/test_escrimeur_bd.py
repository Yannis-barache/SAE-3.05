"""
Module de test de la classe EscrimeurBD
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'tests/tests_bd'))

from test_bd import TestBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/BD'))

from escrimeur_bd import EscrimeurBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from escrimeur import Escrimeur


class TestEscrimeurBD(TestBD, unittest.TestCase):
    """
    Classe de test de la classe EscrimeurBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    def test_constructeur(self):
        """
        Test du constructeur de la classe EscrimeurBD
        """
        self.assertIsInstance(self.modele.get_escrimeur_bd(), EscrimeurBD)

    def test_get_all_escrimeur(self):
        """
        Test de la méthode get_all_escrimeur
        """
        escrimeurs = self.modele.get_escrimeur_bd().get_all_escrimeur()
        self.assertIsInstance(escrimeurs, list)

    def test_get_escrimeur_by_id(self):
        """
        Test de la méthode get_escrimeur_by_id
        """
        escrimeur = self.modele.get_escrimeur_bd().get_escrimeur_by_id(1)
        self.assertIsInstance(escrimeur, Escrimeur)
        escrimeur = self.modele.get_escrimeur_bd().get_escrimeur_by_id(-1)
        self.assertIsNone(escrimeur)
        self.modele.fermer_connexion()
