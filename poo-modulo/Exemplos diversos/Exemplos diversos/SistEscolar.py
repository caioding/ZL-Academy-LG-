class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def mostrar_info(self):
        print(f"Nome: {self.nome}, Matrícula: {self.matricula}")

class Curso:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.alunos = []  # Lista para armazenar os objetos de Aluno

    def adicionar_aluno(self, nome, matricula):
        # Cria um objeto Aluno e o adiciona à lista
        aluno = Aluno(nome, matricula)
        self.alunos.append(aluno)

    def mostrar_alunos(self):
        print(f"Alunos matriculados no curso {self.nome} ({self.codigo}):")
        for aluno in self.alunos:
            aluno.mostrar_info()


class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.cursos = []  # Lista para armazenar os objetos de Curso

    def adicionar_curso(self, nome_curso, codigo_curso):
        # Cria um objeto Curso e o adiciona à lista
        curso = Curso(nome_curso, codigo_curso)
        self.cursos.append(curso)

    def adicionar_aluno_ao_curso(self, codigo_curso, nome_aluno, matricula_aluno):
        # Procura o curso pelo código e adiciona o aluno
        for curso in self.cursos:
            if curso.codigo == codigo_curso:
                curso.adicionar_aluno(nome_aluno, matricula_aluno)
                return
        print(f"Curso com código {codigo_curso} não encontrado.")

    def mostrar_cursos(self):
        print(f"Cursos oferecidos pela escola {self.nome}:")
        for curso in self.cursos:
            print(f"Curso: {curso.nome} ({curso.codigo})")
            curso.mostrar_alunos()


# Criação de uma escola
escola = Escola("Escola Exemplo")

# Adicionando cursos à escola
escola.adicionar_curso("Matemática", "MAT101")
escola.adicionar_curso("História", "HIS102")

# Adicionando alunos aos cursos
escola.adicionar_aluno_ao_curso("MAT101", "João Silva", "202301")
escola.adicionar_aluno_ao_curso("MAT101", "Maria Souza", "202302")
escola.adicionar_aluno_ao_curso("HIS102", "Pedro Lima", "202303")

# Exibindo informações sobre a escola, cursos e alunos
escola.mostrar_cursos()
