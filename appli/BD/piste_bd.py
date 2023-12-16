"""
Fichier qui contient les requêtes SQL pour la table PISTE
"""

import sys
import os
from sqlalchemy import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from piste import Piste
from lieu import Lieu


class PisteBD:
    """
    Classe PistesBD
    """

    def __init__(self, connexion):
        self.__connexion = connexion

    def get_piste_by_id(self, id_piste: int):
        """
        Fonction qui retourne une piste en fonction de son id
        :param id_piste: id de la piste
        :return: piste
        """
        try:
            query = text(
                'SELECT idPiste, idLieu, descriptionPiste FROM PISTE WHERE idPiste = '
                + str(id_piste))
            result = self.__connexion.execute(query)
            for (id_pistee, id_lieu, description_piste) in result:
                return Piste(int(id_pistee), int(id_lieu), description_piste)
        except Exception as e:
            print(e)
            return None

    def get_piste_by_lieu(self, lieu: Lieu):
        """
        Fonction qui retourne toutes les pistes d'un lieu
        :param lieu: lieu
        :return: liste de pistes
        """
        try:
            query = text(
                'SELECT idPiste, idLieu, descriptionPiste FROM PISTE WHERE idLieu = '
                + str(lieu.get_id()))
            result = self.__connexion.execute(query)
            pistes = []
            for (id_piste, id_lieu, description_piste) in result:
                pistes.append(
                    Piste(int(id_piste), int(id_lieu), description_piste))
            return pistes
        except Exception as e:
            print(e)
            return None
