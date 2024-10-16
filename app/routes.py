from app import app
from flask import render_template
from flask import request
import requests
import json
link = "https://flasktintjonatas-default-rtdb.firebaseio.com/"

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',titulo="Página Inicial")

@app.route('/contato')
def contato():
    return render_template('contato.html',titulo="Contato")

@app.route('/usuario')
def usuario():
    requesicao = requests.get(f'{link}/usuario/.json')
    dicionario = requesicao.json()


    return render_template('usuario.html',titulo="Usuario" ,data="bancoDeDados")

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html',titulo="Cadastro")

@app.route('/atualizacao')
def atualizacao():
    return render_template('atualizacao.html',titulo="Atualização")

@app.route('/login')
def login():
    return render_template('login.html',titulo="Login")\

@app.route('/excluicao')
def excluicao():
    return render_template('excluicao.html',titulo="Excluição")


@app.route('/cadastrarUsuario', methods=['POST'])
def cadastrarUsuario():
    try:
        cpf        = request.form.get("cpf")
        nome       = request.form.get("nome")
        telefone   = request.form.get("telefone")
        endereco   = request.form.get("endereco")
        dados      = {"cpf": cpf, "nome": nome, "telefone": telefone, "endereco": endereco}
        requisicao = requests.post(f'{link}/usuario/.json', data=json.dumps(dados))
        return 'Cadastrado com sucesso!'
    except Exception as e:
        return f'Ocorreu um erro\n +{e}'

@app.route('/listar')
def listarTudo():
    try:
        requisicao = requests.get(f'{link}/usuario/.json')
        dicionario = requisicao.json()
        return dicionario

    except Exception as e:
        return f'Algo deu errado\n +{e}'

@app.route('/listarIndividual', methods=['POST'])
def listarIndividual():
    try:
        requesicao = requests.get(f'{link}/usuario/.json')
        dicionario = requesicao.json()

        procurar   = request.form.get("procurar")

        for codigo in dicionario:
            chave = dicionario[codigo]['nome']

            if chave == procurar:
                return f'Nome: {dicionario[codigo]["nome"]}\n<br>' \
                       f'CPF: {dicionario[codigo]["cpf"]}\n<br>' \
                       f'Telefone: {dicionario[codigo]["telefone"]}\n<br>' \
                       f'Endereco: {dicionario[codigo]["endereco"]}\n<br>'
    except Exception as e:
        return f'Algo deu errado\n {e}'

@app.route('/atualizar', methods=['POST'])
def atualizar():
    try:
        #request do banco de dados
        requesicao = requests.get(f'{link}/usuario/.json')
        dicionario = requesicao.json()

        #request do form
        cpf      = request.form.get("cpf")
        nome     = request.form.get("nome")
        email    = request.form.get("email")
        senha    = request.form.get("senha")
        telefone = request.form.get("telefone")
        endereco = request.form.get("endereco")
        dados    = {"cpf": cpf, "nome": nome, "telefone": telefone, "endereco": endereco}

        #procurar codigo
        for codigo in dicionario:
            chave = dicionario[codigo]['cpf']
            if chave == cpf:

                #atualizar dados
                requisicao = requests.patch(f'{link}/usuario/{codigo}/.json', data=json.dumps(dados))
                return "Atualizado com sucesso!"

    except Exception as e:
        return f'Algo deu errado\n {e}'

@app.route('/excluir', methods=['POST'])
def excluir():
    try:
        # request do banco de dados
        requesicao = requests.get(f'{link}/usuario/.json')
        dicionario = requesicao.json()
        cpf = request.form.get("cpf")

        # procurar codigo
        for codigo in dicionario:
            chave = dicionario[codigo]['cpf']
            if chave == cpf:

                # atualizar dados
                requisicao = requests.delete(f'{link}/usuario/{codigo}/.json')
                return "Excluido com sucesso!"

    except Exception as e:
        return f'Algo deu errado\n {e}'