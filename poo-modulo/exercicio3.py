class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def informacao(self):
        print(f"O veículo {self.marca} {self.modelo} foi criado.")

class Carro(Veiculo):
    def __init__(self, marca, modelo, num_portas):
        super().__init__(marca, modelo)
        self.num_porta = num_portas

    def informacao_completa(self):
        super().informacao()
        print(f"O veículo {self.marca} {self.modelo} tem {self.num_porta} portas.")

carro1 = Carro("Toyota", "Corolla", 4)
carro1.informacao_completa()