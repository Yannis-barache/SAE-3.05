from modele.connexion_bd import ConnexionBD
from .app import login_manager
from BD.club_bd import ClubBD

@login_manager.user_loader
def load_user(user_id, user_type):
    try:
        resultat = None
        connexion = ConnexionBD()
        connexion.ouvrir_connexion()

        if user_type == "ORGANISATEUR":
            resultat = connexion.get_connexion().execute("SELECT * FROM %s WHERE id_organisateur = %s", (user_type,user_id))

        elif user_type == "ESCRIMEUR":
            requete = ("SELECT * FROM ESCRIMEUR WHERE licence = %s", int(user_id))
            print(requete)
            resultat=connexion.get_connexion().execute(requete)

        elif user_type == "CLUB":
            club = ClubBD(connexion.get_connexion())
            club_id = club.get_club_by_id(user_id)
            print(club_id)
            return club_id

        if resultat.rowcount == 1:
            user = resultat.fetchone()
            connexion.fermer_connexion()
            return user
        else:
            connexion.fermer_connexion()
            print("pas de user")
            return None
    except Exception as err:
        print(err)
        raise err




