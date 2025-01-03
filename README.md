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
    5 - Quando vamos fazer uma busca por ID usamos o Get, quando é por outra informação usamos o FILTER

AULA 11:
    -> Implementando os formulários de login na 'Homepage'
    -> Vamos dividir a home page para ter o login dos usuarios
    1 - Vamos importar os formulários que criamos para o arquivo routes
    2 - Adicionamos os métodos GET e POST dentro do routes
    3 - Criamos as variáveis que vão aparecer no HTML
    4 - Adicionamos ao arquivo homepage os espaços para acessar a conta 
    5 - Criamos o arquivo "criarconta.html"
    6 - Copiamos o HTML da "homepage" e adicionamos os compos restantes

AULA 12:
    -> Implementando funcionalidades no login e criar conta
    1 - Acessamos o arquivo routes e passamos as informações necessárias para o usuário criar a conta
    2 - Criamos uma trava de segurança para que a senha do usuário não fique salva no bd, para isso fizemos:
    3 - Immportamos o bcrypt no arquivo routes
    4 - Criamos uma variável senha para salvar a senha criptografada com o hash
    5 - Importamos o banco de dados 
    6 - Salvamos a variável usuário com todas as informações dele no banco: 
    7 - Fazemos o ligin do usuário automáticamente
    8 - redirecionamos para a página de perfil
    9 - Criando o sistema de login na página home
    10 - Criando o sistema de logout:
    11 - Acessando o arquivo "pefil.html" e colocando o redirecionamento do botão para a página "logout"
    12 - Acessando novamnete o arquivi voutes e criando a página logout
    13 - Fazendo a importação de 'current_user' para poder deslogar - current_user significa o usuario que está logado
    14 - Quando vocês está logado, pode buscar qualquer perfil, quando não está ele vai redirecionar sempre para a página de home

AULA 13:
    -> Ajustando o perfil do usuário 
    1 - Mexemos na função 'perfil' do arquivo "routes.py" 
    2 - Verificamos se o usuário está vendo o próprio perfil ou não. Isso é importante porque se for o próprio perfil, ele vai conseguir editar as informações 
    3 - Atualizamos o arquivo "perfil.html" para exibir os perfis corretamente 
    4 - Criamos uma estrutura condicional python dentro do HTML para exibir as imagens do perfil 

AULA 14:
    -> Organizando os arquivos estáticos do projeto
    1 - Criação da pasta static com a imagem "default.png" 
    2 - Passando o caminho da imagem para o arquivo "perfil.html"
    3 - Criação de uma variável/configuração para definir que as fotos postadas pelo usuário vão ser salvas na pasta "static/fotos_posts"

AULA 15:
    -> Criando a funcionalidade de postar uma foto no perfil
    1 - Vamos criar um novo formiulário no arquivo "forms.py" chamado "FormFoto"
    2 - Retornamos o arquivo da foto no arquivo "routes"
    3 - Criamos as condições no arquivo "perfil.html" para exibir as imagens se existissem
    4 - Voltando ao arquivo "routes" criamos uma variável para armazenar o arquivo
    5 - criamos uma variável chamada nome_seguro para impedir que o usuário salve o arquivo com qualquer nome e quebre o nosso código
    6 - Para garantir que o nome do arquivo será alterado, importamos duas bibliotecas: import os; from werkzeug.utils import secure_filename
    7 - Salvamos o arquivo no banco de dados e na pasta do nosso projeto
    8 - Alteramos o for para poder exibir as imagens enviadas pelo usuário e vimos como fazer o html reconhecer variáveis 

AULA 16:
    -> Criar um feed do Pinterest
    1 - Criamos um arquivo "feed.html" para podermos colocar uma barra de navegação nele
    2 - Como a barra de navegação vai existir em algumas páginas e não em outras, criamos o arquivo "navbar.html" 
    3 - Criamos uma rota para o feed no arquivo "routes"
    4 - Definimos as páginas "feed" e "perfil" para podermos acessar na barra de navegação
    5 - Fazemos uma busca no bd dentro do arquivo "routes" para o feed retornar as imagens existentes 
    6 - Mudamos o botão "sair" e colocamos dentro da barra de navegação 
    7 - Fazemos com que ao clicar na foto, podemos acessar o perfil do usuário que postou a imagem:
    8 - Acessamos o arquivo "feed.html" e colocamos o link do perfil do usuário na foto 