from datetime import date, timedelta
import flask
import sys
import os
from .app import app
from flask import render_template, redirect, url_for, request


ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))
from escrimeur import Escrimeur
from modele_appli import ModeleAppli
from club import Club
from lieu import Lieu
from competition import Competition
from constantes import USER
from inscrire import Inscrire
from touche import Touche
from organisateur import Organisateur
from phase_final import PhaseFinal

USER = USER
modele_appli = ModeleAppli()


@app.route("/", methods=["GET"])
def home():
    modele_appli = ModeleAppli()
    competitions = modele_appli.get_competition_bd().get_all_competition(
    ) or []
    inscrit = []
    if USER is not None and isinstance(USER, Escrimeur):
        inscription = modele_appli.get_inscrire_bd().get_all_inscrit_escrimeur(
            USER)
        for i in inscription:
            inscrit.append(i.get_id_competition())
    print("USER ", USER)
    modele_appli.close_connexion()
    return render_template("home.html",
                           competitions=competitions,
                           user=USER,
                           competitions_inscrit=inscrit)



@app.route("/choix")
def choose_sign():
    return render_template("connexion_inscription.html", user=USER)


@app.route("/choisir_statut_connexion", methods=["GET", "POST"])
def choisir_statut_connexion():
    return render_template("choisir_statut_connexion.html", user=USER)


@app.route("/choisir_statut_inscription")
def choisir_statut_inscription():
    return render_template("choisir_statut_inscription.html", )


@app.route("/espace_personnel/")
def espace_personnel():
    if USER is None:
        return redirect(url_for('choose_sign'))
    return render_template("espace.html", user=USER)


@app.route("/inscription", methods=["GET", "POST"])
def inscription():
    from .form import inscription_form
    modele_appli = ModeleAppli()
    form = inscription_form()
    message = []
    print("On lance la page inscription")
    if form.validate_on_submit():
        num_licence = int(form.num_licence.data)
        nom = form.nom.data
        prenom = form.prenom.data
        date_naissance = form.date_naissance.data
        sexe = form.sexe.data
        categorie = modele_appli.get_categorie_bd().get_categorie_by_id(
            form.categorie.data)
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
    from .form import connexion_form, connexion_formE
    global USER
    modele_appli = ModeleAppli()
    print("connexion ", USER)
    if nom != "ORGANISATEUR" and nom != "ESCRIMEUR" and nom != "CLUB":
        modele_appli.close_connexion()
        flask.abort(404)
    form = connexion_form()
    if nom == "ESCRIMEUR":
        form = connexion_formE()
    if form.validate_on_submit():
        identifiant = form.identifiant.data
        mdp = form.mdp.data
        if nom == "ESCRIMEUR":
            USER = modele_appli.get_escrimeur_bd().login_escrimeur(
                identifiant, mdp)
            modele_appli.close_connexion()
            if USER is not None:
                return redirect(url_for('home'))
        elif nom == "ORGANISATEUR":
            USER = modele_appli.get_organisateur_bd().login_organisateur(
                identifiant, mdp)
            modele_appli.close_connexion()
            if USER is not None:
                print("redirect")
                return redirect(url_for('home_admin'))

        elif nom == "CLUB":
            USER = modele_appli.get_club_bd().login_club(identifiant, mdp)
            modele_appli.close_connexion()
            if USER is not None:
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
    modele = ModeleAppli()
    la_competition = modele.get_competition_bd().get_competition_by_id(
        id_competition)
    nb_poule = modele.get_poule_bd().nb_poule_compet(id_competition)
    phase_finale = modele.get_phase_finale_bd().exist_phase_finale(id_competition)
    modele.close_connexion()
    return render_template("competition.html", compet=la_competition,
                           poule=nb_poule, user=USER, phase_finale=phase_finale)


@app.route("/arbitre/competition/<id_competition>")
def competition_arbitre(id_competition):
    modele = ModeleAppli()
    la_competition = modele.get_competition_bd().get_competition_by_id(
        id_competition)
    nb_poule = modele.get_poule_bd().nb_poule_compet(id_competition)
    phase_finale = modele.get_phase_finale_bd().exist_phase_finale(id_competition)
    modele.close_connexion()
    return render_template("arbitre/arbitre-competition.html", compet=la_competition,
                           poule=nb_poule, user=USER, phase_finale=phase_finale)


@app.route("/page_de_match")
def page_de_match(id_match):
    form = EnvoiePointForm()
    finir_match_form = FinirMatchForm()
    modele = ModeleAppli()
    le_match = modele.get_match_bd().get_match_by_id(id_match)
    id_competition = modele.get_match_bd().get_id_competition_du_match(
        le_match)
    la_competition = modele.get_competition_bd().get_competition_by_id(
        id_competition)
    le_match = modele.get_match_bd().get_match_by_id(id_match)
    les_touches = modele.get_touche_bd().get_by_match(le_match)
    le_match.set_touche(les_touches)
    modele.close_connexion()
    return render_template("page_de_match.html",
                           match=le_match,
                           user=USER,
                           compet=la_competition,
                           form=form,
                           touches = les_touches,
                           finir_match_form=finir_match_form)

@app.route("/arbitre/arbitre_page_de_match")
def arbitre_page_de_match(id_match):
    form = EnvoiePointForm()
    finir_match_form = FinirMatchForm()
    modele = ModeleAppli()
    le_match = modele.get_match_bd().get_match_by_id(id_match)
    id_competition = modele.get_match_bd().get_id_competition_du_match(
        le_match)
    la_competition = modele.get_competition_bd().get_competition_by_id(
        id_competition)
    le_match = modele.get_match_bd().get_match_by_id(id_match)
    les_touches = modele.get_touche_bd().get_by_match(le_match)
    le_match.set_touche(les_touches)
    modele.close_connexion()
    return render_template("arbitre/arbitre-page_de_match.html",
                           match=le_match,
                           user=USER,
                           compet=la_competition,
                           form=form,
                           touches = les_touches,
                           finir_match_form=finir_match_form)


@app.route("/poule/<id_competition>/<nb>", methods=["GET", "POST"])
def poule(id_competition, nb):
    modele = ModeleAppli()
    nombre_poule = modele.get_poule_bd().nb_poule_compet(int(id_competition))
    if nombre_poule == 0:
        nombre_poule = -1
    else:
        nb = int(nb) % nombre_poule
    la_competition = modele.get_competition_bd().get_competition_by_id_s(
        id_competition)
    la_poule = modele.get_poule_bd().get_poules_by_compet_nb(
        int(id_competition), int(nb))
    modele.close_connexion()
    return render_template("page_poule_compet.html",
                           la_poule=la_poule,
                           compet=la_competition,
                           nb=nb,
                           user=USER,
                           nb_poule=nombre_poule)


@app.route("/abitre/poule/<id_competition>/<nb>", methods=["GET", "POST"])
def poule_arbitre(id_competition, nb):
    modele = ModeleAppli()
    nombre_poule = modele.get_poule_bd().nb_poule_compet(int(id_competition))
    if nombre_poule == 0:
        nombre_poule = -1
    else:
        nb = int(nb) % nombre_poule
    la_competition = modele.get_competition_bd().get_competition_by_id_s(
        id_competition)
    la_poule = modele.get_poule_bd().get_poules_by_compet_nb(
        int(id_competition), int(nb))
    modele.close_connexion()
    return render_template("arbitre/poule-arbitre.html",
                           la_poule=la_poule,
                           compet=la_competition,
                           nb=nb,
                           user=USER,
                           nb_poule=nombre_poule)


@app.route('/telecharger_pdf_poule/<int:id_poule>')
def telecharger_pdf_poule(id_poule):
    modele = ModeleAppli()
    la_poule = modele.get_poule_bd().get_poule_by_id(id_poule)
    la_poule.generer_pdf()
    modele.close_connexion()
    return redirect(request.referrer)

@app.route('/telecharger_pdf_phase_finale/<int:id_compet>/<int:id_phase>', methods=["GET", "POST"])
def telecharger_pdf_phase(id_compet, id_phase):
    modele = ModeleAppli()
    la_phase_finale = modele.get_phase_finale_bd().get_phase_finale_bd_by_id(id_phase)
    la_phase_finale.generer_pdf()
    modele.close_connexion()
    return url_for('phase_finale', id_competition=id_compet)

@app.route("/inscription_competition/<id_competition>")
def inscription_competition(id_competition):
    if USER is None:
        return redirect(url_for('choose_sign'))
    modele = ModeleAppli()
    try:
        modele.get_inscrire_bd().insert_inscrire(
            Inscrire(id_competition, USER.get_id()))
    except Exception as e:
        error = str(e.__cause__)
    modele.close_connexion()
    return redirect(request.referrer)


@app.route("/desinscription_competition/<id_competition>")
def desinscription_competition(id_competition):
    if USER is None:
        return redirect(url_for('choose_sign'))
    modele = ModeleAppli()
    modele.get_inscrire_bd().delete_inscrire_competition(
        Inscrire(id_competition, USER.get_id()))
    modele.close_connexion()
    return redirect(request.referrer)


@app.route("/supp_point/<id_match>", methods=["GET", "POST"])
def supp_point(id_match):
    if USER is None:
        return redirect(url_for('choose_sign'))

    modele = ModeleAppli()
    le_match = modele.get_match_bd().get_match_by_id(id_match)

    finir_match_form = FinirMatchForm()

    if finir_match_form.validate_on_submit():
        # Logique pour terminer le match, par exemple, marquer le match comme terminé
        modele.get_match_bd().set_fini_match(le_match)
        # Mettez à jour d'autres propriétés du match selon vos besoins
        modele.close_connexion()
        return redirect(request.referrer)


@app.route("/envoie_point/<id_match>/<id_escrimeur>", methods=["GET", "POST"])
def envoie_point(id_match, id_escrimeur):
    if USER is None:
        return redirect(url_for('choose_sign'))

    modele = ModeleAppli()
    escrimeur = modele.get_escrimeur_bd().get_escrimeur_by_id(id_escrimeur)
    le_match = modele.get_match_bd().get_match_by_id(id_match)
    id_competition = modele.get_match_bd().get_id_competition_du_match(
        le_match)
    la_competition = modele.get_competition_bd().get_competition_by_id(
        id_competition)
    numero = modele.get_touche_bd().get_max_num_touche(id_match)

    envoie_point_form = EnvoiePointForm(request.form)
    finir_match_form = FinirMatchForm()

    if envoie_point_form.validate_on_submit():
        if envoie_point_form.submit.data:
            modele.get_touche_bd().insert_touche(
                Touche(le_match, escrimeur, numero))

            les_touches = modele.get_touche_bd().get_by_match(le_match)
            le_match.set_touche(les_touches)

            if numero >= 27:
                return render_template("page_de_match.html",
                                       match=le_match,
                                       user=USER,
                                       compet=la_competition,
                                       form=envoie_point_form,
                                       touches = les_touches,
                                       finir_match_form=finir_match_form)

        elif envoie_point_form.supprimer_point.data:
            # Logique pour supprimer un point, par exemple, supprimer la dernière touche
            touche = modele.get_touche_bd().get_touche_by_id(id_match, numero)
            modele.get_touche_bd().delete_touche(touche, numero)
            # Mettez à jour d'autres propriétés du match selon vos besoins

            les_touches = modele.get_touche_bd().get_by_match(le_match)
            le_match.set_touche(les_touches)

            return render_template("page_de_match.html",
                                   match=le_match,
                                   user=USER,
                                   compet=la_competition,
                                   form=envoie_point_form,
                                    touches = les_touches,
                                   finir_match_form=finir_match_form)

    
    les_touches = modele.get_touche_bd().get_by_match(le_match)
    modele.close_connexion()
    return render_template("page_de_match.html",
                           match=le_match,
                           user=USER,
                           compet=la_competition,
                           form=envoie_point_form,
                           touches = les_touches,
                           finir_match_form=finir_match_form)


@app.route("/fin_du_match/<id_match>", methods=["GET", "POST"])
def fin_du_match(id_match):
    if USER is None:
        return redirect(url_for('choose_sign'))
    modele = ModeleAppli()
    le_match = modele.get_match_bd().get_match_by_id(id_match)
    id_competition = modele.get_match_bd().get_id_competition_du_match(
        le_match)
    la_competition = modele.get_competition_bd().get_competition_by_id(
        id_competition)
    les_touches = modele.get_touche_bd().get_by_match(le_match)
    

    envoie_point_form = EnvoiePointForm()
    finir_match_form = FinirMatchForm()

    if finir_match_form.validate_on_submit():
        # Logique pour terminer le match, par exemple, marquer le match comme terminé
        modele.get_match_bd().set_fini_match(le_match)
        # Mettez à jour d'autres propriétés du match selon vos besoins
        modele.close_connexion()

        return render_template("page_de_match.html",
                               match=le_match,
                               user=USER,
                               compet=la_competition,
                               form=envoie_point_form,
                               touches = les_touches,
                               finir_match_form=finir_match_form)


@app.route("/deconnexion")
def deconnexion():
    global USER
    USER = None
    return redirect(url_for('choose_sign'))


@app.route("/admin")
def home_admin():
    if USER is None:
        return redirect(url_for('choose_sign'))
    if not isinstance(USER, Organisateur):
        return redirect(url_for('home'))
    return render_template("Admin/home_admin.html", user=USER)


# Club


@app.route("/admin/clubs")
def admin_club():
    if USER is None:
        return redirect(url_for('choose_sign'))
    if not isinstance(USER, Organisateur):
        return redirect(url_for('home'))
    modele = ModeleAppli()
    les_clubs = modele.get_club_bd().get_all_club_2()
    modele.close_connexion()
    return render_template("Admin/Club/clubs.html", user=USER, clubs=les_clubs)


@app.route("/admin/supprimer_clubs/<int:id_club>", methods=["GET", "POST"])
def supprimer_club(id_club):
    if USER is None:
        return redirect(url_for('choose_sign'))
    if not isinstance(USER, Organisateur):
        return redirect(url_for('home'))
    modele = ModeleAppli()
    modele.get_club_bd().delete_club(id_club)
    modele.close_connexion()
    return redirect(url_for('admin_club'))


@app.route("/admin/modifier_clubs/<int:id_club>", methods=["GET", "POST"])
def modifier_club(id_club):
    from .form import club_form
    if USER is None:
        return redirect(url_for('choose_sign'))
    if not isinstance(USER, Organisateur):
        return redirect(url_for('home'))
    modele = ModeleAppli()
    club = modele.get_club_bd().get_club_by_id(id_club)
    form = club_form()
    form.name.data = club.get_nom()
    form.adresse.data = club.get_adresse()
    modele.close_connexion()
    return render_template("Admin/Club/modifier_club.html",
                           user=USER,
                           title="Modification club",
                           club=club,
                           form=form)


@app.route("/admin/modifier_clubs/<int:id_club>/<int:type>",
           methods=["GET", "POST"])
def update_club(id_club, type):
    from .form import club_form, club_form2
    if USER is None:
        return redirect(url_for('choose_sign'))
    if not isinstance(USER, Organisateur):
        return redirect(url_for('home'))
    modele = ModeleAppli()
    if type == 1:
        form = club_form()
        club = modele.get_club_bd().get_club_by_id(id_club)
        nom = form.name.data
        adresse = form.adresse.data
        club.set_nom(nom)
        club.set_adresse(adresse)
        modele.get_club_bd().update_club(club)
    else :
        form = club_form2()

        nom = form.name.data
        adresse = form.adresse.data
        mdp = form.mdp.data
        club = Club(1, nom, adresse, mdp)
        modele.get_club_bd().insert_club(club)
    modele.close_connexion()
    return redirect(url_for('admin_club'))


@app.route("/admin/ajouter_club", methods=["GET", "POST"])
def ajouter_club():
    from .form import club_form2
    if USER is None:
        return redirect(url_for('choose_sign'))
    if not isinstance(USER, Organisateur):
        return redirect(url_for('home'))
    form = club_form2()
    return render_template("Admin/Club/add_club.html",
                           user=USER,
                           title="Ajouter club",
                           form=form)


# Escrimeur


@app.route("/admin/escrimeurs")
def admin_escrimeur():
    if USER is None:
        return redirect(url_for('choose_sign'))
    if not isinstance(USER, Organisateur):
        return redirect(url_for('home'))
    modele = ModeleAppli()
    les_escrimeurs = modele.get_escrimeur_bd().get_all_escrimeur2()
    modele.close_connexion()
    return render_template("Admin/Escrimeur/escrimeurs.html",
                           user=USER,
                           escrimeurs=les_escrimeurs)


@app.route("/admin/supprimer_escrimeurs/<int:id_escrimeur>",
           methods=["GET", "POST"])
def supprimer_escrimeur(id_escrimeur):
    if USER is None:
        return redirect(url_for('choose_sign'))
    if not isinstance(USER, Organisateur):
        return redirect(url_for('home'))
    modele = ModeleAppli()
    modele.get_escrimeur_bd().delete_escrimeur(id_escrimeur)
    modele.close_connexion()
    return redirect(url_for('admin_escrimeur'))


@app.route("/admin/modifier_escrimeurs/<int:id_escrimeur>",
           methods=["GET", "POST"])
def modifier_escrimeur(id_escrimeur):
    from .form import escrimeur_form
    if USER is None:
        return redirect(url_for('choose_sign'))
    if not isinstance(USER, Organisateur):
        return redirect(url_for('home'))
    modele = ModeleAppli()
    escrimeur = modele.get_escrimeur_bd().get_escrimeur_by_id(id_escrimeur)
    form = escrimeur_form()
    form.name.data = escrimeur.get_nom()
    form.prenom.data = escrimeur.get_prenom()
    form.date_naissance.data = escrimeur.get_date_naissance()
    form.sexe.process_data(escrimeur.get_sexe())
    form.categorie.process_data(escrimeur.get_categorie().get_id())
    form.club.process_data(escrimeur.get_club().get_id())
    form.arbitrage.process_data("Oui" if escrimeur.get_arbitrage() else "Non")
    form.licence.data = escrimeur.get_licence()
    form.nom_utilisateur.data = escrimeur.get_nom_utilisateur()
    modele.close_connexion()
    return render_template("Admin/Escrimeur/modifier_escrimeur.html",
                           user=USER,
                           title="Modification escrimeur",
                           escrimeur=escrimeur,
                           form=form)



@app.route("/admin/modifier_escrimeurs/<int:id_escrimeur>/<int:type>",
           methods=["GET", "POST"])
def update_escrimeur(id_escrimeur, type):
    from .form import escrimeur_form, escrimeur_form2
    if USER is None:
        return redirect(url_for('choose_sign'))
    if not isinstance(USER, Organisateur):
        return redirect(url_for('home'))
    modele = ModeleAppli()
    if type == 1:
        form = escrimeur_form()
        escrimeur = modele.get_escrimeur_bd().get_escrimeur_by_id(id_escrimeur)
        nom = form.name.data
        prenom = form.prenom.data
        date_naissance = form.date_naissance.data
        sexe = form.sexe.data
        categorie = modele.get_categorie_bd().get_categorie_by_id(
            form.categorie.data)
        club = modele.get_club_bd().get_club_by_id(form.club.data)
        licence = form.licence.data
        arbitre = True if form.arbitrage.data == "Oui" else False
        nom_utilisateur = form.nom_utilisateur.data
        escrimeur.set_nom(nom)
        escrimeur.set_prenom(prenom)
        escrimeur.set_date_naissance(date_naissance)
        escrimeur.set_sexe(sexe)
        escrimeur.set_categorie(categorie)
        escrimeur.set_club(club)
        escrimeur.set_licence(licence)
        escrimeur.set_nom_utilisateur(nom_utilisateur)
        escrimeur.set_arbitrage(arbitre)
        modele.get_escrimeur_bd().update_escrimeur(escrimeur)

    else :
        form = escrimeur_form2()
        nom = form.name.data
        prenom = form.prenom.data
        date_naissance = form.date_naissance.data
        sexe = form.sexe.data
        categorie = modele.get_categorie_bd().get_categorie_by_id(
            form.categorie.data)
        club = modele.get_club_bd().get_club_by_id(form.club.data)
        licence = form.licence.data
        arbitre = True if form.arbitrage.data == "Oui" else False
        nom_utilisateur = form.nom_utilisateur.data
        escrimeur = Escrimeur(1, nom, prenom, sexe, date_naissance,
                              prenom.lower(), "mdp", licence, None,
                              club, categorie, arbitre)
        modele.get_escrimeur_bd().insert_escrimeur(escrimeur)
    modele.close_connexion()
    return redirect(url_for('admin_escrimeur'))


@app.route("/admin/ajouter_escrimeur", methods=["GET", "POST"])
def ajouter_escrimeur():
    from .form import escrimeur_form2
    if USER is None:
        return redirect(url_for('choose_sign'))
    if not isinstance(USER, Organisateur):
        return redirect(url_for('home'))
    form = escrimeur_form2()
    return render_template("Admin/Escrimeur/add_escrimeur.html",
                           user=USER,
                           title="Ajouter escrimeur",
                           form=form)

# Lieu


@app.route("/admin/lieux")
def admin_lieu():
    if USER is None:
        return redirect(url_for('choose_sign'))
    if not isinstance(USER, Organisateur):
        return redirect(url_for('home'))
    modele = ModeleAppli()
    les_lieux = modele.get_lieu_bd().get_all_lieu2()
    modele.close_connexion()
    return render_template("Admin/Lieux/lieux.html",
                           user=USER,
                           lieux=les_lieux)


@app.route("/admin/supprimer_lieux/<int:id_lieu>", methods=["GET", "POST"])
def supprimer_lieu(id_lieu):
    if USER is None:
        return redirect(url_for('choose_sign'))
    if not isinstance(USER, Organisateur):
        return redirect(url_for('home'))
    modele = ModeleAppli()
    modele.get_lieu_bd().delete_lieu(id_lieu)
    modele.close_connexion()
    return redirect(url_for('admin_lieu'))


@app.route("/admin/modifier_lieux/<int:id_lieu>", methods=["GET", "POST"])
def modifier_lieu(id_lieu):
    from .form import lieu_form
    if USER is None:
        return redirect(url_for('choose_sign'))
    if not isinstance(USER, Organisateur):
        return redirect(url_for('home'))
    modele = ModeleAppli()
    lieu = modele.get_lieu_bd().get_lieu_by_id(id_lieu)
    form = lieu_form()
    form.description.data = lieu.get_description()
    form.adresse.data = lieu.get_adresse()
    modele.close_connexion()
    return render_template("Admin/Lieux/modifier_lieu.html",
                           user=USER,
                           title="Modification lieu",
                           lieu=lieu,
                           form=form)


@app.route("/admin/modifier_lieux/<int:id_lieu>/<int:type>",
           methods=["GET", "POST"])
def update_lieu(id_lieu, type):
    from .form import lieu_form, lieu_form2
    if USER is None:
        return redirect(url_for('choose_sign'))
    if not isinstance(USER, Organisateur):
        return redirect(url_for('home'))
    modele = ModeleAppli()
    if type == 1:
        form = lieu_form()
        lieu = modele.get_lieu_bd().get_lieu_by_id(id_lieu)
        adresse = form.adresse.data
        description = form.description.data
        print("adresse", adresse)
        print("description", description)
        lieu.set_description(description)
        lieu.set_adresse(adresse)
        modele.get_lieu_bd().update_lieu(lieu)
    else:
        form = lieu_form2()
        adresse = form.adresse.data
        description = form.description.data
        lieu = Lieu(1, description, adresse)
        modele.get_lieu_bd().insert_lieu(lieu)
    modele.close_connexion()
    return redirect(url_for('admin_lieu'))


@app.route("/admin/ajouter_lieu", methods=["GET", "POST"])
def ajouter_lieu():
    from .form import lieu_form2
    if USER is None:
        return redirect(url_for('choose_sign'))
    if not isinstance(USER, Organisateur):
        return redirect(url_for('home'))
    form = lieu_form2()
    return render_template("Admin/Lieux/add_lieu.html", user=USER, title="Ajouter lieu", form=form)
  
# Competition


@app.route("/admin/competitions")
def admin_competition():
    if USER is None:
        return redirect(url_for('choose_sign'))
    if not isinstance(USER, Organisateur):
        return redirect(url_for('home'))
    modele = ModeleAppli()
    les_competitions = modele.get_competition_bd().get_all_competition2()
    modele.close_connexion()
    return render_template("Admin/Competition/competitions.html",
                           user=USER,
                           compets=les_competitions)


@app.route("/admin/supprimer_competitions/<int:id_competition>",
           methods=["GET", "POST"])
def supprimer_competition(id_competition):
    if USER is None:
        return redirect(url_for('choose_sign'))
    if not isinstance(USER, Organisateur):
        return redirect(url_for('home'))
    modele = ModeleAppli()
    modele.get_competition_bd().delete_competition(id_competition)
    modele.close_connexion()
    return redirect(url_for('admin_competition'))


@app.route("/admin/modifier_competitions/<int:id_competition>",
           methods=["GET", "POST"])
def modifier_competition(id_competition):
    from .form import competition_form
    if USER is None:
        return redirect(url_for('choose_sign'))
    if not isinstance(USER, Organisateur):
        return redirect(url_for('home'))
    modele = ModeleAppli()
    competition = modele.get_competition_bd().get_competition_by_id(
        id_competition)
    form = CompetitionForm()
    form.name.data = competition.get_nom()
    form.date.data = competition.get_date()
    form.date_fin_inscripiton.data = competition.get_date_fin_inscription()
    form.categorie.process_data(competition.get_categorie().get_id())
    form.saison.process_data(competition.get_saison())
    form.arme.process_data(competition.get_arme().get_id())
    form.lieu.process_data(competition.get_lieu().get_id())
    form.coefficient.data = competition.get_coefficient()
    modele.close_connexion()
    return render_template("Admin/Competition/modifier_competition.html",
                           user=USER,
                           title="Modification competition",
                           competition=competition,
                           form=form)



@app.route("/admin/modifier_competitions/<int:id_competition>/<int:type>",
           methods=["GET", "POST"])
def update_competition(id_competition, type):
    from .form import competition_form, competition_form2
    if USER is None:
        return redirect(url_for('choose_sign'))
    if not isinstance(USER, Organisateur):
        return redirect(url_for('home'))
    modele = ModeleAppli()
    if type == 1:
        form = competition_form()
        competition = modele.get_competition_bd().get_competition_by_id(
            id_competition)
        nom = form.name.data
        date = form.date.data
        date_fin_inscription = form.date_fin_inscripiton.data
        categorie = modele.get_categorie_bd().get_categorie_by_id(
            form.categorie.data)
        saison = form.saison.data
        arme = modele.get_arme_bd().get_arme_by_id(form.arme.data)
        lieu = modele.get_lieu_bd().get_lieu_by_id(form.lieu.data)
        coefficient = form.coefficient.data
        competition.set_nom(nom)
        competition.set_date(date)
        competition.set_date_fin_inscription(date_fin_inscription)
        competition.set_categorie(categorie)
        competition.set_saison(saison)
        competition.set_arme(arme)
        competition.set_lieu(lieu)
        competition.set_coefficient(coefficient)
        modele.get_competition_bd().update_competition(competition)
    else :
        form = competition_form2()
        nom = form.name.data
        date = form.date.data
        date_fin_inscription = form.date_fin_inscripiton.data
        categorie = modele.get_categorie_bd().get_categorie_by_id(
            form.categorie.data)
        saison = form.saison.data
        arme = modele.get_arme_bd().get_arme_by_id(form.arme.data)
        lieu = modele.get_lieu_bd().get_lieu_by_id(form.lieu.data)
        coefficient = form.coefficient.data
        competition = Competition(1, nom, date, date_fin_inscription, saison,
                                  lieu, arme, categorie, coefficient)
        modele.get_competition_bd().insert_competition(competition)
    modele.close_connexion()
    return redirect(url_for('admin_competition'))


@app.route("/admin/ajouter_competition", methods=["GET", "POST"])
def ajouter_competition():
    from .form import competition_form2
    if USER is None:
        return redirect(url_for('choose_sign'))
    if not isinstance(USER, Organisateur):
        return redirect(url_for('home'))
    form = competition_form2()
    return render_template("Admin/Competition/add_competition.html",
                           user=USER,
                           title="Ajouter competition",
                           form=form)


@app.route("/participants/<id_competition>", methods=["GET", "POST"])
def participants(id_competition):
    from .form import heure_debut_form

    form = heure_debut_form()
    try:
        modele = ModeleAppli()
        competition = modele.get_competition_bd().get_competition_by_id(id_competition)
        inscription = modele.get_inscrire_bd().get_all_inscrit_compet(competition)
        inscrits = []
        for i in inscription:
            inscrits.append(modele.get_escrimeur_bd().get_escrimeur_by_id(i.get_id_escrimeur()))

        arbitrages = modele.get_inscrire_arbitre_bd().get_arbitre_by_competition(competition)
        arbitres = []
        for element in arbitrages:
            arbitres.append(modele.get_escrimeur_bd().get_escrimeur_by_id(element.get_id_escrimeur()))
        poules = modele.get_poule_bd().get_poules_by_compet(competition.get_id())
        fini = any(element.is_finis() for element in poules)
        fini = True

        modele.close_connexion()
    except Exception as e:
        print(e)
        flask.abort(404)
    finally:
        modele.close_connexion()

    if request.method == 'POST':
        heure = form.heure.data
        type = form.type.data
        if type == 1:
            return redirect(url_for('generation_poule', id_competition=id_competition, heure_debut=heure))
        if type == 2:
            return redirect(url_for('generation_phase_finale', id_competition=id_competition, heure_debut=heure))

    return render_template("arbitre/participants.html", competition=competition, inscrits=inscrits,
                           arbitres=arbitres, form=form, fini=fini)


@app.route("/generation_poule/<id_competition>/<heure_debut>")
def generation_poule(id_competition, heure_debut):
    modele = ModeleAppli()
    competition = modele.get_competition_bd().get_competition_by_id(
        id_competition)
    print("competition", competition)
    modele.get_competition_bd().generate_poule_compet(competition.get_id(), heure_debut)
    modele.close_connexion()
    return redirect(url_for('poule', id_competition=id_competition, nb=0))


@app.route("/arbitrage")
def arbitrage():
    if USER is None:
        return redirect(url_for('choose_sign'))
    modele = ModeleAppli()
    id_compet_arbitre = modele.get_inscrire_arbitre_bd(
    ).get_all_compet_arbitre(USER.get_id())
    competitions = []
    for id_compet in id_compet_arbitre:
        competitions.append(
            modele.get_competition_bd().get_competition_by_id(id_compet))

    modele.close_connexion()
    return render_template("arbitre/acceuil_arbitre.html",
                           competitions=competitions)


@app.route("/arbitrage/<id_competition>")
def arbitrage_competition(id_competition):
    modele = ModeleAppli()
    competition = modele.get_competition_bd().get_competition_by_id(
        id_competition)
    poules = modele.get_poule_bd().get_poules_by_compet(competition)
    modele.close_connexion()
    return render_template("arbitre/arbitrage.html", competition=competition, poules=poules)

@app.route("/arbitrage/<id_competition>/classement/<full>")
def podium(id_competition, full):
    modele = ModeleAppli()
    competition = modele.get_competition_bd().get_competition_by_id(id_competition)
    phase_finale = modele.get_phase_finale_bd().get_phase_finale_by_competition(competition)
    if phase_finale is not None:
        matchs = modele.get_match_bd().get_match_by_phase(phase_finale.get_id_phase_f())
        escrimeurs_matchs = []
        if matchs is not None:
            for match in matchs:
                escrimeur_1 = modele.get_escrimeur_bd().get_escrimeur_by_id(match.get_id_escrimeur1())
                escrimeur_2 = modele.get_escrimeur_bd().get_escrimeur_by_id(match.get_id_escrimeur2())
                if escrimeur_1 is not None and escrimeur_1 not in escrimeurs_matchs:
                    escrimeurs_matchs.append(escrimeur_1)
                if escrimeur_2 is not None and escrimeur_2 not in escrimeurs_matchs:
                    escrimeurs_matchs.append(escrimeur_2)

    else:
        escrimeurs_matchs = None

    return render_template("arbitre/podium.html", competition=competition, escrimeurs=escrimeurs_matchs, full=full)

@app.route("/phase_finale/<id_competition>", methods=["GET", "POST"])
def phase_finale(id_competition):
    modele = ModeleAppli()
    competition = modele.get_competition_bd().get_competition_by_id(id_competition)
    la_phase = modele.get_phase_finale_bd().get_phase_finale_by_compet(id_competition)
    liste_match = la_phase.get_les_matchs()
    modele.close_connexion()
    nb_escrimeur = 8
    nombre = competition.get_puissance_sup(nb_escrimeur)
    liste_match_by_tour: list[list] = []
    cpt = 0
    for i in range(nombre):
        un_tour = []
        for match in range(cpt, cpt + nb_escrimeur // 2):
            if match < len(liste_match):
                un_tour.append(liste_match[match])
            else:
                un_tour.append(None)
            cpt += 1
        nb_escrimeur = nb_escrimeur // 2
        liste_match_by_tour.append(un_tour)
    print(liste_match_by_tour)
    return render_template("page_phase_finale_compet.html", compet=competition, phase=la_phase,
                           les_matchs=liste_match_by_tour)


@app.route("/generation_phase_finale/<id_competition>/<heure_debut>")
def generation_phase_finale(id_competition, heure_debut):
    modele = ModeleAppli()
    competition = modele.get_competition_bd().get_competition_by_id(id_competition)
    modele.get_competition_bd().generate_phase_finale_compet(competition.get_id(), heure_debut)
    modele.close_connexion()
    print('Phase finale générée')
    return redirect(url_for('phase_finale', id_competition=id_competition))
