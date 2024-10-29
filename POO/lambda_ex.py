# dobrar = lambda x: x * 2
# print(dobrar(5))
#
# pessoas = [('caio', 30), ('joao', 40), ('maria', 50)]
#
# pessoas_ordenadas = sorted(pessoas, key=lambda pessoa: pessoa[1])
# print(pessoas_ordenadas)
#
# pessoas_ordanadas = sorted(pessoas, key=lambda pessoa: pessoa[1])
# produtos = [
#     {"nome": "Camiseta", "preco": 50},
#     {"nome": "Calça Jeans", "preco": 100},
#     {"nome": "Tênis", "preco": 150},
# ]
#
# produtos_ordanados = sorted(produtos, key=lambda produto: produto["preco"])
# print(produtos_ordanados)
#
# numeros = [1, 2, 3, 4, 5]
# dobrados = list(map(lambda x: x * 2, numeros))
# print(dobrados)
#
# palavras = ["Python", "e", "incrivel"]
# palavras_longas = list(filter(lambda palavra: len(palavra) > 5, palavras))
# print(palavras_longas)
#
# def saudacao_dacorato(func):
#     def wrapper(nome):
#         print("Olá")
#         func(nome)
#         print("Tenha um bom dia")
#
#     return wrapper
#
# @saudacao_dacorato
# def saudacao(nome):
#     print(f"Prazer em conhecê-lo, {nome}")
#
# saudacao("Alice")

# def mul(n):
#     def decorator(func):
#         def wrapper(x):
#             return func(x) * n
#         return wrapper
#     return decorator
#
# @mul(3)
# def sum_two(x):
#     return x + 2
#
# print(sum_two(5))

# def odd_generator(limit):
#     n = 0
#     while n < limit:
#         yield n
#         n +=2
# for num in odd_generator(10):
#     print(num)

# class Cont:
#     def __init__(self, limit):
#         self.limit = limit
#         self.n = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.n < self.limit:
#             result = self.n
#             self.n += 1
#             return result
#         else:
#             raise StopIteration
# cont = Cont(5)
# for num in cont:
#     print(num)

# class IteratorName:
#     def __init__(self, names):
#         self.names = names
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.names):
#             name_list = self.names[self.index].upper()
#             self.index += 1
#             return name_list
#         else:
#             raise StopIteration
#
# names_list = ["alice", "bob", "charlie"]
# for name in IteratorName(names_list):
#     print(name)

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
conta.sacar(150)u
