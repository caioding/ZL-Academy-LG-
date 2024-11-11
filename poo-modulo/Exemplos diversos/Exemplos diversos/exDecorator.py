def saudacao_decorator(func):
    def wrapper(nome):
        print("Olá!")
        func(nome)
        print("Tenha um bom dia!")
    return wrapper

@saudacao_decorator
def saudacao(nome):
    print(f"Prazer em conhecê-lo, {nome}.")

saudacao("Alice")
