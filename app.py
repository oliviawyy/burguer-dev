from flask import Flask, render_template
from model.produto import capturando_produtos

app = Flask(__name__)

@app.route("/")
def pagina_principal():
    produtos = capturando_produtos()
    return render_template("index.html", produtos = produtos)

# @app.route("/layout")
# def layout():
#     return render_template("layout.html")

@app.route("/pagina2")
def pagina_pagina2():
    return render_template("pagina2.html")



if __name__=="__main__":
    app.run(debug=True)