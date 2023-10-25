from appli.modele.escrimeur import Escrimeur
from sqlalchemy import text
from appli.BD.club_bd import ClubBD
from appli.BD.categorie_bd import CategorieBD


class EscrimeurBD:
    def __int__(self, connexion):
        self.__connexion = connexion

    def get_all_escrimeur(self):
        try:
            query = text("SELECT idEscrimeur, nomEscrimeur, licence, prenomEscrimeur, dateNaissance, "
                         "nomUtilisateurEscrimeur, mdpEscrimeur, classement, sexeEscrimeur, "
                         "idClub, idCategorie FROM ESCRIMEUR")
            result = self.__connexion.execute(query)
            escrimeurs = []
            for id_escrimeur, nom, licence, prenom, date_naissance, nom_utilisateur, mdp, classement, sexe, id_club, id_categorie in result:
                club = ClubBD.get_club_by_id(self, id_club)
                categorie = CategorieBD.get_categorie_by_id(self, id_categorie)
                escrimeurs.append(Escrimeur(id_escrimeur, nom, prenom, sexe, date_naissance, nom_utilisateur, mdp, licence, classement, club, categorie))
            return escrimeurs
        except Exception as e:
            print(e)
            return None

    def get_escrimeur_by_id(self, id):
        try:
            query = text("SELECT idEscrimeur, nomEscrimeur, licence, prenomEscrimeur, dateNaissance, "
                         "nomUtilisateurEscrimeur, mdpEscrimeur, classement, sexeEscrimeur, "
                         "idClub, idCategorie FROM ESCRIMEUR WHERE idEscrimeur = :id")
            result = self.__connexion.execute(query, id=id)
            for id_escrimeur, nom, licence, prenom, date_naissance, nom_utilisateur, mdp, classement, sexe, id_club, id_categorie in result:
                club = ClubBD.get_club_by_id(self, id_club)
                categorie = CategorieBD.get_categorie_by_id(self, id_categorie)
                return Escrimeur(id_escrimeur, nom, prenom, sexe, date_naissance, nom_utilisateur, mdp, licence, classement, club, categorie)
            return None
        except Exception as e:
            print(e)
            return None
