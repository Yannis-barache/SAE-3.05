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
                'SELECT idOrganisateur, nomOrganisateur, prenomOrganisateur, '
                'adresseMailOrganisateur, mdpOrganisateur, '
                'nomUtilisateur FROM ORGANISATEUR')
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

    def login_organisateur(self, login_organisateur: str, login_mdp: str) -> Organisateur:
        """
        Fonction qui vérifie les identifiants de l'organisateur
        :param login_organisateur: nom de l'organisateur
        :param login_mdp: mot de passe de l'organisateur
        :return: organisateur
        """
        try:
            query = text(
                f"SELECT idOrganisateur, nomOrganisateur, prenomOrganisateur, "
                f"adresseMailOrganisateur, mdpOrganisateur, nomUtilisateur "
                f" FROM ORGANISATEUR WHERE nomUtilisateur = '{login_organisateur}'")
            result = self.__connexion.execute(query)
            for (id_organisateur, nom, prenom, mail, mpd,
                 nom_utilisateur) in result:

                fonction = text('SELECT verif_mdp_organisateur(:id, :mdp)')
                resultat = self.__connexion.execute(fonction, {"id": id_organisateur, "mdp": login_mdp})

                if resultat.fetchone()[0] == 0:
                    return None

                return Organisateur(id_organisateur, nom, prenom, mail, mpd,
                                 nom_utilisateur)
            return None
        except Exception as e:
            print(e)
            return None
