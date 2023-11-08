from flask import Flask
from flask_bootstrap import Bootstrap4
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = "680be97a-dd71-49c4-ae19-bfcd20de936b"
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
login_manager = LoginManager(app)
login_manager.login_view = "connexion"
bootstrap = Bootstrap4(app)
