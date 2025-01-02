# criar os formulários do nosso site
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from FakePinterest.models import Usuario

class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Fazer Login")

class FormCriarConta(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    username = StringField("Nome de usuário", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)]) #definindo o tamanho que a senha deve ter
    confirmacao_senha = PasswordField("Confirmar Senha", validators=[DataRequired(), EqualTo("senha")])
    botao_confirmacao = SubmitField("Criar Conta")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first() #vai filtrar pelo email e vai retornar o primeiro item dessa busca, quando vamos fazer uma busca por ID usamos o Get, quando é por outra informação usamos o FILTER
        #email.data vai pegar as informações que estão dentro do campo email
        if usuario:
            return ValidationError("Email já cadastrado, faça login para continuar")