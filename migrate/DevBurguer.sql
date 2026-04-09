create database if not exists DevBurguer;
use DevBurguer

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
values("Godo Burguer", "Um lanche especial espera por voce com uma carne divina", 24.00, 1, "https://www.acidadeon.com/wp-content/uploads/sites/4/2023/11/Fest-Gourmet-1.jpeg", 1)