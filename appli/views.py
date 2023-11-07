from .app import app
from flask import render_template, url_for , redirect
from appli.modele import *
from .commands import *
from .views import *
from .modele.connexion_bd import ConnexionBD

user = "332948"
passwd = "SAE-EscrimeBUT2&"
host = "mysql-sae-escrime.alwaysdata.net"
database = "sae-escrime_sae"

