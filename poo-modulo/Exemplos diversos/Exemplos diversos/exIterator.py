class Contador:
    def __init__(self, limite):
        self.limite = limite
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.limite:
            resultado = self.n
            self.n += 1
            return resultado
        else:
            raise StopIteration

contador = Contador(5)
for numero in contador:
    print(numero)
