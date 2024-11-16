from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL de conexão ao MySQL
# Substitua 'usuario', 'senha', 'host', 'porta', e 'banco' pelos valores do seu MySQL
DATABASE_URL = "mysql+pymysql://root@localhost:3306/lojaonline"

# Criando o engine do SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)

# Base para criação dos modelos
Base = declarative_base()

# Configuração da sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Função para inicializar o banco de dados
def init_db():
    Base.metadata.create_all(bind=engine)
