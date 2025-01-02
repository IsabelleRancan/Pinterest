from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db" #poderia ter colocado em qualquer outra linguam sql para criar 
app.config["SECRET_KEY"] = "f0cdec1c9340df3a6664c991663b0355"
app.config["UPLOAD_FOLDER"] = "static/fotos_posts" #essa variável é que define que as fotos postadas serão armazenadas na pasta static

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"

from FakePinterest import routes #essa importação sempre vai vir por último