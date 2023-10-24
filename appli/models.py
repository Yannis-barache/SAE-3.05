import sqlalchemy
from sqlalchemy import text
from appli.modele.organisateur import Organisateur

def ouvrir_connexion(user,passwd,host,database):
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
        #creation de l'objet gérant les interactions avec le serveur de BD
        engine=sqlalchemy.create_engine('mysql+mysqlconnector://'+user+':'+passwd+'@'+host+'/'+database)
        #creation de la connexion
        cnx = engine.connect()
    except Exception as err:
        print(err)
        raise err
    print("connexion réussie")
    return cnx


def get_orga(connexion):

    query = text("SELECT  idOrganisateur, nomOrganisateur, prenomOrganisateur, adresseMailOrganisateur, mdpOrganisateur, nomUtilisateur FROM ORGANISATEUR")
    result = connexion.execute(query)
    organisateurs=[]
    for idO,nomO,prenomO,adresseMail,mdp,nomU in result:
        organisateurs.append(Organisateur(idO,nomO,prenomO,adresseMail,mdp,nomU))
    return organisateurs

