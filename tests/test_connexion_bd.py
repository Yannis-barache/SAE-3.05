"""
Module de test de la classe ConnexionBD
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

#from connexion_bd import ConnexionBD


class TestConnexionBD(unittest.TestCase):
    """
    def test_creation_connexion(self):
        # Vérifie que la création de l'objet ConnexionBD fonctionne sans erreur
        connexion = ConnexionBD()

    def test_ouverture_connexion(self):
        # Vérifie que l'ouverture de la connexion fonctionne sans erreur
        connexion = ConnexionBD()
        connexion.ouvrir_connexion()
        connexion.fermer_connexion()

    def test_fermeture_connexion(self):
        # Vérifie que la fermeture de la connexion fonctionne sans erreur
        connexion = ConnexionBD()
        connexion.ouvrir_connexion()
        connexion.fermer_connexion()
    """
