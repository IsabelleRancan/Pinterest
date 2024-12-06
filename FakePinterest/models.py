# criar a estrutura do banco de dados 

from FakePinterest import database, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader #decorativo que está dizendo que é a função que carrega o usuário
def load_usuario(id_usuario): #essa função vai perminit encontrar o usuário 
    return Usuario.query.get(int(id_usuario)) #nome da tabale + query para buscar + get que vai pegar apenas o que tiver o id(se usássemos filter ele filtraria)

class Usuario(database.Model, UserMixin): #isso permite criar o bd em um formato que o bd entenda, e usermixin diz qual é a classe que vai gerenciar a estrutura de logins
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    fotos = database.relationship("Foto", backref="usuario", lazy=True) #essa coluna não vai exixtir no bd, é só um relacionamento

class Foto(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String, default="default.png") #a imagem foi criada como rexto pq vamos armazenar o local do sistema onde ela está (na pastinha static)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.now())
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False) #primeiro passamos os argumentos de posição e depois os que tem nome, por isso o nullable vai depois do 'ForeignKey'