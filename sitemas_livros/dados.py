import sqlite3 

# Conectar ou criar o banco de dados
conn = sqlite3.connect('dados.db')

# Criar tabela 'livros'
conn.execute('''CREATE TABLE livros (
                id INTEGER PRIMARY KEY,
                titulo TEXT,
                autor TEXT,
                editora TEXT,
                ano_publicacao INTEGER,
                isbn TEXT
            )''')

# Criar tabela 'usuarios'
conn.execute('''CREATE TABLE usuarios (
                id INTEGER PRIMARY KEY,
                nome TEXT,
                sobrenome TEXT,
                endereco TEXT,
                email TEXT,
                telefone TEXT
            )''')

# Criar tabela 'emprestimo'
conn.execute('''CREATE TABLE emprestimo (
                id INTEGER PRIMARY KEY,
                id_livro INTEGER,
                id_usuario INTEGER,
                data_emprestimo TEXT,
                data_devolucao TEXT,
                telefone TEXT,
                FOREIGN KEY(id_livro) REFERENCES livros(id),
                FOREIGN KEY(id_usuario) REFERENCES usuarios(id)
            )''')

# Commit para salvar as alterações
conn.commit()

# Fechar a conexão após uso
conn.close()
