from flask import Flask

app = Flask(__name__)

@app.route("/ola")
def hello_world():
    return "Hello World"

@app.route("/soma")
def soma_um_mais_um():
    soma = 1+1
    return str(soma)

@app.route("/pessoa")
def dados_pessoa():
    nome = "rafael"
    sobrenome = "cabral"
    idade = "18 anos"
    return [{
        'nome': nome,
        'sobrenome': sobrenome,
        'idade': "18 anos"
    },
    {
        'nome': "alan",
        'sobrenome': "Oliveira",
        'idade': "16 anos"
    }
    ]