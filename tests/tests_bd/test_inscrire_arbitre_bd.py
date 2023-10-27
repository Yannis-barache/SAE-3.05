"""
Module de test de la classe InscrireArbitreBD
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/BD'))

from inscrire_arbitre_bd import InscrireArbitreBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from modele_appli import ModeleAppli
from inscrire_arbitre import InscrireArbitre


class TestInscrireArbitreBD(unittest.TestCase):
    """
    Classe de test de la classe InscrireArbitreBD

    Args:
        unittest (unittest): La classe de test unitaire
    """

    def test_constructeur(self):
        """
        Test du constructeur de la classe InscrireArbitreBD
        """
        modele = ModeleAppli()
        self.assertIsInstance(modele.get_inscrire_arbitre_bd(),
                              InscrireArbitreBD)

    def test_get_all_inscrire_arbitre(self):
        """
        Test de la méthode get_all_inscrire_arbitre
        """
        modele = ModeleAppli()
        inscrire_arbitres = modele.get_inscrire_arbitre_bd().get_all_arbitre()
        self.assertIsInstance(inscrire_arbitres, list)

    def test_get_inscrire_arbitre_by_id(self):
        """
        Test de la méthode get_inscrire_arbitre_by_id
        """
        modele = ModeleAppli()
        inscrire_arbitre = modele.get_inscrire_arbitre_bd().get_arbitre_by_id(
            1)
        self.assertIsInstance(inscrire_arbitre, InscrireArbitre)
        inscrire_arbitre = modele.get_inscrire_arbitre_bd().get_arbitre_by_id(
            -1)
        self.assertIsNone(inscrire_arbitre)
