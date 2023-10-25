from flask import Flask
from flask_bootstrap import Bootstrap4

app = Flask(__name__)
app.config['BOOTSTRAP_SERVE_LOCAL']=True
bootstrap = Bootstrap4(app)


