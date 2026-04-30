CREATE DATABASE IF NOT EXISTS DevBurguer;
USE DevBurguer;

CREATE TABLE IF NOT EXISTS usuarios (
    usuario VARCHAR(100) NOT NULL PRIMARY KEY,
    nome VARCHAR(100) DEFAULT "ANONIMO",
    senha VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS produtos (
    codigo INT AUTO_INCREMENT PRIMARY KEY,
    produto VARCHAR(80) NOT NULL,
    descricao VARCHAR(900),
    preco FLOAT,
    destaque BOOL DEFAULT 0,
    foto VARCHAR(300),
    disponibilidade BOOL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS carrinhos (
    cod_carrinho INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id VARCHAR(100),
    data DATETIME DEFAULT CURRENT_TIMESTAMP,
    finalizado BOOL DEFAULT 0,
    CONSTRAINT fk_carrinho_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario)
);

CREATE TABLE IF NOT EXISTS itens_do_carrinho (
    cod_item_carrinho INT AUTO_INCREMENT PRIMARY KEY,
    cod_carrinho INT,
    cod_produto INT,
    quantidade INT DEFAULT 1,
    CONSTRAINT fk_itenscarrinho_carrinhos FOREIGN KEY (cod_carrinho) REFERENCES carrinhos(cod_carrinho),
    CONSTRAINT fk_itens_carrinho_produtos FOREIGN KEY (cod_produto) REFERENCES produtos(codigo)
);

insert into produtos(produto, descricao, preco, destaque, foto, disponibilidade)
values("Godo Burguer", "Um lanche especial espera por voce com uma carne divina", 24.00, 1, "https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg?auto=compress&cs=tinysrgb&w=200", 1);


INSERT INTO `devburguer`.`usuarios` (`nome`, `usuario`, `senha`) VALUES ('olivia', 'oliviawyu', '123');
INSERT INTO `devburguer`.`usuarios` (`nome`, `usuario`, `senha`) VALUES ('ana', 'anadu', '777');







