import psycopg2




def cadastrar_funcionario(connection, nome, cpf, senha):
    try:
        cursor = connection.cursor()

        cursor.execute("INSERT INTO usuarios (loguin, cpf, senha) VALUES (%s, %s, %s)", (nome, cpf, senha))
        connection.commit()

        cursor.close()
        return True
    except (Exception, psycopg2.Error) as error:
        print(f"Erro ao inserir usuário no banco de dados: {str(error)}")
        return False
    
    
    
    

    
def verificar_usuario_cadastrado(connection, loguin):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE loguin = %s", (loguin,))
        user_exists = cursor.fetchone()
        cursor.close()

        return user_exists is not None

    except (Exception, psycopg2.Error) as error:
        print(f"Erro ao verificar usuário cadastrado: {str(error)}")
        return False   
    
def verificar_login_senha(connection, loguin, senha):
    if not verificar_usuario_cadastrado(connection, loguin):
        return False, "Usuário não cadastrado"

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE loguin = %s AND senha = %s", (loguin, senha))
        result = cursor.fetchone()
        cursor.close()

        if result:
            return True, None  # Login bem-sucedido
        else:
            return False, "Credenciais inválidas"

    except (Exception, psycopg2.Error) as error:
        print(f"Erro ao verificar login e senha: {str(error)}")
        return False, "Erro ao verificar login e senha"
    
    
def registrar_corte(connection, user, valor, cpf):
    try:
        cursor = connection.cursor()

        cursor.execute("INSERT INTO cortes (operador, quantidade, preço) VALUES (%s, %s, %s)", (user, valor, cpf))
        connection.commit()

        cursor.close()
        return True
    except (Exception, psycopg2.Error) as error:
        print(f"Erro ao inserir usuário no banco de dados: {str(error)}")
        return False 