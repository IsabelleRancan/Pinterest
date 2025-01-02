from FakePinterest import app, database
from FakePinterest.models import Usuario, Foto

# Criar registros
usuario1 = Usuario(username="admin", email="admin@example.com", senha="senha123")
usuario2 = Usuario(username="user", email="user@example.com", senha="senha456")

# Adicionar registros ao banco no contexto da aplicação
with app.app_context():  # Isso garante que o Flask tenha um contexto de aplicação ativo
    database.session.add_all([usuario1, usuario2])
    database.session.commit()

    print("Registros adicionados com sucesso!")
