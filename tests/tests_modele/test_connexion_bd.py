"""
Module de test de la classe ConnexionBD
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from connexion_bd import ConnexionBD


class TestConnexionBD(unittest.TestCase):
    """
    Classe de test de la classe ConnexionBD

    Args:
        unittest (TestCase): classe de base pour les tests unitaires intégrés
    """

    @classmethod
    def setUpClass(cls):
        cls.connexion = ConnexionBD()
        text = 'Distante'
        # changer la viriable "locale" dans le fichier constante.py
        with open('appli/modele/constantes.py', 'r', encoding="utf-8") as file:
            lines = file.readlines()
        with open('appli/modele/constantes.py', 'w', encoding="utf-8") as file:
            for line in lines:
                if line.startswith('locale = '):
                    file.write(f'locale = {text}\n')
                else:
                    file.write(line)

    @classmethod
    def tearDownClass(cls):
        text = "''"
        # changer la variable "locale" dans le fichier constante.py
        with open('appli/modele/constantes.py', 'r', encoding="utf-8") as file:
            lines = file.readlines()
        with open('appli/modele/constantes.py', 'w', encoding="utf-8") as file:
            for line in lines:
                if line.startswith('locale = '):
                    file.write(f'locale = {text}\n')
                else:
                    file.write(line)

    def test_constructeur_connexion(self):
        """
        Test du constructeur de la classe ConnexionBD
        """
        self.assertIsNotNone(self.connexion)

    def test_constructeur_connexion_iut(self):
        """
        Test du constructeur de la classe ConnexionBD en local
        """
        with open('appli/modele/constantes.py', 'r', encoding="utf-8") as file:
            lines = file.readlines()
        with open('appli/modele/constantes.py', 'w', encoding="utf-8") as file:
            for line in lines:
                if line.startswith('locale = '):
                    file.write(f'locale = {True}\n')
                else:
                    file.write(line)
        connexion = ConnexionBD()
        self.assertIsNotNone(connexion)
        with open('appli/modele/constantes.py', 'r', encoding="utf-8") as file:
            lines = file.readlines()
        with open('appli/modele/constantes.py', 'w', encoding="utf-8") as file:
            for line in lines:
                if line.startswith('locale = '):
                    file.write(f'locale = {False}\n')
                else:
                    file.write(line)

    def test_creation_connexion(self):
        """
        Test de la création d'une connexion
        """
        self.assertIsNotNone(self.connexion)

    def test_ouverture_connexion(self):
        """
        Test de l'ouverture d'une connexion
        """
        self.connexion.ouvrir_connexion()
        self.assertIsNotNone(self.connexion.get_connexion())
        with self.assertRaises(Exception):
            self.connexion.ouvrir_connexion(False)

    def test_fermeture_connexion(self):
        """
        Test de la fermeture d'une connexion
        """
        self.connexion.fermer_connexion()
        self.assertIsNotNone(self.connexion.get_connexion())

    def test_get_connexion(self):
        """
        Test de la récupération de la connexion
        """
        self.connexion.ouvrir_connexion()
        self.assertIsNotNone(self.connexion.get_connexion())

if __name__ == '__main__':
    unittest.main()
