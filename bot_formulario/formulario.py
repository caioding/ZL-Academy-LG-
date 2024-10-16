class FormBase:
    def __init__(self, nome, sexo, idade):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

class FormularioContato(FormBase):
    def __init__(self, nome, sexo, idade, email, mensagem):
        super().__init__(nome, sexo, idade)
        self.email = email
        self.mensagem = mensagem

class FormularioLogin(FormBase):
    def __init__(self, nome, sexo, idade, usuario, senha):
        super().__init__(nome, sexo, idade)
        self.usuario = usuario
        self.senha = senha
