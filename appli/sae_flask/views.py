from .app import app
from flask import render_template

@app.route("/")
def home():
    return render_template(
        "home.html"
    )

@app.route("/connexion_inscription")
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

@app.route("/connexion/<nom>")
def connexion(nom):
    return render_template("page_connexion.html", nom=nom)
