"""
Fichier qui contient les formulaires pour les pages web
"""

from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, PasswordField, IntegerField, SelectField, DateField, FloatField
from wtforms.validators import DataRequired, NumberRange, Length, EqualTo, StopValidation
import os
import sys
from datetime import date, timedelta

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))
from escrimeur import Escrimeur
from modele_appli import ModeleAppli

def competition_form():
    class CompetitionForm(FlaskForm):
        modele = ModeleAppli()
        id = HiddenField('id')
        name = StringField('Nom', validators=[DataRequired()])
        date = DateField('Date', validators=[DataRequired()])
        date_fin_inscripiton = DateField('Date fin inscription', validators=[DataRequired()])
        categorie = SelectField('Catégorie', choices=[(categorie.get_id(), categorie.get_nom()) for categorie in modele.get_categorie_bd().get_all_categorie()], validators=[DataRequired()])
        saison = SelectField('Saison', choices=['été', 'hiver', 'printemps', 'automne'], validators=[DataRequired()])
        arme = SelectField('Arme', choices=[(arme.get_id(), arme.get_nom()) for arme in modele.get_arme_bd().get_all_arme()], validators=[DataRequired()])
        lieu = SelectField('Lieu', choices=[(lieu.get_id(), lieu.get_adresse()) for lieu in modele.get_lieu_bd().get_all_lieu()], validators=[DataRequired()])
        coefficient = FloatField('Coefficient', validators=[DataRequired()])
        title = HiddenField('title')
        modele.close_connexion()
    return CompetitionForm()
def competition_form2():
    class CompetitionForm2(FlaskForm):
        modele = ModeleAppli()
        name = StringField('Nom', validators=[DataRequired()])
        date = DateField('Date', validators=[DataRequired()])
        date_fin_inscripiton = DateField('Date fin inscription', validators=[DataRequired()])
        categorie = SelectField('Catégorie', choices=[(categorie.get_id(), categorie.get_nom()) for categorie in modele.get_categorie_bd().get_all_categorie()], validators=[DataRequired()])
        saison = SelectField('Saison', choices=['été', 'hiver', 'printemps', 'automne'], validators=[DataRequired()])
        arme = SelectField('Arme', choices=[(arme.get_id(), arme.get_nom()) for arme in modele.get_arme_bd().get_all_arme()], validators=[DataRequired()])
        lieu = SelectField('Lieu', choices=[(lieu.get_id(), lieu.get_adresse()) for lieu in modele.get_lieu_bd().get_all_lieu()], validators=[DataRequired()])
        coefficient = FloatField('Coefficient', validators=[DataRequired()])
        title = HiddenField('title')
        modele.close_connexion()
    return CompetitionForm2()


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

def connexion_formE():
    class ConnexionFormE(FlaskForm):
        identifiant = IntegerField(
            "Votre N° de licence",
            validators=[DataRequired(),
                        NumberRange(min=0, max=999999999)])
        mdp = PasswordField("Mot de passe", validators=[DataRequired()])
        next = HiddenField()
    return ConnexionFormE()


def connexion_form():
    class ConnexionForm(FlaskForm):
        identifiant = StringField("Votre nom", validators=[DataRequired()])
        mdp = PasswordField("Mot de passe", validators=[DataRequired()])
        next = HiddenField()
    return ConnexionForm()

def inscription_form():
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
    return InscriptionForm()


def club_form():
    class ClubForm(FlaskForm):
        id = HiddenField('id')
        name = StringField('Nom', validators=[DataRequired()])
        adresse = StringField('Adresse', validators=[DataRequired()])
        title = HiddenField('title')
    return ClubForm()

def club_form2():
    class ClubForm2(FlaskForm):
        name = StringField('Nom', validators=[DataRequired()])
        adresse = StringField('Adresse', validators=[DataRequired()])
        mdp = PasswordField('Mot de passe', validators=[DataRequired()])
        title = HiddenField('title')
    return ClubForm2()

def escrimeur_form():
    class EscrimeurForm(FlaskForm):
        modele = ModeleAppli()
        id = HiddenField('id')
        name = StringField('Nom', validators=[DataRequired()])
        prenom = StringField('Prenom', validators=[DataRequired()])
        date_naissance = DateField('Date de naissance', validators=[DataRequired()])
        sexe = SelectField('Sexe', choices=["H", "F"], validators=[DataRequired()])
        categorie = SelectField('Catégorie', choices=[(categorie.get_id(), categorie.get_nom()) for categorie in modele.get_categorie_bd().get_all_categorie()], validators=[DataRequired()])
        club = SelectField('Club', choices=[(club.get_id(), club.get_nom()) for club in modele.get_club_bd().get_all_club()], validators=[DataRequired()])
        licence = StringField('License', validators=[DataRequired()])
        nom_utilisateur = StringField('Nom d\'utilisateur', validators=[DataRequired()])
        arbitrage = SelectField('Arbitrage', choices=["Oui", "Non"], validators=[DataRequired()])
        title = HiddenField('title')
        modele.close_connexion()
    return EscrimeurForm()

def escrimeur_form2():
    class EscrimeurForm2(FlaskForm):
        modele = ModeleAppli()
        name = StringField('Nom', validators=[DataRequired()])
        prenom = StringField('Prenom', validators=[DataRequired()])
        date_naissance = DateField('Date de naissance', validators=[DataRequired()])
        sexe = SelectField('Sexe', choices=["H", "F"], validators=[DataRequired()])
        categorie = SelectField('Catégorie', choices=[(categorie.get_id(), categorie.get_nom()) for categorie in modele.get_categorie_bd().get_all_categorie()], validators=[DataRequired()])
        club = SelectField('Club', choices=[(club.get_id(), club.get_nom()) for club in modele.get_club_bd().get_all_club()], validators=[DataRequired()])
        licence = StringField('License', validators=[DataRequired()])
        nom_utilisateur = StringField('Nom d\'utilisateur', validators=[DataRequired()])
        arbitrage = SelectField('Arbitrage', choices=["Oui", "Non"], validators=[DataRequired()])
        title = HiddenField('title')
        modele.close_connexion()
    return EscrimeurForm2()

def lieu_form():
    class LieuForm(FlaskForm):
        id = HiddenField('id')
        adresse = StringField('Adresse', validators=[DataRequired()])
        description = StringField('Description', validators=[DataRequired()])
        title = HiddenField('title')
    return LieuForm()

def lieu_form2():
    class LieuForm2(FlaskForm):
        description = StringField('Description', validators=[DataRequired()])
        adresse = StringField('Adresse', validators=[DataRequired()])
        title = HiddenField('title')
    return LieuForm2()

def heure_debut_form():
    class HeureDebutForm(FlaskForm):
        heure = IntegerField('Heure de début', validators=[DataRequired()])
        type = HiddenField('type')
    return HeureDebutForm()

if __name__ == '__main__':
    pass
