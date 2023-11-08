@echo off

python -m venv venv

call venv\Scripts\activate.bat

pip install -r requirements.txt

cd appli
call echo FLASK_APP=sae_flask > .flaskenv
call echo FLASK_DEBUG=True >> .flaskenv