import pandas as pd
import smtplib
import time
import PySimpleGUI as sg
import psycopg2
from datetime import datetime

def criar_tabela_usuarios(connection):
    try:
        cursor = connection.cursor()

        # Verificar se a tabela 'usuarios' já existe
        cursor.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'usuarios')")
        table_exists = cursor.fetchone()[0]

        if not table_exists:
            # Criar a tabela 'usuarios'
            cursor.execute("""
                CREATE TABLE usuarios (
                    id SERIAL PRIMARY KEY,
                    loguin TEXT,
                    cpf NUMERIC,
                    senha TEXT
                )
            """)

            connection.commit()

            print("Tabela 'usuarios' criada com sucesso.")
        else:
            print("A tabela 'usuarios' já existe.")

        cursor.close()

    except (Exception, psycopg2.Error) as error:
        raise Exception(f"Erro ao criar tabela 'usuarios': {str(error)}")
    
#-------------------------------------------------------------------------------------------------------------------------------
    
def criar_tabela_Clientes(connection):
    try:
        cursor = connection.cursor()

        # Verificar se a tabela 'usuarios' já existe
        cursor.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'clientes')")
        table_exists = cursor.fetchone()[0]

        if not table_exists:
            # Criar a tabela 'usuarios'
            cursor.execute("""
                CREATE TABLE clientes (
                    id SERIAL PRIMARY KEY,
                    nome TEXT,
                    telefone VARCHAR(15),
                    cpf VARCHAR(14)
                )
            """)

            connection.commit()

            print("Tabela 'usuarios' criada com sucesso.")
        else:
            print("A tabela 'usuarios' já existe.")

        cursor.close()

    except (Exception, psycopg2.Error) as error:
        raise Exception(f"Erro ao criar tabela 'usuarios': {str(error)}")
      
#-----------------------------------------------------------------------------------------------------------------------------------
def criar_tabela_Produtos(connection):
    try:
        cursor = connection.cursor()

        # Verificar se a tabela 'usuarios' já existe
        cursor.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'produtos')")
        table_exists = cursor.fetchone()[0]

        if not table_exists:
            # Criar a tabela 'usuarios'
            cursor.execute("""
                CREATE TABLE produtos (
                    id SERIAL PRIMARY KEY,
                    item TEXT,
                    quantidade NUMERIC,
                    preço NUMERIC
                )
            """)

            connection.commit()

            print("Tabela 'usuarios' criada com sucesso.")
        else:
            print("A tabela 'usuarios' já existe.")

        cursor.close()

    except (Exception, psycopg2.Error) as error:
        raise Exception(f"Erro ao criar tabela 'usuarios': {str(error)}")
    
    
# ---------------------------------------------------------------------------------------------------


def criar_tabela_cortes(connection):
    try:
        cursor = connection.cursor()

        # Verificar se a tabela 'usuarios' já existe
        cursor.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'cortes')")
        table_exists = cursor.fetchone()[0]

        if not table_exists:
            # Criar a tabela 'usuarios'
            cursor.execute("""
                CREATE TABLE cortes (
                    id SERIAL PRIMARY KEY,
                    operador TEXT,
                    quantidade NUMERIC,
                    preço NUMERIC
                )
            """)

            connection.commit()

            print("Tabela 'cortes' criada com sucesso.")
        else:
            print("A tabela 'cortes' já existe.")

        cursor.close()

    except (Exception, psycopg2.Error) as error:
        raise Exception(f"Erro ao criar tabela 'cortes': {str(error)}")
 