# arquivo que vão as rotas do nosso site

from flask import render_template, url_for
from FakePinterest import app
from flask_login import login_required
from FakePinterest.forms import FormLogin, FormCriarConta

@app.route("/", methods=["GET", "POST"]) #colocamos esses métodos sempre que tivermos formulários nas páginas de HTML
def homepage(): #a importação url_for permite pegar o link pelo nome da função e não pelo link da route
    formlogin = FormLogin()
    return render_template("homepage.html", form=formlogin)

@app.route("/criarconta", methods=["GET", "POST"])
def criarconta():
    formcriarconta = FormCriarConta()
    return render_template("criarconta.html", form=formcriarconta) #form é o nome que a variável vai ter no HTML

@app.route("/perfil/<usuario>") #o nome que vai aparecer dentro do HTML é o que o usuário digitar na barra da URL
@login_required
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)