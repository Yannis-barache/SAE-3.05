from sqlalchemy.sql.expression import text
from appli.modele.club import Club


class ClubBD:
    def __int__(self, connexion):
        self.__connexion = connexion

    def get_all_club(self):
        try:
            query = text("SELECT idClub, nomClub, adresse, mdpClub FROM CLUB")
            result = self.__connexion.execute(query)
            clubs = []
            for id_club, nom, adresse, mdp in result:
                clubs.append(Club(id_club, nom, adresse, mdp))
            return clubs
        except Exception as e:
            print(e)
            return None

    def get_club_by_id(self, id):
        try:
            query = text("SELECT idClub, nomClub, adresse, mdpClub FROM CLUB WHERE idClub = :id")
            result = self.__connexion.execute(query, id=id)
            for id_club, nom, adresse, mdp in result:
                return Club(id_club, nom, adresse, mdp)
            return None
        except Exception as e:
            print(e)
            return None
