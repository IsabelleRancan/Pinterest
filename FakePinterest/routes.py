# arquivo que vão as rotas do nosso site

from flask import render_template, url_for
from FakePinterest import app
from flask_login import login_required

@app.route("/")
def homepage(): #a importação url_for permite pegar o link pelo nome da função e não pelo link da route
    return render_template("homepage.html")

@app.route("/perfil/<usuario>") #o nome que vai aparecer dentro do HTML é o que o usuário digitar na barra da URL
@login_required
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)