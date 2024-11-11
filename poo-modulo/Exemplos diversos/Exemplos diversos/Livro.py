class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True  # Por padrão, o livro está disponível

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f'O livro "{self.titulo}" foi emprestado.')
        else:
            print(f'O livro "{self.titulo}" não está disponível no momento.')

    def devolver(self):
        self.disponivel = True
        print(f'O livro "{self.titulo}" foi devolvido e está disponível.')

    def mostrar_info(self):
        status = "disponível" if self.disponivel else "emprestado"
        print(f'Título: {self.titulo}, Autor: {self.autor}, Status: {status}')
