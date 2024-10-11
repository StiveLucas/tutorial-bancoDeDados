import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

#Criando Banco de dados.
#Cria conexão com banco de dados.
db = create_engine("sqlite:///meubanco.db")

#CREATE DATABASE meubanco.
Session =  sessionmaker(bind =db)
session = Session()

#I/O
#I - input (Entrada)
#O - output(Saída)

#Abrindo uma conexão

Base = declarative_base()

#Criando tabela
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    #Definindo atributos da classe.
    def __init__(self, nome: str, email: str, senha: str):

        self.nome = nome
        self.email = email
        self.senha = senha

#Criando tabela no banco de dados
Base.metadata.create_all(bind=db)

usuario = Usuario(senha="123", nome="lucas", email="luc1234@ggmail")
session.add(usuario)
session.commit()

#Mostrando conteúdo do banco de dados
lista_usuarios = session.query(Usuario).all()

for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.email}")

#Deletando um usuário.
print("\nExcluindo usuário no banco de dados.")
email_usuario = input("Informe o e-mail do usuário:")
usuario = session.query(Usuario).filter_by(email = email_usuario).first()
session.delete(usuario)
session.commit()
print("\nUsuário deletado com sucesso.")

#Mostrando conteúdo do banco de dados.
print("\nListando usuários no banco de dados.")
lista_usuarios = session.query(Usuario).all()

for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.email}")

#Atualiza um usuário.
print("\nAtualizando os dados do usuário.")

email_usuario = input("Informe o e-mail do usuário:")

usuario = session.query(Usuario).filter_by(email = email_usuario).first()
if usuario:
    usuario.nome = input("Digite seu nome:")
    usuario.senha = input("Digite sua senha:")
    usuario.email = input("Digite seu email:")
    session.commit()
else:
    print("\nUsuário não encontrado")

#Pesquisando um usuário.
print("Pesquisando um usuário pelo e-mail.")

email_usuario = input("Informe o e-mail do usuário:")

usuario = session.query(Usuario).filter_by(email =email_usuario).first()

if usuario:
    print(f"{usuario.id} - {usuario.nome} - {usuario.email}")

else:
    print("Usuário não encontrado.")

#Fechando conexão.
session.close()