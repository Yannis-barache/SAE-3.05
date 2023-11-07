"""
Module de test de la classe InscrireBD
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/BD'))

from inscrire_bd import InscrireBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from modele_appli import ModeleAppli


class TestInscrireBD(unittest.TestCase):
    """
    Classe de test de la classe InscrireBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    def test_constructeur(self):
        """
        Test du constructeur de la classe InscrireBD
        """
        modele = ModeleAppli()
        self.assertIsInstance(modele.get_inscrire_bd(), InscrireBD)

    def test_get_all_inscrire(self):
        """
        Test de la méthode get_all_inscrire
        """
        modele = ModeleAppli()
        inscrires = modele.get_inscrire_bd().get_all_inscrire()
        self.assertIsInstance(inscrires, list)
