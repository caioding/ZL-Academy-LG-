class InsufficientBalanceError(Exception):
    pass

class LimitExceededError(Exception):
    pass

class InvalidDestinationAccountError(Exception):
    pass

class Account:
    def __init__(self, owner, balance, limit):
        self.__owner = owner
        self.__balance = balance
        self.__limit = limit

    @property
    def owner(self):
        return self.__owner

    @property
    def balance(self):
        return self.__balance

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, limit):
        self.__limit = limit

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    @owner.setter
    def owner(self, owner):
        self.__owner = owner

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise InsufficientBalanceError("Saldo insuficiente para realizar o saque.")
        self.__balance -= amount

    def transfer(self, amount, destination_account):
        if amount > self.__limit:
            raise LimitExceededError("Valor da transferência excede o limite da conta.")
        if not isinstance(destination_account, Account):
            raise InvalidDestinationAccountError("Conta de destino inválida.")
        self.withdraw(amount)
        destination_account.deposit(amount)

# Limit exceeded example
try:
    account1 = Account("Alice", 1000, 500)
    account2 = Account("Bob", 500, 300)
    account1.transfer(600, account2)
except InsufficientBalanceError as e:
    print(e)
except LimitExceededError as e:
    print(e)
except InvalidDestinationAccountError as e:
    print(e)

# Insufficient balance example
try:
    account1.withdraw(1500)
except InsufficientBalanceError as e:
    print(e)

# Invalid destination account example
try:
    account1.transfer(100, "InvalidAccount")
except InvalidDestinationAccountError as e:
    print(e)

# Deposit example
try:
    account1.deposit(200)
    print(f"Depósito realizado com sucesso. Novo saldo: {account1.balance}, {account1.owner}")
except Exception as e:
    print(e)


class InvalidNameError(Exception):
    pass

class InvalidAgeError(Exception):
    pass

class InvalidEmailError(Exception):
    pass

class User:
    def __init__(self, name, age, email):
        if not name:
            raise InvalidNameError("Nome não pode ser vazio.")
        if not isinstance(age, int):
            raise InvalidAgeError("Idade deve ser um inteiro.")
        if "@" not in email:
            raise InvalidEmailError("Email inválido.")
        self.name = name
        self.age = age
        self.email = email

# Invalid name example
try:
    user = User("", 25, "email@domain.com")
except InvalidNameError as e:
    print(e)
except InvalidAgeError as e:
    print(e)
except InvalidEmailError as e:
    print(e)

# Invalid age example
try:
    user = User("Alice", "vinte e cinco", "alice@domain.com")
except InvalidNameError as e:
    print(e)
except InvalidAgeError as e:
    print(e)
except InvalidEmailError as e:
    print(e)

# Invalid email example
try:
    user = User("Bob", 30, "bobdomain.com")
except InvalidNameError as e:
    print(e)
except InvalidAgeError as e:
    print(e)
except InvalidEmailError as e:
    print(e)

# Correct user creation
try:
    user = User("Charlie", 28, "charlie@domain.com")
    print(f"Usuário criado com sucesso: {user.name}, {user.age}, {user.email}")
except InvalidNameError as e:
    print(e)
except InvalidAgeError as e:
    print(e)
except InvalidEmailError as e:
    print(e)