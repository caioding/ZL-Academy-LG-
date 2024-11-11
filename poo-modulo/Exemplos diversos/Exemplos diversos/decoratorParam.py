def multiplicar_por(n):
    def decorator(func):
        def wrapper(x):
            return func(x) * n
        return wrapper
    return decorator

@multiplicar_por(3)
def soma_dois(x):
    return x + 2

print(soma_dois(5))  