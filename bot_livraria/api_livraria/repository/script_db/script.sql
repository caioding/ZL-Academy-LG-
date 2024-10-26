-- Apagar o banco de dados
-- drop database banco;

-- Criar o banco de dados
create database banco;

-- Atribuir os privilégios de acesso aos objetos do banco
-- para o usuário root
GRANT ALL PRIVILEGES ON banco.* TO 'root'@'localhost';

-- Acessar o banco de dados: banco
USE banco;

-- Criar a tabela: autor
CREATE TABLE autor(
    id INT AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
);

-- Criar a tabela: livro
CREATE TABLE livro(
    id INT AUTO_INCREMENT,
    titulo VARCHAR(100) NOT NULL,
    codigo VARCHAR(20) NOT NULL,
    emprestimo_disponivel BOOLEAN NOT NULL DEFAULT TRUE,
    autor_id INT,
    PRIMARY KEY (id),
    FOREIGN KEY (autor_id) REFERENCES autor(id)
);

-- Criar a tabela: biblioteca
CREATE TABLE biblioteca(
    id INT AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
);

-- Criar a tabela: emprestimo
CREATE TABLE emprestimo(
    id INT AUTO_INCREMENT,
    livro_id INT,
    cliente VARCHAR(100) NOT NULL,
    data_emprestimo DATE NOT NULL,
    data_devolucao DATE,
    PRIMARY KEY (id),
    FOREIGN KEY (livro_id) REFERENCES livro(id)
);

-- Inserir registros na tabela autor
INSERT INTO autor(nome) VALUES('J.K. Rowling');
INSERT INTO autor(nome) VALUES('George R.R. Martin');

-- Inserir registros na tabela livro
INSERT INTO livro(titulo, codigo, autor_id) VALUES('Harry Potter e a Pedra Filosofal', 'HP1', 1);
INSERT INTO livro(titulo, codigo, autor_id) VALUES('Harry Potter e a Câmara Secreta', 'HP2', 1);
INSERT INTO livro(titulo, codigo, autor_id) VALUES('A Guerra dos Tronos', 'GOT1', 2);
INSERT INTO livro(titulo, codigo, autor_id) VALUES('A Fúria dos Reis', 'GOT2', 2);

-- Inserir registros na tabela biblioteca
INSERT INTO biblioteca(nome) VALUES('Biblioteca Central');