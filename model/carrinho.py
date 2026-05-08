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
    resultado = cursor.fetchall()
    conexao.close()
    return resultado

def inserir_item(usuario_id,cod_produto,quantidade=1):
    conexao, cursor = conectar()
    cursor.execute("""
                    SELECT cod_carrinho FROM carrinhos
                    WHERE usuario_id = %s   
                    AND finalizado = 0
                    limit 1;
                    """, [usuario_id])
    resultado = cursor.fetchone()

    if resultado:
        codigo_carrinho = resultado["cod_carrinho"]
    else:
        cursor.execute("""
                        INSERT INTO carrinhos (usuario_id, finalizado)
                        VALUES (%s, 0);
                        """, [usuario_id])
        codigo_carrinho = cursor.lastrowid

    cursor.execute("""   
                    INSERT INTO itens_do_carrinho 
                            (cod_carrinho, cod_produto, quantidade)
                    VALUES 
                            (%s, %s, %s);
                    """, [codigo_carrinho, cod_produto, quantidade])
    conexao.commit()
    conexao.close



