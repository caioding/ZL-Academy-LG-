class Pessoa2:
    def __init__(self, nome, idade):
        self.__nome = nome  # Atributo privado
        self.__idade = idade  # Atributo privado

    # Getter para nome
    def get_nome(self):
        return self.__nome

    # Setter para nome
    def set_nome(self, novo_nome):
        if isinstance(novo_nome, str) and len(novo_nome) > 0:
            self.__nome = novo_nome
        else:
            print("Nome inválido")

    # Getter para idade
    def get_idade(self):
        return self.__idade

    # Setter para idade
    def set_idade(self, nova_idade):
        if nova_idade > 0:
            self.__idade = nova_idade
        else:
            print("Idade inválida")

# Exemplo de uso:
pessoa = Pessoa2("João", 30)

# Usando getters
print(pessoa.get_nome())  # Saída: João

# Usando setters
pessoa.set_nome("Maria")
print(pessoa.get_nome())  # Saída: Maria

