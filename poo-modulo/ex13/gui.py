from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import messagebox

class Funcionario(ABC):
    def __init__(self, nome: str, matricula: int):
        self.__nome = nome
        self.__matricula = matricula

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, nova_matricula):
        self.__matricula = nova_matricula

    @abstractmethod
    def calcular_salario(self):
        pass


class Horista(Funcionario):
    def __init__(self, nome: str, matricula: int, horas_trabalhadas: float, valor_hora: float):
        super().__init__(nome, matricula)
        if horas_trabalhadas <= 0:
            raise ValueError("Horas trabalhadas devem ser positivas")
        if valor_hora <= 0:
            raise ValueError("Valor da hora deve ser positivo")
        self.__horas_trabalhadas = horas_trabalhadas
        self.__valor_hora = valor_hora

    @property
    def horas_trabalhadas(self):
        return self.__horas_trabalhadas

    @horas_trabalhadas.setter
    def horas_trabalhadas(self, nova_horas_trabalhadas):
        if nova_horas_trabalhadas <= 0:
            raise ValueError("Horas trabalhadas devem ser positivas")
        self.__horas_trabalhadas = nova_horas_trabalhadas

    @property
    def valor_hora(self):
        return self.__valor_hora

    @valor_hora.setter
    def valor_hora(self, novo_valor_hora):
        if novo_valor_hora <= 0:
            raise ValueError("Valor da hora deve ser positivo")
        self.__valor_hora = novo_valor_hora

    def calcular_salario(self):
        return self.__horas_trabalhadas * self.__valor_hora


class Mensalista(Funcionario):
    def __init__(self, nome: str, matricula: int, salario_mensal: float):
        super().__init__(nome, matricula)
        if salario_mensal <= 0:
            raise ValueError("Salário mensal deve ser positivo")
        self.__salario_mensal = salario_mensal

    @property
    def salario_mensal(self):
        return self.__salario_mensal

    @salario_mensal.setter
    def salario_mensal(self, novo_salario_mensal):
        if novo_salario_mensal <= 0:
            raise ValueError("Salário mensal deve ser positivo")
        self.__salario_mensal = novo_salario_mensal

    def calcular_salario(self):
        return self.__salario_mensal


class Comissionado(Funcionario):
    def __init__(self, nome: str, matricula: int, salario_base: float, vendas: float, taxa_comissao: float):
        super().__init__(nome, matricula)
        if salario_base < 0:
            raise ValueError("Salário base não pode ser negativo")
        if vendas < 0:
            raise ValueError("Vendas não podem ser negativas")
        if taxa_comissao < 0:
            raise ValueError("Taxa de comissão não pode ser negativa")
        
        self.__salario_base = salario_base
        self.__vendas = vendas
        self.__taxa_comissao = taxa_comissao

    @property
    def salario_base(self):
        return self.__salario_base

    @salario_base.setter
    def salario_base(self, novo_salario_base):
        if novo_salario_base < 0:
            raise ValueError("Salário base não pode ser negativo")
        self.__salario_base = novo_salario_base

    @property
    def vendas(self):
        return self.__vendas

    @vendas.setter
    def vendas(self, novas_vendas):
        if novas_vendas < 0:
            raise ValueError("Vendas não podem ser negativas")
        self.__vendas = novas_vendas

    @property
    def taxa_comissao(self):
        return self.__taxa_comissao 
    
    @taxa_comissao.setter
    def taxa_comissao(self, nova_taxa_comissao):
        if nova_taxa_comissao < 0:
            raise ValueError("Taxa de comissão não pode ser negativa")
        self.__taxa_comissao = nova_taxa_comissao
    
    def calcular_salario(self):
        return self.__salario_base + (self.__vendas * self.__taxa_comissao)


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
        self.option_tipo = tk.OptionMenu(self.frame_tipo, self.tipo_var, "Horista", "Mensalista", "Comissionado", command=self.alterar_campos)
        self.option_tipo.pack(side=tk.LEFT)

        # Frame para as informações adicionais
        self.frame_info_adicional = tk.Frame(self)
        self.frame_info_adicional.pack(padx=10, pady=10)

        # Campos adicionais para Horista e Comissionado
        self.label_horas_trabalhadas = tk.Label(self.frame_info_adicional, text="Horas Trabalhadas:")
        self.entry_horas_trabalhadas = tk.Entry(self.frame_info_adicional)

        self.label_vendas = tk.Label(self.frame_info_adicional, text="Vendas:")
        self.entry_vendas = tk.Entry(self.frame_info_adicional)

        self.label_taxa_comissao = tk.Label(self.frame_info_adicional, text="Taxa de Comissão:")
        self.entry_taxa_comissao = tk.Entry(self.frame_info_adicional)

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

        # Inicializa os campos de entrada de acordo com o tipo de funcionário
        self.alterar_campos()

    def alterar_campos(self, *args):
        """Exibe ou oculta campos adicionais com base no tipo de funcionário selecionado."""
        tipo = self.tipo_var.get()
        
        # Limpa o frame de informações adicionais
        for widget in self.frame_info_adicional.winfo_children():
            widget.pack_forget()

        if tipo == "Horista":
            self.label_horas_trabalhadas.pack(side=tk.LEFT)
            self.entry_horas_trabalhadas.pack(side=tk.LEFT)
            self.label_salario.config(text="Valor por Hora:")
        elif tipo == "Mensalista":
            self.label_salario.config(text="Salário Mensal:")
        elif tipo == "Comissionado":
            self.label_vendas.pack(side=tk.LEFT)
            self.entry_vendas.pack(side=tk.LEFT)
            self.label_taxa_comissao.pack(side=tk.LEFT)
            self.entry_taxa_comissao.pack(side=tk.LEFT)
            self.label_salario.config(text="Salário Base:")

    def cadastrar_funcionario(self):
        """Cadastra um funcionário baseado nas informações fornecidas."""
        nome = self.entry_nome.get()
        matricula = int(self.entry_matricula.get())
        salario = float(self.entry_salario.get())
        
        tipo = self.tipo_var.get()

        try:
            if tipo == "Horista":
                horas_trabalhadas = float(self.entry_horas_trabalhadas.get())
                funcionario = Horista(nome, matricula, horas_trabalhadas, salario)
            elif tipo == "Mensalista":
                funcionario = Mensalista(nome, matricula, salario)
            elif tipo == "Comissionado":
                vendas = float(self.entry_vendas.get())
                taxa_comissao = float(self.entry_taxa_comissao.get())
                funcionario = Comissionado(nome, matricula, salario, vendas, taxa_comissao)
            else:
                raise ValueError("Tipo de funcionário não reconhecido.")

            self.funcionarios.append(funcionario)
            messagebox.showinfo("Sucesso", f"{tipo} cadastrado com sucesso!")

            # Limpar os campos após o cadastro
            self.limpar_campos()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def listar_funcionarios(self):
        """Lista todos os funcionários cadastrados."""
        self.text_lista.delete(1.0, tk.END)
        if not self.funcionarios:
            self.text_lista.insert(tk.END, "Nenhum funcionário cadastrado.")
            return

        for func in self.funcionarios:
            self.text_lista.insert(tk.END, f"Nome: {func.nome}, Matrícula: {func.matricula}, Salário: {func.calcular_salario()}\n")

    def limpar_campos(self):
        """Limpa os campos de entrada."""
        self.entry_nome.delete(0, tk.END)
        self.entry_matricula.delete(0, tk.END)
        self.entry_salario.delete(0, tk.END)
        self.entry_horas_trabalhadas.delete(0, tk.END)
        self.entry_vendas.delete(0, tk.END)
        self.entry_taxa_comissao.delete(0, tk.END)

if __name__ == "__main__":
    app = App()
    app.mainloop()