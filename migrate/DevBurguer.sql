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
values("Godo Burguer", "Um lanche especial espera por voce com uma carne divina", 24.00, 1, "https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg?auto=compress&cs=tinysrgb&w=200", 1)