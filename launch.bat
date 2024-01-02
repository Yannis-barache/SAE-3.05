@echo off

call venv\Scripts\activate.bat
python appli/sae_flask/menu_choix.py

set "vide= ''"
for /f "tokens=2 delims==" %%i in ('findstr /i "locale" config.ini') do set "locale=%%i"
if not "%locale%"=="%vide%" (
    start http://127.0.0.1:5000
    flask run
)