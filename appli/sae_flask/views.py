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


@app.route("/choisir_statut")
def choisir_statut():
    return render_template(
        "choisir_statut.html"
    )


@app.route("/inscription")
def inscription():
    return render_template(
        "page_inscription.html"
    )

# @app.route("/connexion")
# def connexion():
#     return render_template(
#         "page_connexion.html"
#     )