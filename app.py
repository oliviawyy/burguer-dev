from flask import Flask, render_template, session, redirect, request, jsonify
from model.carrinho import recuperar_carrinho
from model.produto import capturando_produtos, rec_destaque, recuperar_produto
from model.usuarios import Usuarios


app = Flask(__name__)
app.secret_key = "banana_verde"

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

@app.route("/login/usuario", methods=["POST"])
def logar_usuario():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")

    resultado = Usuarios.verificar_usuario(usuario, senha )

    if resultado:
        session["usuario_logado"] = resultado
        return redirect("/")
    
    return "Usuário ou senha invalidos", 401



@app.route("/api/get/carrinho", methods=["GET"])
def api_get_carrinho():
    if "usuario_logado" in session:
        login = session["usuario_logado"]["usuario"]
        carrinho = recuperar_carrinho (login)
        return jsonify(carrinho), 200
    else: 
        return jsonify({"message": "Usuário não logado"}), 401


@app.route("/login", methods=["GET"])
def pagina_login():
    return render_template("login.html")
    

if __name__=="__main__":
    app.run(debug=True)