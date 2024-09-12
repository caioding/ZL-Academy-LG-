"""
Desafio em grupo: Seu grupo é uma empresa que necessita de uma ferramenta para solucionar um determinado problema.
Exemplos: 
- Entrada e saída de funcionários
- Registro de novos funcionários
- Listar materiais do almoxarifado
Crie um documento falando da sua empresa e explique o problema em que busca uma solução de desenvolvimento. Obs: não desenvolva o programa.
"""


# Lista global para armazenar os dados dos alunos
alunos = [
    # {
    #     "nomeAluno": "Lucas Andrade",
    #     "matricula": "ativo",
    #     "mediaEscolar": 8.5,
    #     "status": "aprovado"
    # },
    # {
    #     "nomeAluno": "Maria Silva",
    #     "matricula": "ativo",
    #     "mediaEscolar": 9.0,
    #     "status": "aprovado"
    # },
    # {
    #     "nomeAluno": "João Pereira",
    #     "matricula": "inativo",
    #     "mediaEscolar": 6.0,
    #     "status": "reprovado"
    # }
]


def menu():
    print("\n\n--- Menu ---")
    print("1 - Quem Somos")
    print("2 - Listar alunos matriculados")
    print("3 - Matricular aluno")
    print("4 - Encerrar programa")


def quemSomos():
    print("\n\n- Somos uma escola tradicional fundada em 1889 pelo Professor Doutor Tommy Lee Leite. Com proposta de ensino voltada para o ensino tecnológico, em tempo integral. Nossa proposta é que nossos alunos aprendam a montar geladeiras com caixa de isopor (invejando muitos alunos do SENAI). Sim, você vai ter tempo livre, garantimos a melhor educação para seus pestinhas.")
    print("- O Objetivo deste software é registrar e documentar os dados dos alunos matriculados")


def dadosAlunos():
    global alunos
    # Caminho completo para o arquivo 'registro_alunos.txt' na pasta desejada
    caminho_arquivo = r'C:\Users\matutino\Documents\Lucas Andrade\Python Nivelamento\Desafio Empresa\registro_alunos.txt'

    try:
        file = open(caminho_arquivo, 'w')
        for aluno in alunos:
            file.write(f"Nome: {aluno['nomeAluno']}\n")
            file.write(f"Matrícula: {aluno['matricula']}\n")
            file.write(f"Média Escolar: {aluno['mediaEscolar']}\n")
            file.write(f"Status: {aluno['status']}\n")
            file.write("\n")  
    finally:
        file.close()

    for aluno in alunos:
        print(f"Nome: {aluno['nomeAluno']}")
        print(f"Matrícula: {aluno['matricula']}")
        print(f"Média Escolar: {aluno['mediaEscolar']}")
        print(f"Status: {aluno['status']}")
        print()  


def matricularAluno():
    global alunos
    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite a matrícula do aluno (ativo/inativo): ")
    mediaEscolar = float(input("Digite a média escolar do aluno: "))
    status = input("Digite o status do aluno (aprovado/reprovado): ")

    novo_aluno = {
        "nomeAluno": nome,
        "matricula": matricula,
        "mediaEscolar": mediaEscolar,
        "status": status
    }

    alunos.append(novo_aluno)
    print(f"\nAluno {nome} matriculado com sucesso!")


while True:
    menu()
    op = int(input("Digite a opção desejada: "))

    match op:
        case 1:
            quemSomos()
        case 2:
            print("\nRegistro de alunos atualizado no arquivo 'registro_alunos.txt'")
            dadosAlunos()
        case 3:
            matricularAluno()
        case 4:
            print("Encerrando o programa...")
            break
        case _:
            print("Opção inválida. Tente novamente.")
