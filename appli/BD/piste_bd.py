"""
    Fichier qui contient les requêtes SQL pour la table Piste
"""

from sqlalchemy import text
import sys
import os
from lieu_bd import LieuBD


ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from piste import Piste


class PisteBD:
    """
    Classe PisteBD
    """
    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_piste(self):
        """
        Fonction qui retourne toutes les pistes
        :return: liste de pistes
        """
        try:
            query = text('SELECT idPiste, idLieu, descriptionPiste FROM PISTE')
            result = self.__connexion.execute(query)
            pistes = []

            for (id_piste, id_lieu, description_piste) in result:
                lieu = LieuBD(self.__connexion).get_lieu_by_id(id_lieu)
                pistes.append(Piste(id_piste, lieu, description_piste))
            return pistes
        except Exception as e:
            print(e)
            return None

    def get_piste_by_id(self, id_p: int):
        """
        Fonction qui retourne une piste en fonction de son id
        :param id_p: id de la piste
        :return: piste
        """
        try:
            query = text('SELECT idPiste, idLieu, descriptionPiste FROM PISTE WHERE idPiste = :id')
            result = self.__connexion.execute(query, id=id_p)
            for (id_piste, id_lieu, description_piste) in result:
                lieu = LieuBD(self.__connexion).get_lieu_by_id(id_lieu)
                return Piste(id_piste, lieu, description_piste)
        except Exception as e:
            print(e)
            return None

    def get_piste_by_lieu(self, lieu: str):
        """
        Fonction qui retourne une piste en fonction de son lieu
        :param lieu: lieu de la piste
        :return: piste
        """
        try:
            query = text('SELECT idPiste, idLieu, descriptionPiste FROM PISTE WHERE idLieu = :lieu')
            result = self.__connexion.execute(query, lieu=lieu)
            for (id_piste, id_lieu, description_piste) in result:
                lieu = LieuBD(self.__connexion).get_lieu_by_id(id_lieu)
                return Piste(id_piste, lieu, description_piste)
        except Exception as e:
            print(e)

        return None
