from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db" #poderia ter colocado em qualquer outra linguam sql para criar 
app.config["SECRET_KEY"] = "c62e2ec92f63d22c9a85ed39accd5182"


database = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager=LoginManager(app)
login_manager.login_view = "homepage" #se o usuário não estiver logado, onde ele vai ser direcionado

from FakePinterest import routes #essa importação sempre vai vir por último