class IteradorDeNomes:
    def __init__(self, nomes):
        self.nomes = nomes
        self.indice = 0

    def __iter__(self):
        # Retorna o próprio objeto como iterador
        return self

    def __next__(self):
        # Retorna o próximo nome em maiúsculas, se disponível
        if self.indice < len(self.nomes):
            nome = self.nomes[self.indice].upper()
            self.indice += 1
            return nome
        else:
            # Levanta StopIteration ao final da lista
            raise StopIteration

# Usando o iterador personalizado
nomes = ["alice", "bob", "charlie"]
for nome in IteradorDeNomes(nomes):
    print(nome)
