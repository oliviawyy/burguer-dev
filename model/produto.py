from database.conexao import conectar

def capturando_produtos():

    conexao, cursor = conectar()

    cursor.execute("SELECT codigo, produto, descricao, preco, destaque, foto, disponibilidade FROM produtos;")

    produto = cursor.fetchall()

    conexao.close()

    return produto