import tkinter as tk
from tkinter import messagebox

class Funcionario:
    def __init__(self, nome, matricula, salario):
        self.nome = nome
        self.matricula = matricula
        self.salario = salario

class Horista(Funcionario):
    def __init__(self, nome, matricula, salario, horas_trabalhadas):
        super().__init__(nome, matricula, salario)
        self.horas_trabalhadas = horas_trabalhadas

    def calcular_salario(self):
        return self.salario * self.horas_trabalhadas

class Mensalista(Funcionario):
    def __init__(self, nome, matricula, salario):
        super().__init__(nome, matricula, salario)

    def calcular_salario(self):
        return self.salario

class Comissionado(Funcionario):
    def __init__(self, nome, matricula, salario, vendas):
        super().__init__(nome, matricula, salario)
        self.vendas = vendas

    def calcular_salario(self):
        return self.salario + (self.vendas * 0.1)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cadastro de Funcionários")
        self.geometry("800x600")
        self.resizable(True, True)

        self.funcionarios = []

        # Frame para os campos de entrada
        self.frame_entrada = tk.Frame(self)
        self.frame_entrada.pack(padx=10, pady=10)

        # Campos de entrada
        self.label_nome = tk.Label(self.frame_entrada, text="Nome:")
        self.label_nome.grid(row=0, column=0)
        self.entry_nome = tk.Entry(self.frame_entrada)
        self.entry_nome.grid(row=0, column=1)

        self.label_matricula = tk.Label(self.frame_entrada, text="Matrícula:")
        self.label_matricula.grid(row=1, column=0)
        self.entry_matricula = tk.Entry(self.frame_entrada)
        self.entry_matricula.grid(row=1, column=1)

        self.label_salario = tk.Label(self.frame_entrada, text="Salário:")
        self.label_salario.grid(row=2, column=0)
        self.entry_salario = tk.Entry(self.frame_entrada)
        self.entry_salario.grid(row=2, column=1)

        # Frame para o tipo de funcionário
        self.frame_tipo = tk.Frame(self)
        self.frame_tipo.pack(padx=10, pady=10)

        # Campo de seleção do tipo de funcionário
        self.label_tipo = tk.Label(self.frame_tipo, text="Tipo de Funcionário:")
        self.label_tipo.pack(side=tk.LEFT)
        self.tipo_var = tk.StringVar()
        self.tipo_var.set("Horista")
        self.option_tipo = tk.OptionMenu(self.frame_tipo, self.tipo_var, "Horista", "Mensalista", "Comissionado")
        self.option_tipo.pack(side=tk.LEFT)

        # Frame para as informações adicionais
        self.frame_info_adicional = tk.Frame(self)
        self.frame_info_adicional.pack(padx=10, pady=10)

        # Campos adicionais para Horista e Comissionado
        self.label_horas_trabalhadas = tk.Label(self.frame_info_adicional, text="Horas Trabalhadas:")
        self.label_horas_trabalhadas.pack(side=tk.LEFT)
        self.entry_horas_trabalhadas = tk.Entry(self.frame_info_adicional)
        self.entry_horas_trabalhadas.pack(side=tk.LEFT)

        self.label_vendas = tk.Label(self.frame_info_adicional, text="Vendas:")
        self.label_vendas.pack(side=tk.LEFT)
        self.entry_vendas = tk.Entry(self.frame_info_adicional)
        self.entry_vendas.pack(side=tk.LEFT)

        # Frame para os botões
        self.frame_botoes = tk.Frame(self)
        self.frame_botoes.pack(padx=10, pady=10)

        # Botões
        self.botao_cadastrar = tk.Button(self.frame_botoes, text="Cadastrar", command=self.cadastrar_funcionario)
        self.botao_cadastrar.pack(side=tk.LEFT, padx=5)

        self.botao_listar = tk.Button(self.frame_botoes, text="Listar Funcionários", command=self.listar_funcionarios)
        self.botao_listar.pack(side=tk.LEFT, padx=5)

        # Text widget para exibir a lista de funcionários
        self.text_lista = tk.Text(self, height=10, width=100)
        self.text_lista.pack(padx=10, pady=10)

    def cadastrar_funcionario(self):
        nome = self.entry_nome.get()
        matricula = self.entry_matricula.get()
        salario = float(self.entry_salario.get())

        tipo = self.tipo_var.get()

        if tipo == "Horista":
            horas_trabalhadas = float(self.entry_horas_trabalhadas.get())
            funcionario = Horista(nome, matricula, salario, horas_trabalhadas)
        elif tipo == "Mensalista":
            funcionario = Mensalista(nome, matricula, salario)
        elif tipo == "Comissionado":
            vendas = float(self.entry_vendas.get())
            funcionario = Comissionado(nome, matricula, salario, vendas)

        self.funcionarios.append(funcionario)
        messagebox.showinfo("Sucesso", f"Funcionário {nome} cadastrado com sucesso!")
        self.limpar_campos()

    def listar_funcionarios(self):
        # Limpa o conteúdo atual do Text widget
        self.text_lista.delete(1.0, tk.END)
        
        if not self.funcionarios:
            self.text_lista.insert(tk.END, "Nenhum funcionário cadastrado.\n")
        else:
            for func in self.funcionarios:
                salario = func.calcular_salario()
                self.text_lista.insert(tk.END, f"Nome: {func.nome}, Matrícula: {func.matricula}, Salário: R$ {salario:.2f}\n")

    def limpar_campos(self):
        """Função auxiliar para limpar os campos após o cadastro"""
        self.entry_nome.delete(0, tk.END)
        self.entry_matricula.delete(0, tk.END)
        self.entry_salario.delete(0, tk.END)
        self.entry_horas_trabalhadas.delete(0, tk.END)
        self.entry_vendas.delete(0, tk.END)

if __name__ == "__main__":
    app = App()
    app.mainloop()
