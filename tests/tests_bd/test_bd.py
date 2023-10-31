"""
Module d'initialisation des tests de la BD
"""

import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from modele_appli import ModeleAppli

class TestBD():
    """
    Classe de test de la BD
    """

    def __init__(self, *args, **kwargs):
        """
            Constructeur de la classe de test de la BD
        """
        super(TestBD, self).__init__(*args, **kwargs)
        self.modele = ModeleAppli()
