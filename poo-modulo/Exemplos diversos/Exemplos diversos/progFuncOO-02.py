def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Executando {func.__name__} com argumentos {args[1:]}")
        resultado = func(*args, **kwargs)
        print(f"Resultado de {func.__name__}: {resultado}")
        return resultado
    return wrapper

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    @log_decorator
    def depositar(self, valor):
        self.saldo += valor
        return self.saldo

    @log_decorator
    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente!")
            return self.saldo
        self.saldo -= valor
        return self.saldo

# Exemplo de uso
conta = ContaBancaria("Alice", 1000)
conta.depositar(200)
conta.sacar(150)
