import flask
import sys
import os
from .app import app
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField , HiddenField, PasswordField,IntegerField,SelectField,EmailField
from wtforms.validators import DataRequired,NumberRange

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))
from connexion_bd import ConnexionBD

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/BD'))
from club_bd import ClubBD
from escrimeur_bd import EscrimeurBD
from organisateur_bd import OrganisateurBD
from categorie_bd import CategorieBD
from .models import load_user


class ConnexionFormE(FlaskForm):
    identifiant = IntegerField("Votre numéro de licence",validators=[DataRequired(),NumberRange(min=0, max=999999999)])
    mdp = PasswordField("Mot de passe", validators=[DataRequired()])
    next = HiddenField()

class ConnexionForm(FlaskForm):
    identifiant = StringField("Votre nom",validators=[DataRequired()])
    mdp = PasswordField("Mot de passe", validators=[DataRequired()])
    next = HiddenField()

class InscriptionForm(FlaskForm):
    numLicence = IntegerField("Votre numéro de licence",validators=[DataRequired(),NumberRange(min=0, max=999999999)])
    nom = StringField("Votre nom",validators=[DataRequired()])
    prenom = StringField("Votre prénom",validators=[DataRequired()])
    age = IntegerField("Votre âge",validators=[DataRequired(),NumberRange(min=0, max=999999999)])
    sexe = SelectField("Votre sexe", choices=["H","F"] ,validators=[DataRequired()])
    categorie = SelectField("Votre catégorie",choices=[(categorie.get_id(),categorie.get_nom()) for categorie in CategorieBD(ConnexionBD().get_connexion()).get_all_categorie()])
    mdp = PasswordField("Mot de passe", validators=[DataRequired()])
    conf_mdp = PasswordField("Confirmation du mot de passe", validators=[DataRequired()])
    telephone = IntegerField("Votre numéro de téléphone",validators=[DataRequired(),NumberRange(min=0, max=999999999)])
    club = SelectField("Votre club",choices=[(club.get_id(),club.get_nom()) for club in ClubBD(ConnexionBD().get_connexion()).get_all_club()])
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

connexion_vers_bd = ConnexionBD()
@app.route("/inscription", methods=["GET", "POST"]  )
def inscription():
    form = InscriptionForm()
    if form.validate_on_submit():
        print("carre")
    
    return render_template(
        "page_inscription.html",form=form
    )

@app.route("/connexion/<nom>", methods=["GET", "POST"])
def connexion(nom):
    connexion_vers_bd.ouvrir_connexion()
    user=""
    if nom != "ORGANISATEUR" and nom != "ESCRIMEUR" and nom != "CLUB":
        flask.abort(404)
    form = ConnexionForm()
    if nom == "ESCRIMEUR":
        form = ConnexionFormE()
    if form.validate_on_submit():
        identifiant = form.identifiant.data
        mdp = form.mdp.data
        if nom == "ESCRIMEUR":
            escrimeur = EscrimeurBD(connexion_vers_bd.get_connexion())
            user = escrimeur.login_escrimeur(int(identifiant), mdp)
            if user is not None and user.get_mdp() == mdp:
                return render_template("home.html", nom=user)

        elif nom == "ORGANISATEUR":
            organisateur = OrganisateurBD(connexion_vers_bd.get_connexion())
            user = organisateur.login_organisateur(identifiant, mdp)
            if user is not None and user.get_mdp() == mdp:
                return render_template("home.html", nom=user)

        elif nom == "CLUB":
            club = ClubBD(connexion_vers_bd.get_connexion())
            user = club.login_club(identifiant, mdp)
            if user is not None and user.get_mdp() == mdp:
                return render_template("home.html", nom=user)
        print("USER ",user)
        if user is None:
            return render_template("page_connexion.html",nom=nom,form=form,message="Identifiant ou mot de passe invalide")
        return render_template("home.html", nom=user)

    return render_template("page_connexion.html", nom=nom, form=form)
