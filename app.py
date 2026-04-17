from flask import Flask, render_template, session, redirect, request
from model.produto import capturando_produtos, rec_destaque, recuperar_produto
from model.usuarios import Usuarios

app = Flask(__name__)

@app.route("/")
def pagina_principal():
    produtos = capturando_produtos()
    destaques = rec_destaque()
    return render_template("index.html", produtos = produtos, destaques = destaques)

# @app.route("/layout")
# def layout():
#     return render_template("layout.html")

@app.route("/pagina2/<int:codigo>")
def pagina_pagina2(codigo):
    produto = recuperar_produto(codigo)  #recuperar produto com código 
    return render_template("pagina2.html", produto = produto)


# @app.route("/login", methods=["POST"])
# def login():
#     session["nome"]= "olivia"
#     return redirect("/")

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    nome = request.form.get ("nome")


    novo_usuario = Usuarios(usuario, senha, nome)
    novo_usuario.cadastrar()

    return redirect("/")

@app.route("/login", methods=["GET"])
def pagina_login():
    return render_template("login.html")
    

if __name__=="__main__":
    app.run(debug=True)