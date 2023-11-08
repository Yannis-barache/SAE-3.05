"""
Module contenant la classe ConnexionBD qui permet de se connecter à la base de données
"""
import sqlalchemy
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from constantes import locale


class ConnexionBD:
    """
    Classe ConnexionBD

    Attributes:
        __connexion (sqlalchemy.engine.base.Connection): connexion à la base de données
        __user (str): le login MySQL de l'utilsateur
        __passwd (str): le mot de passe MySQL de l'utilisateur
        __host (str): le nom ou l'adresse IP de la machine hébergeant le serveur MySQL
        __database (str): le nom de la base de données à utiliser
    """

    def __init__(self):
        if not locale:
            self.__connexion = None
            self.__user = "332948"
            self.__passwd = "SAE-EscrimeBUT2&"
            self.__host = "mysql-sae-escrime.alwaysdata.net"
            self.__database = "sae-escrime_sae"
        elif locale:
            self.__connexion = None
            self.__user = "barache"
            self.__passwd = "barache"
            self.__host = "servinfo-maria"
            self.__database = "DBbarache"
        else:
            raise AttributeError(
                "Erreur de configuration de la base de données")
        self.ouvrir_connexion()

    def ouvrir_connexion(self, con: bool = True):
        """
        ouverture d'une connexion MySQL
        paramètres:
           user     (str) le login MySQL de l'utilsateur
           passwd   (str) le mot de passe MySQL de l'utilisateur
           host     (str) le nom ou l'adresse IP de la machine hébergeant le serveur MySQL
           database (str) le nom de la base de données à utiliser
        résultat: l'objet qui gère le connection MySQL si tout s'est bien passé
        """
        try:
            if con:
                # creation de l'objet gérant les interactions avec le serveur de BD
                engine = sqlalchemy.create_engine("mysql+mysqlconnector://" +
                                                  self.__user + ":" +
                                                  self.__passwd + "@" +
                                                  self.__host + "/" +
                                                  self.__database)
            # creation de la connexion
            cnx = engine.connect()
            print("connexion réussie")
            self.__connexion = cnx
        except Exception as err:
            print(err)
            raise err

    def get_connexion(self):
        return self.__connexion

    def fermer_connexion(self):
        self.__connexion.close()
        print("connexion fermée")
