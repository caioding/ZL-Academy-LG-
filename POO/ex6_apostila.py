class Pagamento:
    def processar_pagamento(self:int):
        pass

class PagamentoCartaoCredito(Pagamento):
    def __init__(self, numero_cartao: int):
        self.numero_cartao = numero_cartao

    def processar_pagamento(self: int):
        print(f"Pagamentdo do cartão de credito processado pelo cartão {self.numero_cartao}")
        return super().processar_pagamento()
    
class PagamentoBoleto(Pagamento):
    def __init__(self, codigo_boleto: int):
        self.codigo_boleto = codigo_boleto
    
    def processar_pagamento(self: int):
        print(f"Pagamento do boleto processado no código {self.codigo_boleto}")
        return super().processar_pagamento()

class PagamentoPix(Pagamento):
    def __init__(self, chave_pix: int):
        self.chave_pix = chave_pix

    def processar_pagamento(self: int):
        print(f"Pagamento do pix processado na chave {self.chave_pix}")
        return super().processar_pagamento()

def processar(pagamento: Pagamento):
        return pagamento.processar_pagamento()

def main():
    cartao_credito = PagamentoCartaoCredito(4532015112830361)
    boleto = PagamentoBoleto(12345678901234567890)
    pix = PagamentoPix("12345678901234567890123456789012")

    processar(cartao_credito)
    processar(boleto)
    processar(pix)

if __name__ == "__main__":
    main()
