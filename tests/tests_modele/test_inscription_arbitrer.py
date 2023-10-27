"""
Module de test de la classe InscrireArbitre
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from inscrire_arbitre import InscrireArbitre


class TestInscrireArbitre(unittest.TestCase):
    """
    Classe de test de la classe InscrireArbitre
    """

    def test_constructeur(self):
        """
        Test du constructeur de la classe InscrireArbitre
        """
        arbitrer = InscrireArbitre(1, 1)
        self.assertIsInstance(arbitrer, InscrireArbitre)

    def test_get_id_arbitre(self):
        """
        Test de la fonction get_id_arbitre de la classe InscrireArbitre
        """
        arbitrer = InscrireArbitre(1, 1)
        self.assertEqual(arbitrer.get_id_arbitre(), 1)

    def test_get_id_competition(self):
        """
        Test de la fonction get_id_competition de la classe InscrireArbitre
        """
        arbitrer = InscrireArbitre(1, 1)
        self.assertEqual(arbitrer.get_id_competition(), 1)

    def test_set_id_arbitre(self):
        """
        Test de la fonction set_id_arbitre de la classe InscrireArbitre
        """
        arbitrer = InscrireArbitre(1, 1)
        arbitrer.set_id_arbitre(2)
        self.assertEqual(arbitrer.get_id_arbitre(), 2)

    def test_set_id_competition(self):
        """
        Test de la fonction set_id_competition de la classe InscrireArbitre
        """
        arbitrer = InscrireArbitre(1, 1)
        arbitrer.set_id_competition(2)
        self.assertEqual(arbitrer.get_id_competition(), 2)

    def test_str(self):
        """
        Test de la fonction __str__ de la classe InscrireArbitre
        """
        arbitrer = InscrireArbitre(1, 1)
        self.assertEqual(str(arbitrer), 'Arbitre : 1 - 1 |')
