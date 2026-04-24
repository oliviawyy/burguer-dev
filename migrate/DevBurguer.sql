create database if not exists DevBurguer;
use DevBurguer;

CREATE TABLE if not exists produtos (
    codigo int auto_increment primary key,
    produto varchar(80) not null,
    descricao varchar(900),
    preco float,
    destaque bool default 0,
    foto varchar(300),
    disponibilidade bool default 1
);

insert into produtos(produto, descricao, preco, destaque, foto, disponibilidade)
values("Godo Burguer", "Um lanche especial espera por voce com uma carne divina", 24.00, 1, "https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg?auto=compress&cs=tinysrgb&w=200", 1);


INSERT INTO `devburguer`.`usuarios` (`nome`, `usuario`, `senha`) VALUES ('olivia', 'oliviawyu', '123');
INSERT INTO `devburguer`.`usuarios` (`nome`, `usuario`, `senha`) VALUES ('ana', 'anadu', '777');


CREATE TABLE IF NOT EXISTS usuarios (
    nome VARCHAR(100) DEFAULT "ANONIMO",
    usuario VARCHAR(100) NOT NULL PRIMARY KEY,
    senha VARCHAR(255) NOT NULL
);





CREATE TABLE IF NOT EXISTS itens_do_carrinho (
	cod_item_carrinho int auto_increment primary key,
    cod_carrinho int,
    cod_produto int,
    quantidade int default 1,
    constraint fk_itenscarrinho_carrinhos FOREIGN KEY (cod_carrinho) references carrinhos (cod_carrinho),
    constraint fk_itens_carrinho_itens foreign key (cod_produto) REFERENCES itens(codigo)
   );

CREATE TABLE IF NOT EXISTS carrinhos (
	cod_carrinho int auto_increment primary key,
    usuario varchar(50),
    data datetime default current_timestamp,
    finalizado bool,
    CONSTRAINT fk_carrinho_usuario FOREIGN KEY (usuario) REFERENCES usuarios(usuario)
    );

