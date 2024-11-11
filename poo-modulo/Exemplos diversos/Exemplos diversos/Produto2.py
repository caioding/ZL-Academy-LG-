class Produto2:
    def __init__(self, nome, preco, quantidade):
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade

    # Getter com @property
    @property
    def nome(self):
        return self._nome

    # Setter com @nome.setter
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

# Exemplo de uso
produto = Produto2("Mesa", 250.00, 10)
print(produto.nome)  # Acessa o nome diretamente
produto.nome = "Cadeira"  # Modifica o nome diretamente
print(produto.nome)
