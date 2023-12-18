from datetime import date, timedelta
import flask
import sys
import os
from .app import app
from flask import render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, PasswordField, IntegerField, SelectField, TelField, DateField
from wtforms.validators import DataRequired, NumberRange, Length, EqualTo, StopValidation

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))
from escrimeur import Escrimeur
from modele_appli import ModeleAppli
from competition import Competition
from constantes import USER


USER = USER

modele_appli = ModeleAppli()
print("On récupère les compétitions")
COMPETITIONS = modele_appli.get_competition_bd().get_all_competition()
print("fini")
modele_appli.close_connexion()


def statut(competition : Competition):
    if competition.get_date_fin_inscription() == None:
        return "Pas disponible"
    if competition.get_date_fin_inscription() > date.today():
        return "En cours d'inscription"
    elif competition.get_date() > date.today():
        return "En cours"
    else:
        return "Terminée"


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
                    NumberRange(min=0)])
    
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
                    NumberRange(min=0)])
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

    club = SelectField(
        "Votre club",
        choices=[(club.get_id(), club.get_nom())
                 for club in modele_appli.get_club_bd().get_all_club()])
    next = HiddenField()
    modele_appli.close_connexion()

@app.route("/", methods=["GET"])
def home():
    print("USER ", USER)
    statuts = []
    for competition in COMPETITIONS:
        statuts.append(statut(competition))

    return render_template(
        "home.html",competitions=COMPETITIONS, statuts=statuts, user=USER
    )


@app.route("/choix")
def choose_sign():
    return render_template("connexion_inscription.html", user=USER)


@app.route("/choisir_statut_connexion", methods=["GET", "POST"])
def choisir_statut_connexion():
    return render_template(

        "choisir_statut_connexion.html", user=USER
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
        club = form.club.data

        escrimeur_a_inserer = Escrimeur(1, nom, prenom, sexe, date_naissance,
                                        prenom.lower(), mdp, num_licence, None,
                                        club, categorie, False)
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
    global USER
    modele_appli = ModeleAppli()
    print("connexion ",USER)

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
            USER = modele_appli.get_escrimeur_bd().login_escrimeur(
                identifiant, mdp)
            modele_appli.close_connexion()
            if USER is not None and USER.get_mdp() == mdp:
                print("redirectzefdiz")
                return redirect(url_for('home'))
        elif nom == "ORGANISATEUR":
            USER = modele_appli.get_organisateur_bd(
            ).login_organisateur(identifiant, mdp)
            modele_appli.close_connexion()
            if USER is not None and USER.get_mdp() == mdp:
                return redirect(url_for('home'))

        elif nom == "CLUB":
            USER = modele_appli.get_club_bd(

            ).login_club(identifiant, mdp)
            modele_appli.close_connexion()
            if USER is not None and USER.get_mdp() == mdp:
                return redirect(url_for('home'))
        print("USER ", USER)
        if USER is None:
            return render_template(
                "page_connexion.html",
                nom=nom,
                form=form,
                message="Identifiant ou mot de passe invalide")

        return redirect(url_for('home'))

    modele_appli.close_connexion()
    return render_template("page_connexion.html", nom=nom, form=form)

@app.route("/regles")
def regles():
    return render_template("regles.html")

@app.route("/competition/<id_competition>")
def competition(id_competition):
    modele = ModeleAppli()
    print("id_competition", id_competition)
    la_competition = modele.get_competition_bd().get_competition_by_id(id_competition)
    return render_template("competition.html", compet = la_competition)


@app.route("/competition_match/<id_competition>")
def competition_match(id_competition):
    modele = ModeleAppli()
    la_competition = modele.get_competition_bd().get_competition_by_id(id_competition)
    matchs = modele.get_competition_bd().get_all_matchs(id_competition)
    return render_template("competition_match.html" , compet = la_competition, matchs = matchs,user=USER)

# verifier que le USer est conecter + arbitre
@app.route("/competition_arbitre/<id_arbitre>")
def competition_arbitre(id_arbitre):
    modele = ModeleAppli()
    les_competition = modele.get_competition_bd().get_competition_by_arbitre(id_arbitre)
    return render_template("page_competition_arbitre.html" , competitions = les_competition,user=USER)
