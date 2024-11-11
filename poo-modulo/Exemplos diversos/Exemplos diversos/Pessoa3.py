class Pessoa3:
    def __init__(self, nome, idade):
        # Atributos privados
        self.__nome = nome
        self.__idade = idade

    # Getter para o nome
    def get_nome(self):
        return self.__nome

    # Setter para o nome
    def set_nome(self, nome):
        self.__nome = nome

    # Getter para a idade
    def get_idade(self):
        return self.__idade

    # Setter para a idade
    def set_idade(self, idade):
        if idade >= 0:  # Exemplo de validação
            self.__idade = idade
        else:
            print("Idade inválida. Deve ser maior ou igual a 0.")

    # Método para exibir as informações da pessoa
    def mostrar_info(self):
        print(f'Nome: {self.__nome}, Idade: {self.__idade}')


# Exemplo de uso da classe
pessoa = Pessoa3("João", 30)

# Acessando atributos através dos getters
print(pessoa.get_nome())  # Saída: João
print(pessoa.get_idade())  # Saída: 30

# Modificando os atributos através dos setters
pessoa.set_nome("Maria")
pessoa.set_idade(25)

# Exibindo as novas informações
pessoa.mostrar_info()  # Saída: Nome: Maria, Idade: 25

# Tentando definir uma idade inválida
pessoa.set_idade(-5)  # Saída: Idade inválida. Deve ser maior ou igual a 0.
