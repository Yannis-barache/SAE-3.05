#!/bin/bash
source venv/bin/activate
python3 appli/sae_flask/menu_choix.py
vide=" ''"
locale=$(grep 'locale' config.ini | cut -d "=" -f 2)
echo "$locale"
echo "$vide"
# shellcheck disable=SC2053
if [ $locale != $vide ]
then
  python3 -m webbrowser http://127.0.0.1:5000
  flask run
fi