import PySimpleGUI as sg
import sys
sys.path.append(r'C:\Users\daniel.reis\Desktop\ProjetcBarber')
from system import database, controller
import psycopg2

def cadastrar_funcionario(connection):
    layout = [
        [sg.Text("Cadastro funcionário")],
        [sg.Text("Nome:"), sg.Input(key="-NOME-")],
        [sg.Text("CPF:"), sg.Input(key="-CPF-")],
        [sg.Text("Senha:"), sg.Input(key="-SENHA-", password_char='*')],
        [sg.Button("Cadastrar"), sg.Button("Sair")]
    ]

    window = sg.Window('CADASTRO', layout, size=(400, 340), resizable=True)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Sair':
            window.close()
            return False

        elif event == 'Cadastrar':
            nome = values["-NOME-"]
            cpf = values["-CPF-"]
            senha = values["-SENHA-"]
            
            sucesso = controller.cadastrar_funcionario(connection, nome, cpf, senha)
            
            if sucesso:
                sg.popup("Funcionário Cadastrado!")
                window.close()
                return True
            else:
                sg.popup_error("Erro ao cadastrar Funcionário. Verifique o console para mais detalhes.")
    
    window.close()
    return False
