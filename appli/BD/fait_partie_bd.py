"""
Fichier qui contient les requêtes SQL pour la table EQUIPE
"""

import sys
import os
from sqlalchemy.sql.expression import text

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/BD'))
from escrimeur_bd import EscrimeurBD

class FaitPartieBD:
    """
        Classe FaitPartieBD

        Methods :
            __init__(self, connexion)
            get_fait_partie_equipe(self, id_equipe: int)
    """

    def __init__(self, connexion):
        """
        Constructeur de la classe EquipeBD
        :param connexion: connexion à la base de données
        """
        self.__connexion = connexion

    def get_fait_partie_equipe(self, id_equipe: int) -> list | None:
        """
        Fonction qui retourne les id des tireurs qui font partie d'une équipe
        :param id_equipe: id de l'équipe
        :return: liste d'id de tireurs
        """
        try:
            query = text('SELECT idEscrimeur FROM FAIT_PARTIE WHERE idEquipe =' + str(id_equipe))
            result = self.__connexion.execute(query)
            id_escrimeurs = []
            escrimeur_bd = EscrimeurBD(self.__connexion)
            for id_escrimeur in result:
                id_escrimeurs.append(escrimeur_bd.get_escrimeur_by_id(int(id_escrimeur)))
            return id_escrimeurs
        except Exception as e:
            print(e)
            return None

    def modif_composition(self, id_equipe: int, id_tireur: int, role: str):
        """
        Fonction qui modifie la composition d'une équipe
        :param id_equipe: id de l'équipe
        :param id_tireur: id du tireur
        """
        try:
            query = text('INSERT INTO FAIT_PARTIE (idEquipe, idEscrimeur,role) VALUES (:id_equipe, :id_tireur, :role)')
            self.__connexion.execute(query, {'id_equipe': id_equipe, 'id_tireur': id_tireur, 'role': role})
            self.__connexion.commit()
            print("Ajouté")
        except Exception as e:
            print(e)
            return None
