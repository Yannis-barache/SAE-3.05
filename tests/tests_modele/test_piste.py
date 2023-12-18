"""
Module de test de la classe Piste
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from piste import Piste


class TestPiste(unittest.TestCase):
    """
    Classe de test de la classe ïste
    """

    def test_constructeur(self):
        """
        Test du constructeur de la classe Piste
        """
        piste = Piste(1, 1, 'Piste 1')
        self.assertIsInstance(piste, Piste)

    def test_get_id_piste(self):
        """
        Test de la fonction get_id_piste de la classe Piste
        """
        piste = Piste(1, 1, 'Piste 1')
        self.assertEqual(piste.get_id_piste(), 1)

    def test_get_id_lieu(self):
        """
        Test de la fonction get_id_lieu de la classe Piste
        """
        piste = Piste(1, 1, 'Piste 1')
        self.assertEqual(piste.get_id_lieu(), 1)

    def test_get_description(self):
        """
        Test de la fonction get_description de la classe Piste
        """
        piste = Piste(1, 1, 'Piste 1')
        self.assertEqual(piste.get_description(), 'Piste 1')

    def test_set_id_piste(self):
        """
        Test de la fonction set_id_piste de la classe Piste
        """
        piste = Piste(1, 1, 'Piste 1')
        piste.set_id_piste(2)
        self.assertEqual(piste.get_id_piste(), 2)

    def test_set_id_lieu(self):
        """
        Test de la fonction set_id_lieu de la classe Piste
        """
        piste = Piste(1, 1, 'Piste 1')
        piste.set_id_lieu(2)
        self.assertEqual(piste.get_id_lieu(), 2)

    def test_set_description(self):
        """
        Test de la fonction set_description de la classe Piste
        """
        piste = Piste(1, 1, 'Piste 1')
        piste.set_description('Piste 2')
        self.assertEqual(piste.get_description(), 'Piste 2')

    def test_str(self):
        """
        Test de la fonction __str__ de la classe Piste
        """
        piste = Piste(1, 1, 'Piste 1')
        self.assertEqual(str(piste), 'Piste : id = 1, idLieu = 1, description = Piste 1')
