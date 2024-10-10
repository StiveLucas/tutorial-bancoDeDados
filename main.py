import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

#Criando Banco de dados.
#Cria conexão com banco de dados.
db = create_engine("sqlalchemy:///meubanco.db")

#CREATE DATABASE meubanco.
Session =  sessionmaker(bin =db)
session = Session()

#I/O
#I - input (Entrada)
#O - output(Saída)

#Abrindo uma conexão

Base = declarative_base()

#Criando tabela
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    #Definindo atributos da classe.
    def __init__
