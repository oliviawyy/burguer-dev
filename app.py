from flask import Flask, render_template, session, redirect, request
from model.produto import capturando_produtos, rec_destaque, recuperar_produto
from model.usuarios import Usuarios
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

lista_produtos = [
                    {"codigo": 1,
                    "nome": "Hamburguer", 
                    "preco": 20.9, 
                    "foto": "https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg?auto=compress&cs=tinysrgb&w=200"
                    },
                    {"codigo": 2,
                    "nome": "Super Godofredo",
                    "preco": 50.00,
                    "foto": "https://www.sabornamesa.com.br/media/k2/items/cache/bf1e20a4462b71e3cc4cece2a8c96ac8_XL.jpg"
                    }

                ]

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

    if not resultado:
        session["nome"] = resultado["nome"]

    return redirect("/")


@app.route("/login", methods=["GET"])
def pagina_login():
    return render_template("login.html")
    

if __name__=="__main__":
    app.run(debug=True)