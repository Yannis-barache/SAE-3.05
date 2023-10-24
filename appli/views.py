from .app import app
from flask import render_template, url_for , redirect
from appli.modele import *
from .commands import *
from .views import *
from .models import *

user = "332948"
passwd = "SAE-EscrimeBUT2&"
host = "mysql-sae-escrime.alwaysdata.net"
database = "sae-escrime_sae"

connexion=ouvrir_connexion(user,passwd,host,database)

@app.route('/')
def home():
    recup=get_orga(connexion)
    organisateurs=[]
    for orga in recup:
        organisateurs.append(orga.get_nom())

    return render_template('home.html', organisateurs=organisateurs)

