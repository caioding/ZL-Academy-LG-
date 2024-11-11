class CalculadoraIMC:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura
        self.imc = 0.0

    def calcular_imc(self):
        self.imc = self.peso / (self.altura ** 2)
        return self.imc

    def classificar_imc(self):
        if self.imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= self.imc < 24.9:
            return "Peso normal"
        elif 25 <= self.imc < 29.9:
            return "Sobrepeso"
        else:
            return "Obesidade"

# Solicitando os dados do usuário
peso = float(input("Digite seu peso em quilogramas: "))
altura = float(input("Digite sua altura em metros: "))

# Criando um objeto da classe CalculadoraIMC
calculadora = CalculadoraIMC(peso, altura)

# Calculando o IMC
imc = calculadora.calcular_imc()

# Classificando o IMC
faixa = calculadora.classificar_imc()

# Exibindo o resultado
print(f"Seu IMC é: {imc:.2f}")
print(f"Faixa de peso: {faixa}")
