@echo off

call venv\Scripts\activate.bat
cd appli/sae_flask
python menu_choix.py
cd ../modele

set "vide= True"
for /f "tokens=2 delims==" %%i in ('findstr /i "locale" constantes.py') do set "locale=%%i"
if not "%locale%"=="%vide%" (
    cd ..
    start http://127.0.0.1:5000
    flask run
)