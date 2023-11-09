#!/bin/bash
source venv/bin/activate
cd appli/sae_flask
python3 menu_choix.py
cd ../modele
vide=" ''"
locale=$(grep 'locale' constantes.py | cut -d "=" -f 2)
echo $locale
echo $vide
if [ $locale != $vide ]
then
  cd ..
  python3 -m webbrowser http://127.0.0.1:5000
  flask run
fi

