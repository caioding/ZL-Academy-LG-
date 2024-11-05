import json
import csv
import pickle
from functools import reduce

class Book:
    def __init__(self, title, author, year_published, genre):
        self._title = title
        self._author = author
        self._year_published = year_published
        self._genre = genre

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        self._title = title

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        self._author = author

    @property
    def year_published(self):
        return self._year_published
    
    @year_published.setter
    def year_published(self, year_published):
        self._year_published = year_published

    @property
    def genre(self):
        return self._genre
    
    @genre.setter
    def genre(self, genre):
        self._genre = genre
    
    def __repr__(self):
        return f"Título: {self._title}\nAutor: {self._author}\nAno de publicação: {self._year_published}\nGênero: {self._genre}"
    
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
    
    def list_books_by_author(self, author):
        return list(filter(lambda book: book.author == author, self.books))
    
    def export_for_text(self, file):
        with open(file, 'w') as f:
            for book in self.books:
                f.write(f"{book.title};{book.author};{book.year_published};{book.genre}\n")

    def import_from_text(self, file):
        with open(file, 'r') as f:
            for line in f:
                title, author, year_published, genre = line.strip().split(';')
                self.add_book(Book(title, author, int(year_published), genre))
    
    def export_for_json(self, file):
        with open(file, 'w') as f:
            json.dump([book.__dict__ for book in self.books], f)
    
    def import_from_json(self, file):
        with open(file, 'r') as f:
            data_books = json.load(f)
            for data in data_books:
                data = {k.lstrip('_'): v for k, v in data.items()}
                self.add_book(Book(**data))

    def export_for_csv(self, file):
        with open(file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Title', 'Author', 'Year Published', 'genre'])
            for book in self.books:
                writer.writerow([book.title, book.author, book.year_published, book.genre])
    
    def import_from_csv(self, file):
        with open(file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.add_book(Book(row['Title'], row['Author'], int(row['Year Published']), row['genre']))

    def export_for_binary(self, file):
        with open(file, 'wb') as f:
            pickle.dump(self.books, f)
    
    def import_from_binary(self, file):
        with open(file, 'rb') as f:
            self.books = pickle.load(f)

    def title_list(self):
        return list(map(lambda book: book.title, self.books))

    def books_by_genre(self, genre):
        return reduce(lambda count, book: count + 1 if book.genre == genre else count, self.books, 0)
    
    def filter_books(self, year_published=None, genre=None):
            return list(filter(lambda book: (year_published is None or book.year_published == year_published) and (genre is None or book.genre == genre), self.books))
    
    def backup(self, file, format="json"):
        if format == "json":
            self.export_for_json(file)
        elif format == "csv":
            self.export_for_csv(file)
        elif format == "binary":
            self.export_for_binary(file)
        else:
            raise ValueError("Formato inválido")

def __main__():
    library = Library()
    library.add_book(Book("Dom Casmurro", "Machado de Assis", 1899, "Drama"))
    library.add_book(Book("O Alienista", "H.G. Wells", 1898, "Ficção Científica"))
    library.add_book(Book("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, "Fantasia"))
    library.add_book(Book("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, "Fantasia"))
    library.add_book(Book("1984", "George Orwell", 1949, "Ficção Científica"))

    # List by author
    print("Livros por J.R.R. Tolkien:")
    for book in library.list_books_by_author("J.R.R. Tolkien"):
        print(book)

    # List by genre
    print("\nNúmero de livros de Ficção Científica:")
    print(library.books_by_genre("Ficção Científica"))

    # Export and import JSON data
    library.export_for_json("books.json")
    new_library = Library()
    new_library.import_from_json("books.json")

    print("\nLivros importados da biblioteca (JSON):")
    for book in new_library.books:
        print(book)

    # Export and import text data
    library.export_for_text("books.txt")
    new_library = Library()
    new_library.import_from_text("books.txt")

    print("\nLivros importados da biblioteca (Texto):")
    for book in new_library.books:
        print(book)

    # Export and import CSV data
    library.export_for_csv("books.csv")
    new_library = Library()
    new_library.import_from_csv("books.csv")

    print("\nLivros importados da biblioteca (CSV):")
    for book in new_library.books:
        print(book)

    # Export and import binary data
    library.export_for_binary("books.bin")
    new_library = Library()
    new_library.import_from_binary("books.bin")

    print("\nLivros importados da biblioteca (Binário):")
    for book in new_library.books:
        print(book)

    print("\nLivros filtrados por ano de publicação e gênero:")
    for book in library.filter_books(year_published=1899, genre="Drama"):
        print(book)

    # Backup
    library.backup("backup.json", format="json")

if __name__ == "__main__":
    __main__()
