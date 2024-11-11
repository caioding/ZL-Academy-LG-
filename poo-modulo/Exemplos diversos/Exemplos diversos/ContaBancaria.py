class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # Variável privada

    def depositar(self, quantia):
        self.__saldo += quantia

    def sacar(self, quantia):
        if self.__saldo >= quantia:
            self.__saldo -= quantia
        else:
            print("Saldo insuficiente")

    def mostrar_saldo(self):
        return self.__saldo

conta = ContaBancaria(100)
conta.depositar(50)

print(conta.mostrar_saldo())  # Acessando via método

# Tentar acessar a variável diretamente resulta em um erro:
# print(conta.__saldo)  # AttributeError: 'ContaBancaria' object has no attribute '__saldo'

# Mas podemos acessar indiretamente via name mangling
print(conta._ContaBancaria__saldo)  # Acessando a variável privada usando name mangling
