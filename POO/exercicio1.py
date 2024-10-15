class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O livro '{self.titulo}' foi emprestado.")
        else:
            print(f"O livro '{self.titulo}' já está emprestado.")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"O livro '{self.titulo}' foi devolvido.")
        else:
            print(f"O livro '{self.titulo}' já está disponível.")

    def mostrar_info(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        print(f"Título: {self.titulo}, Autor: {self.autor}, Status: {status}")


class Livraria:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado ao inventário.")

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                livro.emprestar()
                return
        print(f"Livro '{titulo}' não encontrado no inventário.")

    def mostrar_inventario(self):
        if len(self.livros) == 0:
            print("Inventário vazio.")
        else:
            for livro in self.livros:
                livro.mostrar_info()

livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien")
livro2 = Livro("1984", "George Orwell")

livraria = Livraria()
livraria.adicionar_livro(livro1)
livraria.adicionar_livro(livro2)

livraria.mostrar_inventario()

livraria.emprestar_livro("1984")
livraria.mostrar_inventario()

livro2.devolver()
livraria.mostrar_inventario()
