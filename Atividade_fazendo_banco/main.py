import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

#Criando Banco.
db = create_engine("sqlite:///meubanco.db")

#Creando dataBase
Session = sessionmaker(bind=db)
session = Session()

#Abrindo conexão
Base = declarative_base()

#Criando tabela
class Aluno(Base):
    __tablename__ = "Alunos"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    ra = Column("R.A", String)
    nome = Column("nome", String)
    idade = Column("idade", Integer)
    email = Column("email", String)

    def __init__(self, nome:str, ra: str, idade: int, email: str):
        self.nome = nome
        self.ra = ra
        self.idade = idade
        self.email = email

#Criando tabela no banco de dados
Base.metadata.create_all(bind=db)

#Quando usar laços o save dos dados dentro do laço.
for i in range(2):
    ra = input("Digita seu ra:")
    nome = input("Digite seu nome:")
    idade = input("Digite sua idade:")
    email = input("Digite seu email:")
    print("\n")

    aluno = Aluno(ra= ra, nome=nome, idade=idade, email=email)
    session.add(aluno)
    session.commit()

#Mostrando conteúdo do banco de dados
lista_alunos = session.query(Aluno).all()

for aluno in lista_alunos:
    print(f"{aluno.id} - {aluno.ra} - {aluno.nome} - {aluno.idade} - {aluno.email}")