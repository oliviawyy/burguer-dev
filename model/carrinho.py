from database.conexao import conectar

def recuperar_carrinho(usuario:str) -> list:
    conexao, cursor = conectar()
    cursor.execute("""
                    SELECT 	carrinhos.cod_carrinho,
		                    carrinhos.usuario_id,
                            carrinhos.data,
                            carrinhos.finalizado,
                            produtos.produto,
                            itens_do_carrinho.quantidade,
                            produtos.preco,
                            produtos.foto
                    FROM carrinhos
                    INNER JOIN itens_do_carrinho ON carrinhos.cod_carrinho = itens_do_carrinho.cod_carrinho
                    INNER JOIN produtos ON produtos.codigo = itens_do_carrinho.cod_produto
                    WHERE carrinhos.usuario_id = %s;
        
                    """, [usuario])
    resultado = cursor.fetchone()
    conexao.close()
    return resultado


