from datetime import date, timedelta
import flask
import sys
import os
from .app import app
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, PasswordField, IntegerField, SelectField, TelField, DateField
from wtforms.validators import DataRequired, NumberRange, Length, EqualTo, StopValidation

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))
from modele_appli import ModeleAppli
from escrimeur import Escrimeur


class Alpha:

    def __init__(self, message=None):
        self.__message = message

    def __call__(self, form, field):
        for element in field.data:
            if not element.isdigit():
                raise StopValidation(
                    "Le numéro de téléphone ne doit contenir que des chiffres")


class ValideMdp:
    """
    Classe qui permet de vérifier que le mot de passe est valide

    """

    def __init__(self, message=None):

        self.__message = message

    def __call__(self, form, field):
        """
        Fonction qui vérifie que le mot de passe est valide

        Args :
            form (FlaskForm) : formulaire
            field (PasswordField) : champ du mot de passe

        Raises :
            ValidationError : si le mot de passe n'est pas valide
        """
        mdp = field.data
        chiffre = False
        majuscule = False
        symbole = False
        if len(mdp) < 8:
            raise StopValidation(
                "Le mot de passe doit contenir au moins 8 caractères")
        for element in mdp:
            if element.isdigit():
                chiffre = True
            if element.isupper():
                majuscule = True
            if element.isalnum():
                symbole = True
        if not chiffre or not majuscule or not symbole:
            raise StopValidation(
                "Le mot de passe doit contenir au moins un chiffre, une majuscule et un symbole"
            )


class ConnexionFormE(FlaskForm):
    identifiant = IntegerField(
        "Votre N° de licence",
        validators=[DataRequired(),
                    NumberRange(min=0, max=999999999)])
    mdp = PasswordField("Mot de passe", validators=[DataRequired()])
    next = HiddenField()


class ConnexionForm(FlaskForm):
    identifiant = StringField("Votre nom", validators=[DataRequired()])
    mdp = PasswordField("Mot de passe", validators=[DataRequired()])
    next = HiddenField()


class InscriptionForm(FlaskForm):
    modele_appli = ModeleAppli()
    dixhuit = date.today() - timedelta(days=18 * 365)
    numLicence = IntegerField(
        "Votre numéro de licence",
        validators=[DataRequired(),
                    NumberRange(min=0, max=999999999)])
    nom = StringField("Votre nom", validators=[DataRequired()])
    prenom = StringField("Votre prénom", validators=[DataRequired()])
    date_naissance = DateField("Votre date de naissance",
                               default=dixhuit,
                               validators=[DataRequired()])
    sexe = SelectField("Votre sexe",
                       choices=["H", "F"],
                       validators=[DataRequired()])
    categorie = SelectField(
        "Votre catégorie",
        choices=[(categorie.get_id(), categorie.get_nom()) for categorie in
                 modele_appli.get_categorie_bd().get_all_categorie()])
    mdp = PasswordField(
        "Mot de passe",
        validators=[
            DataRequired(),
            Length(min=8, max=50),
            EqualTo('conf_mdp',
                    message="Les mots de passe ne correspondent pas")
        ])
    conf_mdp = PasswordField("Confirmation du mot de passe",
                             validators=[DataRequired()])
    telephone = TelField(
        "Votre numéro de téléphone",
        validators=[DataRequired(),
                    Alpha(), Length(min=10, max=10)])
    club = SelectField(
        "Votre club",
        choices=[(club.get_id(), club.get_nom())
                 for club in modele_appli.get_club_bd().get_all_club()])
    next = HiddenField()
    modele_appli.close_connexion()


@app.route("/home")
def home():
    return render_template(
        "home.html"
    )


@app.route("/")
def choose_sign():
    return render_template("connexion_inscription.html")


@app.route("/choisir_statut_connexion", methods=["GET", "POST"])
def choisir_statut_connexion():
    return render_template(

        "choisir_statut_connexion.html"
    )


@app.route("/inscription", methods=["GET", "POST"])
def inscription():
    modele_appli = ModeleAppli()
    form = InscriptionForm()
    message = []
    print("On lance la page inscription")
    if form.validate_on_submit():
        num_licence = form.numLicence.data
        nom = form.nom.data
        prenom = form.prenom.data
        date_naissance = form.date_naissance.data
        sexe = form.sexe.data
        categorie = form.categorie.data
        mdp = form.mdp.data
        telephone = form.telephone.data
        club = form.club.data

        escrimeur_a_inserer = Escrimeur(1, nom, prenom, sexe, date_naissance,
                                        prenom.lower(), mdp, num_licence, None,
                                        club, categorie, telephone)
        print("escrimeur_a_inserer", escrimeur_a_inserer)
        try:
            print("On va insérer l'escrimeur")
            modele_appli.get_escrimeur_bd().insert_escrimeur(
                escrimeur_a_inserer)
            modele_appli.close_connexion()
            return render_template("page_inscription.html",
                                   form=form,
                                   message="Inscription réussie")
        except Exception as e:
            exception = str(e.__cause__)
            print("exception", exception)
            exception = exception.split(": ")[1]
            print("exception", exception)
            message.append(exception)
            modele_appli.close_connexion()
            return render_template("page_inscription.html",
                                   form=form,
                                   message=message)

    # Si le formulaire n'est pas valide, on affiche les erreurs
    if form.errors:
        for erreur in form.errors:
            message.append(form.errors[erreur][0])

    modele_appli.close_connexion()

    return render_template("page_inscription.html", form=form, message=message)


@app.route("/connexion/<nom>", methods=["GET", "POST"])
def connexion(nom):
    modele_appli = ModeleAppli()
    user = ""
    if nom != "ORGANISATEUR" and nom != "ESCRIMEUR" and nom != "CLUB":
        modele_appli.close_connexion()
        flask.abort(404)
    form = ConnexionForm()
    if nom == "ESCRIMEUR":
        form = ConnexionFormE()
    if form.validate_on_submit():
        identifiant = form.identifiant.data
        mdp = form.mdp.data
        if nom == "ESCRIMEUR":
            user = modele_appli.get_escrimeur_bd().login_escrimeur(
                identifiant, mdp)
            modele_appli.close_connexion()
            if user is not None and user.get_mdp() == mdp:
                return render_template("home.html", nom=user)

        elif nom == "ORGANISATEUR":
            organisateur = modele_appli.get_organisateur_bd(
            ).login_organisateur(identifiant, mdp)
            user = organisateur 
            modele_appli.close_connexion()
            if user is not None and user.get_mdp() == mdp:
                return render_template("home.html", nom=user)

        elif nom == "CLUB":
            club = modele_appli.get_club_bd().login_club(identifiant, mdp)
            user = club.login_club(identifiant, mdp)
            modele_appli.close_connexion()
            if user is not None and user.get_mdp() == mdp:
                return render_template("home.html", nom=user)
        print("USER ", user)
        if user is None:
            return render_template(
                "page_connexion.html",
                nom=nom,
                form=form,
                message="Identifiant ou mot de passe invalide")
        return render_template("home.html", nom=user)

    modele_appli.close_connexion()
    return render_template("page_connexion.html", nom=nom, form=form)

