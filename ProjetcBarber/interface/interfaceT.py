import PySimpleGUI as sg
import platform
import sys
sys.path.append(r'C:\Users\daniel.reis\Desktop\ProjetcBarber')
from system import database, controller
import psycopg2
import cadmenu
import menu

try:
    connection = psycopg2.connect(
        user="postgres",
        password="@Adriamor123#",
        host="localhost",
        port="5432",
        database="bdBarber",
        options="-c client_encoding=utf-8"
    )

    database.criar_tabela_usuarios(connection)
    database.criar_tabela_Produtos(connection)
    database.criar_tabela_Clientes(connection)
    database.criar_tabela_cortes(connection)

except (Exception, psycopg2.Error) as error:
    sg.popup_error(f"Erro ao conectar ao banco de dados: {str(error)}")
    exit()

coluna_esquerda = [
    [sg.Text("MENU")],
    [sg.Text("Login:"), sg.Input(key="-Seuloguin-")],
    [sg.Text("Pass: "), sg.Input(key="-Senha-", password_char='*')], 
    [sg.Button("Entrar"), sg.Button("Sair")],
    [sg.Button("Cadastro")]
]

painel_central =[
    [sg.Text("CADASTRO DE CORTE")],
    [sg.Text("User:"), sg.Input(key="-USER-")],
    [sg.Text("Valor:"), sg.Input(key="-VALOR-")],
    [sg.Text("OP.CPF:"), sg.Input(key="-CPF-")],
    [sg.Button("Registrar")]
]

painel_direita = [
    [sg.Text("Relatório do Dia")],
    [sg.Output(size=(30, 10), key='-OUTPUT-')],  # Este é o elemento sg.Output
    [sg.Button('Atualizar Informações')]
]

layout_principal = [
    [
        sg.Column(coluna_esquerda, element_justification='left', pad=(10, 10), size=(300, 280)),
        sg.Column(painel_central, element_justification='center', pad=(10, 10), size=(300, 280)),
        sg.Column(painel_direita, justification='right', size=(400, 280)),
    ]
]

janela_principal = sg.Window('Barber', layout_principal, size=(1000, 340), resizable=True)



while True:
    eventos, valores = janela_principal.read()
    
    if eventos == 'Sair' or eventos == sg.WIN_CLOSED:
        janela_principal.close()
        break
    
    elif eventos == 'Cadastro':
        # Cria uma nova janela para o submenu sem fechar a janela principal
        cadmenu.cadastrar_funcionario(connection)
        
    elif eventos == 'Entrar':
        loguin = valores["-Seuloguin-"]
        senha = valores["-Senha-"]

        sucesso, mensagem_erro = controller.verificar_login_senha(connection, loguin, senha)

        if sucesso:
            # Se o login for bem-sucedido, chame o menu
            menu.menu_user(connection, loguin)
        else:
            # Se o login falhar, exiba uma mensagem de erro
            sg.popup_error(f"Erro ao fazer login: {mensagem_erro}")
            
            
    elif eventos == 'Registrar':
        loguin = valores["-USER-"]

    # Verificar se o usuário está cadastrado
        usuario_cadastrado = controller.verificar_usuario_cadastrado(connection, loguin)

        if usuario_cadastrado:
        # Se o usuário estiver cadastrado, continuar com o registro
            user = valores["-USER-"]
            valor = valores["-VALOR-"]
            cpf = valores["-CPF-"]

            sucesso, mensagem_erro = controller.registrar_corte(connection, user, valor, cpf)

            if sucesso:
                sg.popup("Corte registrado com sucesso!")
                janela_principal.close()
            else:
                sg.popup_error(f"Erro ao registrar corte: {mensagem_erro}")
        else:
           sg.popup_error("Usuário não cadastrado. Faça o cadastro antes de registrar um corte.")
        
    