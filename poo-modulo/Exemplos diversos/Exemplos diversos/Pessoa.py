class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        for _ in range(anos):
            if self.idade < 21:
                self.crescer(0.5)
            self.idade += 1

    def engordar(self, quilos):
        self.peso += quilos

    def emagrecer(self, quilos):
        self.peso -= quilos

    def crescer(self, centimetros):
        self.altura += centimetros / 100  # Convertendo para metros

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Peso: {self.peso} kg")
        print(f"Altura: {self.altura:.2f} m")

# Código principal
if __name__ == "__main__":
    # Exemplo de uso
    pessoa = Pessoa("João", 18, 70, 1.75)
    
    # Envelhecer a pessoa em 3 anos e verificar o crescimento
    pessoa.envelhecer(3)
    pessoa.engordar(5)
    pessoa.emagrecer(2)
    
    # Mostrar as informações da pessoa
    pessoa.mostrar_informacoes()
