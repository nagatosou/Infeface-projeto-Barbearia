import PySimpleGUI as sg
from backend_menu import backend_menu  # Importe a classe backend_menu corretamente

layout = [
    [sg.Text('Login')],
    [sg.InputText(key='username')],
    [sg.Text('Senha')],
    [sg.InputText(key='password', password_char='*')],
    [sg.Button('Login'), sg.Button('Cadastrar'), sg.Exit("Sair")],
]

window = sg.Window('Sistema de Login', layout)
menu = backend_menu()  # Crie uma instância da classe backend_menu

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    if event == 'Login':
        username = values['username']
        password = values['password']
        if menu.verificar_login(username, password):  # Use menu.verificar_login()
            window.close()
            menu_layout = [
                [sg.Button("Cadastro cliente")],
                [sg.Button("Cadastro dados")],
                [sg.Button("Cadastro Plano")],
                [sg.Button("Voltar login")],  # Corrija o texto do botão
                [sg.Exit()]
            ]
            menu_window = sg.Window("Menu Geral", menu_layout)

            while True:
                menu_event, _ = menu_window.read()
                if menu_event == sg.WINDOW_CLOSED or menu_event == 'Exit':
                    break
                if menu_event == 'Cadastro cliente':
                    # Faça algo quando o botão "Cadastro cliente" for clicado
                    pass  # Adicione sua lógica aqui
                elif menu_event == 'Cadastro dados':
                    # Faça algo quando o botão "Cadastro dados" for clicado
                    pass  # Adicione sua lógica aqui
                elif menu_event == 'Cadastro Plano':
                    # Faça algo quando o botão "Cadastro Plano" for clicado
                    pass  # Adicione sua lógica aqui
                elif menu_event == 'Voltar login':
                    # Faça algo quando o botão "Voltar login" for clicado
                    pass  # Adicione sua lógica aqui

            menu_window.close()
        else:
            sg.popup('Usuário ou senha incorretos. Tente novamente.')

window.close()

