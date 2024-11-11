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
