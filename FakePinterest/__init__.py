from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db" #poderia ter colocado em qualquer outra linguam sql para criar 

database = SQLAlchemy(app)

from FakePinterest import routes #essa importação sempre vai vir por último