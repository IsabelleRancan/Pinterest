# arquivo que vão as rotas do nosso site

from flask import render_template, url_for, redirect
from FakePinterest import app, database, bcrypt
from FakePinterest.models import Usuario, Foto
from flask_login import login_required, login_user, logout_user, current_user
from FakePinterest.forms import FormLogin, FormCriarConta

@app.route("/", methods=["GET", "POST"]) #colocamos esses métodos sempre que tivermos formulários nas páginas de HTML
def homepage(): #a importação url_for permite pegar o link pelo nome da função e não pelo link da route
    form_login = FormLogin()
    if form_login.validate_on_submit:
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data): #a segunda parte já retorna um booleano, por isso está no if
          login_user(usuario)  
          return redirect(url_for("perfil", usuario=usuario.username))
    return render_template("homepage.html", form=form_login)

@app.route("/criarconta", methods=["GET", "POST"])
def criar_conta():
    form_criarconta = FormCriarConta()
    if form_criarconta.validate_on_submit(): #nesse momento ele já passou por todas as validações que colocamos antes de poder enviar o formulário
        senha = bcrypt.generate_password_hash(form_criarconta.senha.data) #criando a variável senha, essa variável vai receber a senha criptografada em hash
        usuario = Usuario(username=form_criarconta.username.data, #criando o usuario que definimos em "models"; usuario=form_criarconta.username.data= formulário.campo.informação dentro do campo
                          email=form_criarconta.email.data, 
                          senha=senha) #colocamos a senha criptografada nesse campo 
        database.session.add(usuario) #adicionando usuario ao bd
        database.session.commit() #salvando essa alterações no BD
        login_user(usuario, remember=True) #fazendo o login do usuário e salvando o login nos coockies para ele n ter que logar sempre que trocar de página
        return redirect(url_for("perfil", usuario=usuario.username)) #redirecionando a pessoa para a página perfil
    return render_template("criarconta.html", form=form_criarconta) #form é o nome que a variável vai ter no HTML

@app.route("/perfil/<usuario>") #o nome que vai aparecer dentro do HTML é o que o usuário digitar na barra da URL
@login_required
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))