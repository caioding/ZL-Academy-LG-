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
