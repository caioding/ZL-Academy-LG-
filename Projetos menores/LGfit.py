clients = []

def menu():
    print("\n\n--- Menu ---")
    print('1 - Matricular cliente')
    print('2 - Encerrar programa')

def clients_data():
    file_path = r'C:\Users\noturno\Desktop\Caio\registro_clientes.txt'

    try:
        with open(file_path, 'a') as file:  # 'a' to append new clients
            for client in clients:
                file.write(f"Nome: {client['nome']}\n")
                file.write(f"Idade: {client['idade']}\n")
                file.write(f"Peso: {client['peso']}\n")
                file.write(f"Altura: {client['altura']}\n")
                file.write(f"Sexo: {client['sexo']}\n")
                file.write("\n")
        print("\nDados dos clientes registrados com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

def client_inputs():
    global clients
    name = input('Digite seu nome: ')
    age = int(input('Digite sua idade: '))
    weight = float(input('Digite seu peso: '))
    height = float(input('Digite sua altura: '))
    sex = input('Informe seu sexo: M (masculino) ou F (feminino): ').upper()

    new_client = {
        'nome': name,
        'idade': age,
        'peso': weight,
        'altura': height,
        'sexo': sex
    }

    clients.append(new_client)
    print(f'\nCliente {name} matriculado com sucesso!')

# Main program
while True:
    menu()
    option = input("Escolha uma opção: ")
    
    if option == '1':
        client_inputs()
        clients_data()
    elif option == '2':
        print("Encerrando programa...")
        break
    else:
        print("Opção inválida, tente novamente.")
