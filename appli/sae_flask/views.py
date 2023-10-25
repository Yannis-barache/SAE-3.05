from .app import app
from flask import render_template

@app.route("/")
def home():
    return render_template(
        "page_connexion.html"
    )

@app.route("/connexion")
def connexion():
    return render_template(
        "page_connexion.html"
    )