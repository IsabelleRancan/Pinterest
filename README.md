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
    