"""
    Fichier qui contient les requêtes SQL pour la table ORGANISATEUR
"""

import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from organisateur import Organisateur


class OrganisateurBD:
    """
    Classe OrganisateurBD
    """

    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_organisateur(self):
        """
        Fonction qui retourne tous les organisateurs
        :return: liste d'organisateur
        """
        try:
            query = text(
                "SELECT idOrganisateur, nomOrganisateur, prenomOrganisateur, "
                "adresseMailOrganisateur, mdpOrganisateur, "
                "nomUtilisateur FROM ORGANISATEUR")
            result = self.__connexion.execute(query)
            organisateurs = []
            for (id_organisateur, nom, prenom, mail, mpd,
                 nom_utilisateur) in result:
                organisateurs.append(
                    Organisateur(id_organisateur, nom, prenom, mail, mpd,
                                 nom_utilisateur))
            return organisateurs
        except Exception as e:
            print(e)
            return None
