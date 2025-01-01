# Pinterest
Este é um repositório destinado ao desenvolvimento do projeto Fake Pinterest. 

AULA 03:
    -> Criação de um ambiente virtual para rodar o projeto 

AULA 04:
    -> Criando páginas em HTML e conectando a main.py 
    -> Criando a pasta 'templates' para poder colocar os meus arquivos do HTML 
    -> Aprendendo a usar o render_template

AULA 05:
    -> Rotas e páginas dinâmicas 
    -> ENtendendo como criar vários perfis de usuário sem ter que criar um apágina de HTML para cada uma delas 
    -> Entedendo como passar links das páginas pelas funções e links de sites externos 

AULA 06: 
    -> Transformando a homepage em um arquivos base HTML para não precisar ficar reescrevendo várias vezes 
    -> Usando estruturas em Python de bloco dinâmico para poder criar os blocos de conteúdo no HTML

AULA 7:
    -> Reestruturando o projeto e criando mais arquivos:
    1 - Criamos a pasta do projeto FakePinterest 
    2 - Dentro dessa pasta criamos os arquivos:
        |__init__ -> contém o inicio de todo o projeto, nele temos a importação do flask, a criação do app e a importação das rotas
        |forms -> vai possuir todos os formulários que criarmos para o nosso site 
        |models -> vai ser onde o nosso banco de dados vai estar 
        |routes  -> contém todas as rotas do site

    -> Na main(projeto principal que está fora da pasta) ficou a importação do aplicativo já criado na pasta init e o debug da aplicação, ou seja, ele está executando o código
    Essas são as alteração está o presente momento 

    *Essa vai ser a estrutura padrão que todos os projetos que criarmos em Flask vão ter

AULA 08:
    -> Criação do Banco de Dados
    1 - Baixamos o SQLAlchemy no nosso ambiente virtual 
    2 - Adicionamosb algumas coisas no nosso arquivo de init:
        from flask_sqlalchemy import SQLAlchemy - importamos o alchemy
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db" - comando utilizado para criar o banco de dados, nesse caso vai ser em SQLLite e o nome do arquivo é 'comunidade.bd'
        database = SQLAlchemy(app) - estamos chamando o aplicativo 
    3 - Criamos um arquivo do lado de fora da pasta FakePinterest chamado 'criar_banco', esse arquivo não é necessário no projeto final, mas utilizamos ele agora para criar o bd e se necessário fazer algumas modificações
    4 - A pasta 'instance' foi criada, é dentro dela que está o nosso bd
    5 - Vamos criar as nossas tabelas dentro do arquivo 'models'
    6 - Importamos as tabelas no 'criar_banco', apagamos o banco vazio e executamos o arquivo 'criar' de novo 

AULA 09:
    -> Implementando um sistema de login e segurança
    1 - instalando flask-login flask-bcrypt
    2 - fazendo as importação necessárias no arquivo init 
    3 - criando o arquivo chave aleatória e passando para o arquivo init 
    4 - Fazendo a importação de usermixin no arquivo models
    5 - Apagar o banco de dados novamente 
    6 - Criando uma função que vai encontrar o usuário pelo seu id usando a importação UserMixin e o decorador @login_manager no arquivos models 
    7 - Criar o banco de dados novamente utilizando o arquivo 'criar_banco' 
    8 - Mexendo no arquivo routes para impedir que qualquer pessoa possa acessar o página de perfil utilizando a importação e o decorador @login_required 

AULA 10:
    -> Criando os formulários de login 
    1 - Instalando mais algumas dependencias do Flask: pip install flask-wtf, pip install email_validator;
    2 - Fazer a importação das dependencias instaladas no arquivo 'forms.py';
    3 - Criação das classes de 'acessar conta' e 'criar conta':
        inserimos os campos com os seus tipos correspondentes e inserimos seus validaroes que já haviam sido importados no arquivo 
    4 - Fazemos uma validação para que apenas uma conta possa ser criada por email 

AULA 11:
    -> Implementando os formulários de login na 'Homepage'
