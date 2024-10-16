# Criar uma hierarquia de classes que representem
# diferentes tipos de formulários (FormBase, FormularioContato, FormularioLogin).
# Utilizar BotCity para preencher automaticamente diferentes tipos de formulários
# em uma página web.

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
