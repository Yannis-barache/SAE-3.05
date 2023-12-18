from datetime import date, timedelta
import flask
import sys
import os
from .app import app
from flask import render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, PasswordField, IntegerField, SelectField, DateField
from wtforms.validators import DataRequired, NumberRange, Length, EqualTo, StopValidation

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))
from escrimeur import Escrimeur
from modele_appli import ModeleAppli
from constantes import USER

USER = USER




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
    num_licence = IntegerField(
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
    modele_appli.close_connexion()
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
    modele_appli = ModeleAppli()
    club = SelectField(
        "Votre club",
        choices=[(club.get_id(), club.get_nom())
                 for club in modele_appli.get_club_bd().get_all_club()])
    next = HiddenField()
    modele_appli.close_connexion()

@app.route("/", methods=["GET"])
def home():
    modele_appli = ModeleAppli()
    competitions = modele_appli.get_competition_bd().get_all_competition()
    print("USER ", USER)
    modele_appli.close_connexion()
    return render_template(
        "home.html",competitions=competitions, user=USER
    )


@app.route("/choix")
def choose_sign():
    return render_template("connexion_inscription.html", user=USER)


@app.route("/choisir_statut_connexion", methods=["GET", "POST"])
def choisir_statut_connexion():
    return render_template(

        "choisir_statut_connexion.html", user=USER
    )


@app.route("/page_poule")
def page_poule():
    return render_template(
        "page_poule_compet.html"
    )


@app.route("/choisir_statut_inscription")
def choisir_statut_inscription():
    return render_template(
        "choisir_statut_inscription.html",
    )

@app.route("/espace_personnel/")
def espace_personnel():
    user = USER
    return render_template(
        "espace.html", user=user
    )

@app.route("/inscription", methods=["GET", "POST"])
def inscription():
    modele_appli = ModeleAppli()
    form = InscriptionForm()
    message = []
    print("On lance la page inscription")
    if form.validate_on_submit():
        num_licence = int(form.num_licence.data)
        nom = form.nom.data
        prenom = form.prenom.data
        date_naissance = form.date_naissance.data
        sexe = form.sexe.data
        categorie = modele_appli.get_categorie_bd().get_categorie_by_id(form.categorie.data)
        mdp = form.mdp.data
        club = modele_appli.get_club_bd().get_club_by_id(form.club.data)
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
    return render_template("regles.html", user=USER)

@app.route("/competition/<id_competition>")
def competition(id_competition):
    if USER is not None and USER.is_arbitre():
        modele = ModeleAppli()
        print("id_competition", id_competition)
        la_competition = modele.get_competition_bd().get_competition_by_id(id_competition)
        nb_poule = modele.get_poule_bd().nb_poule_compet(id_competition)
        modele.close_connexion()
        return render_template("competition.html", compet=la_competition,
                            poule=nb_poule, user=USER)
    else:
        flask.abort(404)

@app.route("/competition_match/<id_competition>")
def competition_match(id_competition):
    modele = ModeleAppli()
    la_competition = modele.get_competition_bd().get_competition_by_id(id_competition)
    matchs = modele.get_competition_bd().get_all_matchs(id_competition)
    modele.close_connexion()
    return render_template("competition_match.html" , compet = la_competition, matchs = matchs,user=USER)

# verifier que le USer est conecter + arbitre

@app.route("/competition_arbitre/<id_arbitre>")
def competition_arbitre(id_arbitre):
    print("icicicicic",USER)
    if USER is not None and USER.get_arbitrage():
        modele = ModeleAppli()
        les_competition = modele.get_competition_bd().get_competition_by_arbitre(id_arbitre)
        modele.close_connexion()
        return render_template("page_competition_arbitre.html" , competitions = les_competition,user=USER)
    else:
        flask.abort(404)

@app.route("/poule/<id_competition>/<nb>", methods=["GET", "POST"])
def poule(id_competition, nb):
    modele = ModeleAppli()
    nombre_poule = modele.get_poule_bd().nb_poule_compet(int(id_competition))
    print("nombre_poule", nombre_poule)
    nb = int(nb) % nombre_poule
    la_competition = modele.get_competition_bd().get_competition_by_id_s(id_competition)
    la_poule = modele.get_poule_bd().get_poules_by_compet_nb(int(id_competition), int(nb))
    modele.close_connexion()
    return render_template(
        "page_poule_compet.html", la_poule=la_poule,
        compet=la_competition, nb=nb, user=USER, nb_poule = nombre_poule
    )

@app.route('/telecharger_pdf_poule/<int:id_poule>')
def telecharger_pdf_poule(id_poule):
    modele = ModeleAppli()
    la_poule = modele.get_poule_bd().get_poule_by_id(id_poule)
    la_poule.generer_pdf()
    modele.close_connexion()
    return redirect(request.referrer)

@app.route("/deconnexion")
def deconnexion():
    global USER
    USER = None
    return redirect(url_for('choose_sign'))
