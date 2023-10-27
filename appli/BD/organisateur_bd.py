"""
    Fichier qui contient les requêtes SQL pour la table ORGANISATEUR
"""

from sqlalchemy.sql.expression import text
from appli.modele.organisateur import Organisateur


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
