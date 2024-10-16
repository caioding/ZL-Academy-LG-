class Produto:
    def __init__(self, nome, preco, quantidade):
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        if not value:
            raise ValueError("O nome não pode ser vazio.")
        self._nome = value

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, value):
        if value < 0:
            raise ValueError("O preço não pode ser negativo.")
        self._preco = value

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, value):
        if value < 0:
            raise ValueError("A quantidade não pode ser negativa.")
        self._quantidade = value

    def exibir(self):
        print(f'Nome: {self.nome}')
        print(f'Preço: {self.preco}')
        print(f'Quantidade: {self.quantidade}')
    
    def atualizar(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade