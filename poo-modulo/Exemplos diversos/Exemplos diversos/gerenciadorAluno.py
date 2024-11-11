import json
import csv
import pickle

class Aluno:
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

class GerenciadorDeAlunos:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def salvar_json(self, nome_arquivo="alunos.json"):
        dados = [{"nome": aluno.nome, "idade": aluno.idade, "notas": aluno.notas} for aluno in self.alunos]
        with open(nome_arquivo, "w") as arquivo_json:
            json.dump(dados, arquivo_json)
        print(f"Dados salvos em {nome_arquivo}.")

    def carregar_json(self, nome_arquivo="alunos.json"):
        with open(nome_arquivo, "r") as arquivo_json:
            dados = json.load(arquivo_json)
            self.alunos = [Aluno(**aluno) for aluno in dados]
        print(f"Dados carregados de {nome_arquivo}.")

    def salvar_csv(self, nome_arquivo="alunos.csv"):
        with open(nome_arquivo, "w", newline="") as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow(["Nome", "Idade", "Notas"])
            for aluno in self.alunos:
                escritor.writerow([aluno.nome, aluno.idade, aluno.notas])
        print(f"Dados salvos em {nome_arquivo}.")

    def carregar_csv(self, nome_arquivo="alunos.csv"):
        with open(nome_arquivo, "r") as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            next(leitor)  # Pular cabeçalho
            self.alunos = [Aluno(linha[0], int(linha[1]), eval(linha[2])) for linha in leitor]
        print(f"Dados carregados de {nome_arquivo}.")

    def salvar_pickle(self, nome_arquivo="alunos.pkl"):
        with open(nome_arquivo, "wb") as arquivo:
            pickle.dump(self.alunos, arquivo)
        print(f"Dados salvos em {nome_arquivo}.")

    def carregar_pickle(self, nome_arquivo="alunos.pkl"):
        with open(nome_arquivo, "rb") as arquivo:
            self.alunos = pickle.load(arquivo)
        print(f"Dados carregados de {nome_arquivo}.")

    def listar_alunos(self):
        for aluno in self.alunos:
            print(f"Nome: {aluno.nome}, Idade: {aluno.idade}, Média: {aluno.calcular_media():.2f}")

# Criando instância do gerenciador e adicionando alunos
gerenciador = GerenciadorDeAlunos()
gerenciador.adicionar_aluno(Aluno("Alice", 20, [8, 7.5, 9]))
gerenciador.adicionar_aluno(Aluno("Bob", 22, [6, 5, 7]))

# Salvando e carregando dados em JSON
gerenciador.salvar_json()
gerenciador.carregar_json()
gerenciador.listar_alunos()

# Salvando e carregando dados em CSV
gerenciador.salvar_csv()
gerenciador.carregar_csv()
gerenciador.listar_alunos()

# Salvando e carregando dados com pickle
gerenciador.salvar_pickle()
gerenciador.carregar_pickle()
gerenciador.listar_alunos()
