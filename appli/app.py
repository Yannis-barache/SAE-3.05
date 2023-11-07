from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



app=Flask(__name__)
app.config['SECRET_KEY'] = "680be97a-dd71-49c4-ae19-bfcd20de936b"

# Pour la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://332948:SAE-EscrimeBUT2&@mysql-sae-escrime:3306/sae-escrime_sae'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)










# Pour les logs



