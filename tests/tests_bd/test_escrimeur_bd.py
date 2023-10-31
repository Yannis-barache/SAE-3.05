"""
Module de test de la classe EscrimeurBD
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/BD'))

from escrimeur_bd import EscrimeurBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from modele_appli import ModeleAppli
from escrimeur import Escrimeur


class TestEscrimeurBD(unittest.TestCase):
    """
    Classe de test de la classe EscrimeurBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    @classmethod
    def setUpClass(cls):
        cls.modele = ModeleAppli()
        cls.escrimeur_bd = cls.modele.get_escrimeur_bd()

    def test_constructeur(self):
        """
        Test du constructeur de la classe EscrimeurBD
        """
        self.assertIsInstance(self.escrimeur_bd, EscrimeurBD)

    def test_get_all_escrimeur(self):
        """
        Test de la méthode get_all_escrimeur
        """
        escrimeurs = self.escrimeur_bd.get_all_escrimeur()
        self.assertIsInstance(escrimeurs, list)

    def test_get_escrimeur_by_id(self):
        """
        Test de la méthode get_escrimeur_by_id
        """
        escrimeur = self.escrimeur_bd.get_escrimeur_by_id(1)
        self.assertIsInstance(escrimeur, Escrimeur)
        escrimeur = self.escrimeur_bd.get_escrimeur_by_id(-1)
        self.assertIsNone(escrimeur)
