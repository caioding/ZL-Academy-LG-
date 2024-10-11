# • Classe Pessoa: Crie uma classe que modele uma
# pessoa:
# • Atributos: nome, idade, peso e altura
# • Métodos: Envelhecer, engordar, emagrecer,
# crescer.
# • Obs: Por padrão, a cada ano que nossa pessoa
# envelhece, sendo a idade dela menor que 21 anos,
# ela deve crescer 0,5 cm
# • Pode possuir ou não parâmetros.

class Pessoa:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def envelhecer(self):
        if self.age < 21:
            self.crescer()
    
    def crescer(self):
        self.height += 0.05

    def emagrecer(self):
        self.weight -= 0.05
    
    def engordar(self):
        self.weight += 00.5

def main():
    Pessoa1 = Pessoa("João", 20, 70, 1.75)
    print(Pessoa1.name)
    print(Pessoa1.age)
    print(Pessoa1.weight)
    print(Pessoa1.height)    

    Pessoa1.envelhecer()
    print(Pessoa1.height)
    Pessoa1.engordar()
    print(Pessoa1.weight)
    Pessoa1.emagrecer()
    print(Pessoa1.weight)

if __name__ == "__main__":
    main()