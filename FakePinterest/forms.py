# criar os formulários do nosso site
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField #importando os campos de texto, senha e etc 
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from FakePinterest.models import Usuario

class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Fazer login")

class FormCriarConta(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField("Nome de usuário", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField("Senha", validators=[DataRequired(), EqualTo("Senha")])
    botao_confirmacao = SubmitField("Criar Conta")

    def validate_email(self, email):
        usuario = Usuario.queryfilter_by(email=email.data).first() #quando a busca é por Id buscamos por get, se for qualquer outro tipo de busca, como nesse caso, então usamos o filter. Usamos o first para mostrar o primeiro usuário que já possuir esse email, acredito que sempre vai existir só um. Usamos email.data pq estamos pegando o dado que está dentro do campo email
        if usuario: 
            return ValidationError("Email já cadastrado, faça login para continuar")
