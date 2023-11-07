import flask
import sys
import os
from .app import app
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField , HiddenField, PasswordField,IntegerField,SelectField,TelField,DateField
from wtforms.validators import DataRequired,NumberRange

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
    age = DateField("Votre date de naissance",validators=[DataRequired()])
    sexe = SelectField("Votre sexe", choices=["H","F"] ,validators=[DataRequired()])
    categorie = SelectField("Votre catégorie",choices=[(categorie.get_id(),categorie.get_nom()) for categorie in CategorieBD(ConnexionBD().get_connexion()).get_all_categorie()])
    mdp = PasswordField("Mot de passe", validators=[DataRequired()])
    conf_mdp = PasswordField("Confirmation du mot de passe", validators=[DataRequired()])
    telephone = TelField("Votre numéro de téléphone",validators=[DataRequired()])
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
    message=""
    print("On lance la page inscription")
    if form.validate_on_submit():
        num_licence = form.numLicence.data
        nom = form.nom.data
        prenom = form.prenom.data
        date_naissance = form.age.data
        sexe = form.sexe.data
        categorie = form.categorie.data
        mdp = form.mdp.data
        conf_mdp = form.conf_mdp.data
        telephone = form.telephone.data
        club = form.club.data
        print("numLicence",num_licence,"\n","nom",nom,"\n","prenom",prenom,"\n","date de naissance",date_naissance,"\n","sexe",sexe,"\n","categorie",categorie,"\n","mdp",mdp,"\n","conf_mdp",conf_mdp,"\n","telephone",telephone,"\n","club",club,"\n")

        if mdp != conf_mdp:
            message="Les mots de passe ne correspondent pas"
            return render_template(
                "page_inscription.html",form=form,message=message
            )
        else:
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
                message = str(e.__cause__)
                message = message.split(": ")[1]
                connexion_vers_bd.fermer_connexion()
                return render_template(
                    "page_inscription.html",form=form,message=message
                )
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
        print("C'est là")
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
