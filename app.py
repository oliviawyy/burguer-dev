from flask import Flask, render_template
from model.produto import capturando_produtos, rec_destaque, recuperar_produto

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


@app.route("/login")
def login():
    return render_template("login.html")

if __name__=="__main__":
    app.run(debug=True)