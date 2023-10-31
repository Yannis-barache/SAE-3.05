"""
Module de test de la classe OrganisateurBD
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'tests/tests_bd'))

from test_bd import TestBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/BD'))

from organisateur_bd import OrganisateurBD


class TestOrganisateurBD(TestBD, unittest.TestCase):
    """
    Classe de test de la classe OrganisateurBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    def test_constructeur(self):
        """
        Test du constructeur de la classe OrganisateurBD
        """
        self.assertIsInstance(self.modele.get_organisateur_bd(), OrganisateurBD)

    def test_get_all_organisateur(self):
        """
        Test de la méthode get_all_organisateur
        """
        organisateurs = self.modele.get_organisateur_bd().get_all_organisateur()
        self.assertIsInstance(organisateurs, list)
        self.modele.fermer_connexion()
