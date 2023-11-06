import flask
from sqlalchemy import text

from .app import app
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField , HiddenField, PasswordField,IntegerField
from wtforms.validators import DataRequired,NumberRange
from modele.connexion_bd import ConnexionBD
from .models import load_user

connexion_vers_bd = ConnexionBD()
class ConnexionFormE(FlaskForm):
    identifiant = IntegerField("Votre numéro de licence",validators=[DataRequired(),NumberRange(min=0, max=999999999)])
    mdp = PasswordField("Mot de passe", validators=[DataRequired()])
    next = HiddenField()

class ConnexionForm(FlaskForm):
    identifiant = StringField("Votre nom",validators=[DataRequired()])
    mdp = PasswordField("Mot de passe", validators=[DataRequired()])
    next = HiddenField()


# @app.route("/")
# def home():
#     return render_template(
#         "home.html"
#     )

@app.route("/")
def choose_sign():
    return render_template(
        "connexion_inscription.html"
    )


@app.route("/choisir_statut_connexion", methods=["GET", "POST"])
def choisir_statut_connexion():
    return render_template(
        "choisir_statut_connexion.html"
    )

@app.route("/choisir_statut_inscription")
def choisir_statut_inscription():
    return render_template(
        "choisir_statut_inscription.html"
    )

@app.route("/inscription")
def inscription():
    return render_template(
        "page_inscription.html"
    )

@app.route("/connexion/<nom>", methods=["GET", "POST"])
def connexion(nom):
    connexion_vers_bd.ouvrir_connexion()
    if nom != "ORGANISATEUR" and nom != "ESCRIMEUR" and nom != "CLUB":
        flask.abort(404)
    form = ConnexionForm()
    if nom == "ESCRIMEUR":
        form = ConnexionFormE()
    if form.validate_on_submit():
        identifiant = form.identifiant.data
        mdp = form.mdp.data
        try:
            if nom == "ESCRIMEUR":
                # On vérifie que le mot de passe correspond à l'identifiant
                query = text('SELECT * FROM ESCRIMEUR WHERE licence = :identifiant AND mdpEscrimeur = :mdp')
                resultat = connexion_vers_bd.get_connexion().execute(query, {"identifiant": identifiant, "mdp": mdp})
                if resultat.rowcount == 1:
                    user=load_user(identifiant,nom)

                print(user)
            elif nom == "CLUB":
                # Créez une requête SQL avec un paramètre nommé :identifiant
                query = text('SELECT idClub FROM CLUB WHERE nomClub = :identifiant')

                # Exécutez la requête en spécifiant les paramètres
                resultat = connexion_vers_bd.get_connexion().execute(query, {"identifiant": identifiant})
                identifiant = resultat.fetchone()[0]
                print(identifiant)
            else:
                resultat = connexion_vers_bd.get_connexion().execute("SELECT * FROM ORGANISATEUR WHERE nomUtilisateur = %s", (identifiant))

        except Exception as err:
            print(err)
            raise err

        user = load_user(identifiant,nom)
        print("USER ",user)
        return render_template("home.html", nom=user)

    return render_template("page_connexion.html", nom=nom, form=form)
