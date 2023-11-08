from datetime import date,timedelta
import flask
import sys
import os
from .app import app
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField , HiddenField, PasswordField,IntegerField,SelectField,TelField,DateField
from wtforms.validators import DataRequired, NumberRange, Length, ValidationError,EqualTo

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))
from connexion_bd import ConnexionBD
from escrimeur import Escrimeur

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/BD'))
from club_bd import ClubBD
from escrimeur_bd import EscrimeurBD
from organisateur_bd import OrganisateurBD
from categorie_bd import CategorieBD


def alpha():
    def _alpha(form, field):
        for element in field.data:
            if not element.isdigit():
                raise ValidationError("Le numéro de téléphone ne doit contenir que des chiffres")
    return _alpha

def valide_mdp():

    def _valide_mdp(form, field):
        symbole= False
        chiffre = False
        majuscule = False
        for element in field.data:
            if element.isdigit():
                chiffre = True
            elif element.isupper():
                majuscule = True
            elif not element.isalnum():
                symbole = True
        if not symbole or not chiffre or not majuscule:
            raise ValidationError("Le mot de passe doit contenir au moins une majuscule, un chiffre et un symbole")
    return _valide_mdp




class ConnexionFormE(FlaskForm):
    identifiant = IntegerField("Votre numéro de licence",validators=[DataRequired(),NumberRange(min=0, max=999999999)])
    mdp = PasswordField("Mot de passe", validators=[DataRequired()])
    next = HiddenField()

class ConnexionForm(FlaskForm):
    identifiant = StringField("Votre nom",validators=[DataRequired()])
    mdp = PasswordField("Mot de passe", validators=[DataRequired()])
    next = HiddenField()

class InscriptionForm(FlaskForm):
    dixhuit = date.today() - timedelta(days=18*365)
    numLicence = IntegerField("Votre numéro de licence",validators=[DataRequired(),NumberRange(min=0, max=999999999)])
    nom = StringField("Votre nom",validators=[DataRequired()])
    prenom = StringField("Votre prénom",validators=[DataRequired()])
    date_naissance = DateField("Votre date de naissance",default=dixhuit,validators=[DataRequired()])
    sexe = SelectField("Votre sexe", choices=["H","F"] ,validators=[DataRequired()])
    categorie = SelectField("Votre catégorie",choices=[(categorie.get_id(),categorie.get_nom()) for categorie in CategorieBD(ConnexionBD().get_connexion()).get_all_categorie()])
    mdp = PasswordField("Mot de passe", validators=[DataRequired(),Length(min=8,max=50),valide_mdp(),EqualTo('conf_mdp',message="Les mots de passe ne correspondent pas")])
    conf_mdp = PasswordField("Confirmation du mot de passe", validators=[DataRequired()])
    telephone = TelField("Votre numéro de téléphone",validators=[DataRequired(),alpha(),Length(min=10,max=10)])
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
    connexion_vers_bd.ouvrir_connexion()
    form = InscriptionForm()
    message=[]
    print("On lance la page inscription")
    if form.validate_on_submit():
        num_licence = form.numLicence.data
        nom = form.nom.data
        prenom = form.prenom.data
        date_naissance = form.date_naissance.data
        sexe = form.sexe.data
        categorie = form.categorie.data
        mdp = form.mdp.data
        conf_mdp = form.conf_mdp.data
        telephone = form.telephone.data
        club = form.club.data

        escrimeur_a_inserer = Escrimeur(1,nom, prenom,sexe, date_naissance,prenom.lower(),mdp,num_licence,None,club, categorie, telephone )
        print("escrimeur_a_inserer",escrimeur_a_inserer)
        escrimeur = EscrimeurBD(connexion_vers_bd.get_connexion())
        try:
            print("On va insérer l'escrimeur")
            escrimeur.insert_escrimeur(escrimeur_a_inserer)
            connexion_vers_bd.fermer_connexion()
            return render_template(
                "page_inscription.html",form=form,message="Inscription réussie"
            )
        except Exception as e:
            exception = str(e.__cause__)
            exception = message.split(": ")[1]
            message.append(exception)
            connexion_vers_bd.fermer_connexion()
            return render_template(
                "page_inscription.html",form=form,message=message
            )

    # Si le formulaire n'est pas valide on affiche les erreurs
    if (form.errors):
        for erreur in form.errors:
            message.append(form.errors[erreur][0])

    return render_template(
        "page_inscription.html",form=form,message=message
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
