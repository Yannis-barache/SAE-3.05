from flask import Flask
from flask_bootstrap import Bootstrap4
from flask_login import LoginManager
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'appli/modele'))

from escrimeur import Escrimeur
from organisateur import Organisateur
from club import Club

app = Flask(__name__)
app.config['SECRET_KEY'] = "680be97a-dd71-49c4-ae19-bfcd20de936b"
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
login_manager = LoginManager(app)
login_manager.login_view = "connexion"
bootstrap = Bootstrap4(app)


@app.template_filter("is_escrimeur")
def is_escrimeur(user):
    return isinstance(user, Escrimeur)


@app.template_filter("is_organisateur")
def is_organisateur(user):
    return isinstance(user, Organisateur)


@app.template_filter("is_club")
def is_club(user):
    return isinstance(user, Club)




