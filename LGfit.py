clients = [

]

def menu():
    print("\n\n--- Menu ---")
    print('1 - Matricular cliente')
    print('2 - Encerrar programa')

def clients_data():
    file_path = r'C:\Users\noturno\Desktop\Caio\registro_clientes.txt'

    try:
        file = open(file_path, 'w')
        for client in clients:
            file.write(f"Nome: {client['nome']}\n")
            file.write(f"Idade: '{client['idade']}\n")
            file.write(f"Peso: '{client['peso']}\n")
            file.write(f"Altura: '{client['altura']}\n")
            file.write(f"Sexo: '{client['sexo']}\n")
            file.write("\n")

def client_inputs():
    global clients
    name = input('Digite seu nome: ')
    age = int(input('Digite sua idade: '))
    weight = float(input('Digite seu peso'))
    height = float(input('Digite sua altura'))
    sex = str('Informe seu sexo: M (masculino) ou F(feminino): ')

    new_client =  {
        'nome': name,
        'idade': age,
        'peso': weight,
        'altura': height,
        'sexo': sex
    }

    clients.append(new_client)
    print(f'\nCliente {name} matriculado com seucesso!')
