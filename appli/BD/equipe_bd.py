"""
    Fichier qui contient les requêtes SQL pour la table Equipe
"""

import sys
import os
from sqlalchemy.sql.expression import text

from escrimeur_bd import EscrimeurBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from equipe import Equipe
from escrimeur import Escrimeur


class EquipeBD:
    """
    Classe EquipeBD
    """

    def __init__(self, connexion):
        self.__connexion = connexion

    def get_escrimeur_by_equipe(self, id_equipe) -> list[Escrimeur]:
        """
        Fonction qui retourne tous les escrimeurs d'une équipe
        :param id_equipe: id de l'équipe
        :return: liste d'escrimeurs
        """
        try:
            query = text(f'SELECT idEscrimeur FROM FAIT_PARTIE WHERE idEquipe = {id_equipe}')
            result = self.__connexion.execute(query)
            escrimeurs = []
            escrimeur_db = EscrimeurBD(self.__connexion)
            for (id_escrimeur, ) in result:
                escrimeurs.append(escrimeur_db.get_escrimeur_by_id(id_escrimeur))
            return escrimeurs
        except Exception as e:
            print(e)
            return None