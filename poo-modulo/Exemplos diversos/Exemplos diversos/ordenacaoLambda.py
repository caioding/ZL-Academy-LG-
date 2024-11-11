dobrar = lambda x: x * 2
print(dobrar(5))  # Saída: 10


# Lista de tuplas (nome, idade)
pessoas = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]

# Ordena pela idade (segundo elemento da tupla)
pessoas_ordenadas = sorted(pessoas, key=lambda pessoa: pessoa[1])
print(pessoas_ordenadas)  # Saída: [('Bob', 25), ('Alice', 30), ('Charlie', 35)]

# Lista de dicionários
produtos = [
    {"nome": "Camisa", "preco": 50},
    {"nome": "Calça", "preco": 100},
    {"nome": "Sapato", "preco": 200}
]

# Ordena pelo preço do produto
produtos_ordenados = sorted(produtos, key=lambda produto: produto["preco"])
print(produtos_ordenados)  # Ordenados por preço crescente

#exemplos função map()
numeros = [1, 2, 3, 4]
dobrados = list(map(lambda x: x * 2, numeros))
print(dobrados)  # Saída: [2, 4, 6, 8]

# Lista de temperaturas em Celsius
temperaturas_celsius = [0, 20, 37, 100]

# Converte cada temperatura para Fahrenheit
temperaturas_fahrenheit = list(map(lambda c: c * 9/5 + 32, temperaturas_celsius))
print(temperaturas_fahrenheit)  # Saída: [32.0, 68.0, 98.6, 212.0]

#elevar ao quadrado
numeros = [1, 2, 3, 4, 5]
numeros_quadrados = list(map(lambda x: x ** 2, numeros))
print(numeros_quadrados)  # Saída: [1, 4, 9, 16, 25]


#exemplo funcao filter()
#filtrar numeros pares
numeros = [1, 2, 3, 4, 5]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Saída: [2, 4]

#filtrar palavras com mais de 5 letras
palavras = ["Python", "é", "incrível", "para", "data", "science"]
palavras_longas = list(filter(lambda palavra: len(palavra) > 5, palavras))
print(palavras_longas)  # Saída: ['Python', 'incrível', 'science']


from functools import reduce

numeros = [1, 2, 3, 4]
soma = reduce(lambda x, y: x + y, numeros)
print(soma)  # Saída: 10

#encontrar o maior valor em uma lista
numeros = [1, 2, 3, 4, 5]
maior = reduce(lambda x, y: x if x > y else y, numeros)
print(maior)  # Saída: 5

numeros = [1, 2, 2, 3, 4, 4]
quadrados_set = {x ** 2 for x in numeros}
print(quadrados_set)  # Saída: {16, 1, 4, 9}

