from database.conexao import conectar

class Usuarios():
    def __init__(self, usuario:str, senha:str, nome:str=None):
        self.usuario = usuario
        self.senha = senha
        self.nome = nome

    def cadastrar(self):
        conexao, cursor = conectar()
        cursor.execute("""
                        INSERT INTO usuarios (usuario, senha, nome)
                       VALUES (%s, %s, %s);
                        """, [self.usuario, self.senha, self.nome])
        conexao.commit()
        conexao.close()
        
    @staticmethod
    def verificar_usuario(usuario, senha):
        try:
            conexao, cursor = conectar()
    
            cursor.execute("""SELECT usuario, nome FROM usuarios WHERE usuario = %s AND senha = %s""", [usuario, senha])
            resultado = cursor.fetchone()
            conexao.close()
            return resultado 
        except Exception as erro:
            print(f"Erro no login: {erro}")
            return False