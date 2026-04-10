from database.conexao import conectar

def capturando_produtos():

    conexao, cursor = conectar()

    cursor.execute("SELECT codigo, produto, descricao, preco, destaque, foto, disponibilidade FROM produtos;")

    produto = cursor.fetchall()

    conexao.close()

    return produto


def rec_destaque():
    conexao, cursor = conectar()
    cursor.execute("""
                    SELECT destaque, foto from produtos WHERE destaque = 1;
                    """)
    resultado = cursor.fetchall()
    conexao.close()
    return resultado


def recuperar_produto(codigo:int):
    conexao, cursor = conectar()
    cursor.execute("""
                    SELECT codigo, produto, descricao, preco, destaque, foto, disponibilidade FROM produtos WHERE codigo = %s;
                    """, [codigo])
    resultado = cursor.fetchone()
    conexao.close()
    return resultado











