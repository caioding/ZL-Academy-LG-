class Produto:
    def __init__(self, nome, preco, quantidade):
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade

    # Getter
    def get_nome(self):
        return self._nome

    # Setter
    def set_nome(self, novo_nome):
        self._nome = novo_nome

# Exemplo de uso
produto = Produto("Mesa", 250.00, 10)
print(produto.get_nome())  # Acessa o nome
produto.set_nome("Cadeira")  # Modifica o nome
print(produto.get_nome())
