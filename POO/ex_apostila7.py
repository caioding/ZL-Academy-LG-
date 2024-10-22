from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processar_pagamento(self):
        pass

    def detalhes_pagamento(self, metodo):
        print(f"Processando pagamento via {metodo}")


class PagamentoCartao(Pagamento):
    def __init__(self, numero_cartao: int):
        self.numero_cartao = numero_cartao

    def processar_pagamento(self):
        print(f"Pagamento processado com cartão {self.numero_cartao}")
        self.detalhes_pagamento("cartão")


class PagamentoBoleto(Pagamento):
    def __init__(self, codigo_boleto: int):
        self.codigo_boleto = codigo_boleto

    def processar_pagamento(self):
        print(f"Pagamento processado com boleto {self.codigo_boleto}")
        self.detalhes_pagamento("boleto")


def testar_pagamentos():
    cartao = PagamentoCartao(4532015112830361)
    boleto = PagamentoBoleto(12345678901234567890)

    cartao.processar_pagamento()
    boleto.processar_pagamento()


if __name__ == "__main__":
    testar_pagamentos()