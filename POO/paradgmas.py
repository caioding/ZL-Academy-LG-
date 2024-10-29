from functools import reduce

class Venda:
    def __init__(self, nome_produto, quantidade, preco_unitario):
        self.nome_produto = nome_produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

class HistoricoVendas:
    def __init__(self):
        self.vendas = []

    def adicionar_venda(self, venda):
        self.vendas.append(venda)

    def total_por_produto(self):
        return reduce(lambda acumulador, venda: {
            **acumulador,
            venda.nome_produto: acumulador.get(venda.nome_produto, 0) + venda.quantidade * venda.preco_unitario
        }, self.vendas, {})

    def listar_vendas_acima_de(self, valor):
        for venda in self.vendas:
            if venda.quantidade * venda.preco_unitario > valor:
                yield venda

class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

class SistemaRH:
    def __init__(self):
        self.funcionarios = []
        self.usuario_logado = None

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def autenticar_acesso(func):
        def wrapper(self, *args, **kwargs):
            if self.usuario_logado and self.usuario_logado.cargo == "Gerente":
                return func(self, *args, **kwargs)
            else:
                raise Exception("Acesso negado. Somente gerentes podem aumentar salários.")
        return wrapper

    @autenticar_acesso
    def aumentar_salario(self, nome_funcionario, aumento):
        for funcionario in self.funcionarios:
            if funcionario.nome == nome_funcionario:
                funcionario.salario += aumento
                print(f"Salário de {nome_funcionario} aumentado para {funcionario.salario}")
                return
        print(f"Funcionário {nome_funcionario} não encontrado")

class Transacao:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

class Conta:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def filtrar_transacoes_por_tipo(self, tipo):
        return list(filter(lambda transacao: transacao.tipo == tipo, self.transacoes))

    def aplicar_taxa(self, taxa):
        saques = self.filtrar_transacoes_por_tipo("Saque")
        saques_com_taxa = list(map(lambda saque: Transacao(saque.tipo, saque.valor - (saque.valor * taxa)), saques))
        self.transacoes = [transacao for transacao in self.transacoes if transacao.tipo != "Saque"] + saques_com_taxa

def main():
    # Testando a classe Venda
    venda1 = Venda("Produto 1", 2, 10.0)
    venda2 = Venda("Produto 2", 3, 20.0)

    print(f"Nome do produto: {venda1.nome_produto}")
    print(f"Quantidade: {venda1.quantidade}")
    print(f"Preço unitário: {venda1.preco_unitario}")

    # Testando a classe HistoricoVendas
    historico_vendas = HistoricoVendas()
    historico_vendas.adicionar_venda(venda1)
    historico_vendas.adicionar_venda(venda2)

    print("Total por produto:")
    total_por_produto = historico_vendas.total_por_produto()
    for produto, total in total_por_produto.items():
        print(f"{produto}: {total}")

    print("Vendas acima de 30:")
    vendas_acima_de_30 = historico_vendas.listar_vendas_acima_de(30)
    for venda in vendas_acima_de_30:
        print(f"Nome do produto: {venda.nome_produto}")
        print(f"Quantidade: {venda.quantidade}")
        print(f"Preço unitário: {venda.preco_unitario}")

    # Testando a classe Funcionario
    funcionario1 = Funcionario("João", "Gerente", 1000.0)
    funcionario2 = Funcionario("Maria", "Analista", 700.0)

    print(f"Nome: {funcionario1.nome}")
    print(f"Cargo: {funcionario1.cargo}")
    print(f"Salário: {funcionario1.salario}")

    # Testando a classe SistemaRH
    sistema_rh = SistemaRH()
    sistema_rh.adicionar_funcionario(funcionario1)
    sistema_rh.adicionar_funcionario(funcionario2)

    sistema_rh.usuario_logado = funcionario1
    sistema_rh.aumentar_salario("João", 100.0)

    # Testando a classe Transacao
    transacao1 = Transacao("Depósito", 100.0)
    transacao2 = Transacao("Saque", 50.0)

    print(f"Tipo: {transacao1.tipo}")
    print(f"Valor: {transacao1.valor}")

    # Testando a classe Conta
    conta = Conta()
    conta.adicionar_transacao(transacao1)
    conta.adicionar_transacao(transacao2)

    print("Transações:")
    for transacao in conta.transacoes:
        print(f"Tipo: {transacao.tipo}")
        print(f"Valor: {transacao.valor}")

    conta.aplicar_taxa(0.1)
    print("Transações após aplicar taxa:")
    for transacao in conta.transacoes:
        print(f"Tipo: {transacao.tipo}")
        print(f"Valor: {transacao.valor}")

if __name__ == "__main__":
    main()
    