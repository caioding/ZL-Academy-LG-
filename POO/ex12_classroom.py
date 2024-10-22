from abc import ABC, abstractmethod
import datetime
import calendar

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
    def __init__(self, nome, matricula, horas_trabalhadas: float, valor_hora: float):
        super().__init__(nome, matricula)
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
    def __init__(self, nome, matricula, salario_mensal: float):
        super().__init__(nome, matricula)
        self.__salario_mensal = salario_mensal

    @property
    def salario_mensal(self):
        return self.__salario_mensal

    @salario_mensal.setter
    def salario_mensal(self, novo_salario_mensal):
        self.__salario_mensal = novo_salario_mensal

    def calcular_salario(self):
        return self.__salario_mensal

class Comissionado(Funcionario):
    def __init__(self, nome, matricula, salario_base: float, vendas: float, taxa_comissao: float):
        super().__init__(nome, matricula)
        self.__salario_base = salario_base
        self.__vendas = vendas
        self.__taxa_comissao = taxa_comissao

    @property
    def salario_base(self):
        return self.__salario_base

    @salario_base.setter
    def salario_base(self, novo_salario_base):
        self.__salario_base = novo_salario_base

    @property
    def vendas(self):
        return self.__vendas

    @vendas.setter
    def vendas(self, novas_vendas):
        self.__vendas = novas_vendas

    @property
    def taxa_comissao(self):
        return self.__taxa_comissao 
    
    @taxa_comissao.setter
    def taxa_comissao(self, nova_taxa_comissao):
        self.__taxa_comissao = nova_taxa_comissao
    
    def calcular_salario(self):
        return self.__salario_base + (self.__vendas * self.__taxa_comissao)
    
class FuncionarioPorProjeto(Funcionario):
    def __init__(self, nome, matricula, valor_por_projeto: float):
        super().__init__(nome, matricula)
        self.__valor_por_projeto = valor_por_projeto
        self.__projetos_realizados = 0

    @property
    def valor_por_projeto(self):
        return self.__valor_por_projeto

    @valor_por_projeto.setter
    def valor_por_projeto(self, novo_valor_por_projeto):
        self.__valor_por_projeto = novo_valor_por_projeto

    def adicionar_projeto(self):
        self.__projetos_realizados += 1

    def calcular_salario(self):
        return self.__projetos_realizados * self.__valor_por_projeto

def processar_pagamento(funcionario: Funcionario):
    print(f"Nome do funcionário: {funcionario.nome}")
    print(f"Salário: {funcionario.calcular_salario()}")

def simular_mes_de_pagamentos(funcionario: Horista, mes, ano):
    salario_total = 0
    dias_uteis = 0
    feriados = [datetime.date(ano, mes, 1), datetime.date(ano, mes, 15)]  # exemplo de feriados

    for dia in range(1, calendar.monthrange(ano, mes)[1] + 1):
        data = datetime.date(ano, mes, dia)
        if data.weekday() < 5 and data not in feriados:  # se não é fim de semana e não é feriado
            dias_uteis += 1
            salario_total += funcionario.calcular_salario() / dias_uteis

    return salario_total

def main():
    # Criando funcionários
    horista = Horista("João", 1234, 200, 10)
    mensalista = Mensalista("Maria", 5678, 2000)
    comissionado = Comissionado("Pedro", 9012, 1500, 5000, 0.1)
    horista2 = Horista("Luiz", 1111, 250, 12)
    mensalista2 = Mensalista("Ana", 2222, 2500)
    comissionado2 = Comissionado("Carlos", 3333, 1800, 6000, 0.12)
    funcionario_por_projeto = FuncionarioPorProjeto("Caio", 1234, 1000.0)

    # Adicionando funcionários a uma lista
    funcionarios = [
        horista,
        mensalista,
        comissionado,
        horista2,
        mensalista2,
        comissionado2,
        funcionario_por_projeto
    ]

    # Adicionando projetos
    funcionario_por_projeto.adicionar_projeto()
    funcionario_por_projeto.adicionar_projeto()

    # Processando pagamentos
    for funcionario in funcionarios:
        processar_pagamento(funcionario)

    # Simulando mês de pagamentos para funcionários horistas
    print("Simulando mês de pagamentos para funcionários horistas:")
    salario_total_horista = simular_mes_de_pagamentos(horista, 1, 2023)
    salario_total_horista2 = simular_mes_de_pagamentos(horista2, 1, 2023)
    print(f"Salário total do funcionário {horista.nome}: {salario_total_horista}")
    print(f"Salário total do funcionário {horista2.nome}: {salario_total_horista2}")


if __name__ == "__main__":
    main() 