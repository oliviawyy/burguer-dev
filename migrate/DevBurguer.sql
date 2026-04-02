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

insert into produto(produto, descricao, preco, destaque, foto, disponibilidade)
values("Godo Burguer", "Um lanche especial espera por voce com uma carne divina", 24.00, 1, "https://assets.grok.com/users/6c51eb9c-5b1a-4715-b68c-9f325c88541d/generated/82bc4c98-4a2d-4e4f-b243-0fcce9c83917/image.jpg", 1)