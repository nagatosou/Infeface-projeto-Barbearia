import PySimpleGUI as sg
import psycopg2
import io
import os
import platform
import sys
sys.path.append(r'C:\Users\daniel.reis\Desktop\ProjetcBarber')
from system import database, controller

def  menu_user(connection, usuario_logado):
            layout_opcoes = [
                [sg.Text(f"Bem-vindo, {usuario_logado}!")],
                [sg.Button("Cadastrar Cliente")],
                [sg.Button("Estoque")],
                [sg.Button("Consulta")],
                [sg.Button("Sair")]
            ]

            layout_opcoes = sg.Window('CADASTRO', layout_opcoes, size=(400, 340), resizable=True)

            while True:
                eventos_opcoes, valores_opcoes = layout_opcoes.read()

                if eventos_opcoes == sg.WIN_CLOSED or eventos_opcoes == 'Sair':
                    layout_opcoes.close()
                    break
                
                
    