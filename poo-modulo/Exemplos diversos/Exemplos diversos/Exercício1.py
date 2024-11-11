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

class Livraria:
    def __init__(self):
        self.inventario = []  # Lista para armazenar os livros

    def adicionar_livro(self, livro):
        self.inventario.append(livro)
        print(f'O livro "{livro.titulo}" foi adicionado ao inventário.')

    def emprestar_livro(self, titulo):
        for livro in self.inventario:
            if livro.titulo == titulo:
                livro.emprestar()
                return
        print(f'O livro "{titulo}" não foi encontrado no inventário.')

    def mostrar_inventario(self):
        if len(self.inventario) == 0:
            print("O inventário está vazio.")
        else:
            print("Inventário da Livraria:")
            for livro in self.inventario:
                livro.mostrar_info()

#testa as classes livro e livraria
if __name__ == "__main__":
    # Criando a livraria
    livraria = Livraria()

    # Adicionando livros à livraria
    livro1 = Livro("1984", "George Orwell")
    livro2 = Livro("Dom Casmurro", "Machado de Assis")

    livraria.adicionar_livro(livro1)
    livraria.adicionar_livro(livro2)

    # Exibindo o inventário
    livraria.mostrar_inventario()

    # Emprestando um livro
    livraria.emprestar_livro("1984")

    # Tentando emprestar novamente o mesmo livro
    livraria.emprestar_livro("1984")

    # Devolvendo o livro
    livro1.devolver()

    # Exibindo o inventário novamente
    livraria.mostrar_inventario()

