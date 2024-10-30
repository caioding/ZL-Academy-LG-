class IMC:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura

    def calculo_imc(self):
        imc = self.peso / (self.altura * self.altura)
        return imc

    def classificacao(self):
        imc = self.calculo_imc()
        if imc < 18.5:
            return "Magreza"
        elif imc < 24.9:
            return "Normal"
        elif imc < 29.9:
            return "Sobrepeso"
        else:
            return "Obesidade"
    
def main():
    peso = float(input("Insira seu peso: "))
    altura = float(input("Insira sua altura: "))
    imc = IMC(peso, altura)
    print("Seu IMC é:", imc.calculo_imc())
    print("Sua classificação é:", imc.classificacao())

if __name__ == "__main__":
    main()