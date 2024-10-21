from flask import Flask, render_template, request
from bot_test.bot import extrari_dados

app = Flask(__name__)

def ler_dados():
    with open('veiculos.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

    dados = []
    for linha in linhas:
        id, nome, ano, diaria, tipo, combustivel, cilindrada = linha.strip().split(',')
        dados.append({
            'id' : id,
            'nome' : nome,
            'ano' : ano,
            'diaria' : diaria,
            'tipo' : tipo,
            'combustivel' : combustivel,
            'cilindrada' : cilindrada
        })
    
    return dados

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/alugar_carro')
def alugar_carros():
    return render_template('carro.html')

@app.route('/alugar_moto')
def alugar_motos():
    return render_template('moto.html')

@app.route('/veiculos_alugados')
def listar_veiculos():
    dados = ler_dados()
    return render_template('veiculos.html', dados=dados)

@app.route('/alugar_carros/instanciar', methods=['POST'])
def alugar_carros_instanciar():
    nome = request.form['nome']
    ano = request.form['ano']
    diaria = request.form['diaria']
    combustivel = request.form['combustivel']

    carro = {
        'nome' : nome,
        'ano' : ano,
        'diaria' : diaria,
        'combustivel' : combustivel
    }

    extrari_dados(carro)
    return listar_veiculos()

@app.route('/alugar_motos/instanciar', methods=['POST'])
def alugar_motos_instanciar():
    nome = request.form['nome']
    ano = request.form['ano']
    diaria = request.form['diaria']
    cilindrada = request.form['cilindrada']

    moto = {
        'nome' : nome,
        'ano' : ano,
        'diaria' : diaria,
        'cilindrada' : cilindrada
    }
    
    extrari_dados(moto)
    return listar_veiculos()
    
if __name__ == '__main__':
    app.run()
