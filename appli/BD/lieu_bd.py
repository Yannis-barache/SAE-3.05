"""
    Fichier qui contient les requêtes SQL pour la table Lieu
"""

import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from lieu import Lieu


class LieuBD:
    """
    Classe LieuBD
    """

    def __init__(self, connexion):
        self.__connexion = connexion

    def get_all_lieu(self):
        """
        Fonction qui retourne tous les lieux
        :return: liste de Lieu
        """
        try:
            query = text(
                'SELECT idLieu, adresseLieu, descriptionLieu FROM LIEU')
            result = self.__connexion.execute(query)
            lieux = []
            for id_lieu, adresse, description in result:
                lieux.append(Lieu(id_lieu, description, adresse))
            return lieux
        except Exception as e:
            print(e)
            return None

    def get_all_lieu2(self):
        """
        Fonction qui retourne tous les lieux
        :return: liste de Lieu
        """
        try:
            query = text(
                'SELECT idLieu, adresseLieu, descriptionLieu FROM LIEU')
            result = self.__connexion.execute(query)
            lieux = []
            for id_lieu, adresse, description in result:
                nombre_pistes = self.get_nombre_pistes_by_lieu(id_lieu)
                nombre_compets = self.get_nombre_competitions_by_lieu(id_lieu)
                lieux.append((Lieu(id_lieu, description, adresse), nombre_pistes, nombre_compets))
            return lieux
        except Exception as e:
            print(e)
            return None

    def get_nombre_pistes_by_lieu(self, id_lieu: int):
        """
        Fonction qui retourne le nombre de pistes en fonction de l'id du lieu
        :param id_lieu: id du lieu
        :return: nombre de pistes
        """
        try:
            query = text(
                'SELECT COUNT(*) FROM PISTE WHERE idLieu =' +
                str(id_lieu))
            result = self.__connexion.execute(query)
            for nombre_pistes in result:
                return nombre_pistes[0]
            return None
        except Exception as e:
            print(e)
            return None

    def get_nombre_competitions_by_lieu(self, id_lieu: int):
        """
        Fonction qui retourne le nombre de compétitions en fonction de l'id du lieu
        :param id_lieu: id du lieu
        :return: nombre de compétitions
        """
        try:
            query = text(
                'SELECT COUNT(*) FROM COMPETITION WHERE idLieu =' +
                str(id_lieu))
            result = self.__connexion.execute(query)
            for nombre_competitions in result:
                return nombre_competitions[0]
            return None
        except Exception as e:
            print(e)
            return None

    def get_lieu_by_id(self, id_l: int):
        """
        Fonction qui retourne un lieu en fonction de son id
        :param id_l: id du lieu
        :return: lieu
        """
        try:
            query = text('SELECT idLieu, adresseLieu, '
                         'descriptionLieu FROM LIEU WHERE idLieu =' +
                         str(id_l))
            result = self.__connexion.execute(query)
            for id_lieu, adresse, description in result:
                return Lieu(id_lieu, description, adresse)
            return None
        except Exception as e:
            print(e)
            return None

    def insert_lieu(self, lieu: Lieu):
        """
        Fonction qui insère un lieu
        :param lieu : lieu
        """
        try:
            query = text(
                f"INSERT INTO LIEU (adresseLieu, descriptionLieu) VALUES "
                f"('{lieu.get_adresse()}','{lieu.get_description()}')")
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None

    def delete_lieu(self, id_lieu: int):
        """
        Fonction qui supprime un lieu
        :param lieu: lieu
        """
        try:
            query = text(
                f"DELETE FROM LIEU WHERE idLieu = {id_lieu}")
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None

    def update_lieu(self, lieu: Lieu):
        """
        Fonction qui met à jour un lieu
        :param lieu: lieu
        """
        try:
            if '\'' in lieu.get_description():
                lieu.set_description(lieu.get_description().replace('\'', '\'\''))
            if '\'' in lieu.get_adresse():
                lieu.set_adresse(lieu.get_adresse().replace('\'', '\'\''))
            query = text(
                f"UPDATE LIEU SET adresseLieu = '{lieu.get_adresse()}', "
                f"descriptionLieu = '{lieu.get_description()}' WHERE idLieu = {lieu.get_id()}")
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None

    def delete_lieu_by_addresse(self, lieu: Lieu):
        """
        Fonction qui supprime un lieu en fonction de son adresse
        :param lieu: lieu
        """
        try:
            query = text(
                f"DELETE FROM LIEU WHERE adresseLieu = '{lieu.get_adresse()}'")
            self.__connexion.execute(query)
            self.__connexion.commit()
        except Exception as e:
            print(e)
            return None
