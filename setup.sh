#!/bin/bash
# Ce script permet de mettre en place l'environnement de travail pour le projet
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt

# On crée le .flaskenv
echo "FLASK_APP=appli" > .flaskenv
echo "FLASK_DEBUG=True" >> .flaskenv


