from database.conexao import conectar

class Usuarios():
    def cadastrar_usuario(nome, usuario, senha):
        try:
            conexao, cursor = conectar.conectar()

            cursor.execute("""INSERT INTO usuarios(nome, usuario, senha)VALUES(%s, %s, %s)""", [nome, usuario, senha])
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro:
            print(erro)
            return False
        

    def verificar_usuario(usuario, senha):
        try:
            conexao, cursor = conectar.conectar()

            cursor.execute("""SELECT usuario, senha from usuarios where usuario = %s""", [usuario])
            usuario = cursor.fetchone()
            conexao.commit()
            conexao.close()
            return True
        
        except Exception as erro:
            print(erro)
            return False