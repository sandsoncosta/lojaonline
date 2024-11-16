from database import SessionLocal, init_db
from models import Usuario, Produto, Pedido, ItemPedido

# Inicializando o banco de dados
init_db()

# Função para criar um novo usuário
def criar_usuario(nome, email, senha):
    session = SessionLocal()
    try:
        novo_usuario = Usuario(nome=nome, email=email, senha=senha)
        session.add(novo_usuario)
        session.commit()
        session.refresh(novo_usuario)
        print(f"Usuário criado: {novo_usuario.nome} (ID: {novo_usuario.id})")
    finally:
        session.close()

# Função para listar todos os usuários
def listar_usuarios():
    session = SessionLocal()
    try:
        usuarios = session.query(Usuario).all()
        for usuario in usuarios:
            print(f"{usuario.id}: {usuario.nome} - {usuario.email}")
    finally:
        session.close()

# Executando o script
if __name__ == "__main__":
    # Criar usuários
    criar_usuario("João Silva", "joao@email.com", "senha123")
    criar_usuario("Maria Oliveira", "maria@email.com", "senha456")

    # Listar usuários
    print("Usuários cadastrados:")
    listar_usuarios()
