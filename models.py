from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

# Tabela Usuario
class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    senha = Column(String(255), nullable=False)

    # Relacionamento com pedido
    pedido = relationship("Pedido", back_populates="usuario")

# Tabela Pedido
class Pedido(Base):
    __tablename__ = "pedido"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuario.id"), nullable=False)
    data = Column(DateTime, default=datetime.utcnow)
    total = Column(Float, nullable=False)

    # Relacionamentos
    usuario = relationship("Usuario", back_populates="pedido")
    itens = relationship("ItemPedido", back_populates="pedido")

# Tabela Produto
class Produto(Base):
    __tablename__ = "produto"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    estoque = Column(Integer, nullable=False)

    # Relacionamento com itens de pedido
    itens = relationship("ItemPedido", back_populates="produto")

# Tabela ItemPedido
class ItemPedido(Base):
    __tablename__ = "itempedido"

    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("pedido.id"), nullable=False)
    produto_id = Column(Integer, ForeignKey("produto.id"), nullable=False)
    quantidade = Column(Integer, nullable=False)

    # Relacionamentos
    pedido = relationship("Pedido", back_populates="itens")
    produto = relationship("Produto", back_populates="itens")
