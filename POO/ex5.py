class Aluno:
    def __init__(self, nome: str, matricula: int):
        self.__nome = nome
        self.__matricula = matricula

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula
        
    def mostrar_info(self):
        print(f"Nome: {self.nome}, Matricula: {self.matricula}")

class Curso:
    def __init__(self, nome: str, codigo: int, alunos: Aluno):
        self.__nome = nome
        self.__codigo = codigo
        self.__alunos = alunos
        alunos = []
        # self.alunos = Aluno()

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def alunos(self):
        return self.__alunos
    
    @alunos.setter
    def alunos(self, alunos):
        self.__alunos = alunos

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def mostrar_alunos(self):
        print(f"Alunos do curso de {self.nome}:")
        for aluno in self.alunos:
            aluno.mostrar_info()

class Escola:
    def __init__(self, nome: str, cursos: Curso):
        self.__nome = nome
        self.__cursos = cursos
        cursos = []

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cursos(self):
        return self.__cursos
    
    @cursos.setter
    def cursos(self, cursos):
        self.__cursos = cursos
    def adicionar_curso(self, curso):
        self.cursos.append(curso)
    
    def mostrar_cursos(self):
        print(f"Cursos da escola {self.nome}:")
        for curso in self.cursos:
            print(f"Curso: {curso.nome}")
            curso.mostrar_alunos()
            print()

def main():
# Criando objetos das classes Aluno, Curso e Escola
    aluno1 = Aluno("João", 123)
    aluno2 = Aluno("Maria", 456)
    aluno3 = Aluno("Pedro", 789)

    curso1 = Curso("Matemática", 101, [])
    curso1.adicionar_aluno(aluno1)
    curso1.adicionar_aluno(aluno2)

    curso2 = Curso("Português", 202, [])
    curso2.adicionar_aluno(aluno3)

    escola = Escola("Escola Municipal", [])
    escola.adicionar_curso(curso1)
    escola.adicionar_curso(curso2)

    # Exibindo as informações
    escola.mostrar_cursos()

    # Adicionando novos cursos e alunos
    aluno4 = Aluno("Ana", 901)
    curso3 = Curso("História", 303, [])
    curso3.adicionar_aluno(aluno4)
    escola.adicionar_curso(curso3)
    
    # Exibindo as informações
    escola.mostrar_cursos()

if __name__ == "__main__":
    main()

# Exemplo

# class Motor:
#     def ligar(self):
#         print("Motor Ligado")

# class Carro:
#     def __init__(self, modelo):
#         self.modelo = modelo
#         self.motor = Motor()
    
#     def dirigir(self):
#         print(f"dirigindo o carro {self.modelo}")
#         self.motor.ligar()
        	
# Carro = Carro("Gol")
# Carro.dirigir()