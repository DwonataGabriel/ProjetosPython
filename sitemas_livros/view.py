import sqlite3

# Func para conectar
def connect():
    return sqlite3.connect('dados.db')

# Func para inserir livros
def insert_book(titulo, autor, editora, ano_publicacao, isbn):
    conn = connect()
    conn.execute("INSERT INTO livros(titulo, autor, editora, ano_publicacao, isbn) VALUES (?, ?, ?, ?, ?)",
                 (titulo, autor, editora, ano_publicacao, isbn))
    conn.commit()
    conn.close()

# Func para inserir usuários
def insert_users(nome, sobrenome, endereco, email, telefone):
    conn = connect()
    conn.execute("INSERT INTO usuarios(nome, sobrenome, endereco, email, telefone) VALUES (?, ?, ?, ?, ?)",
                 (nome, sobrenome, endereco, email, telefone))
    conn.commit()
    conn.close()

# Func para exibir livros
def show_livros():
    conn = connect()
    livros = conn.execute("SELECT * FROM livros").fetchall()
    conn.close()

    if not livros: 
        print("Nenhum livro encontrado na Biblioteca")
        return

    print("Livros na Biblioteca")
    for livro in livros:
        print(f"ID: {livro[0]}")
        print(f"Título: {livro[1]}")
        print(f"Autor: {livro[2]}")
        print(f"Editora: {livro[3]}")
        print(f"Ano de Publicação: {livro[4]}")
        print(f"ISBN: {livro[5]}")
        print("\n")

# Func para realizar empréstimo
def insert_loan(id_livro, id_usuario, data_emprestimo, data_devolucao):
    conn = connect()
    conn.execute("INSERT INTO emprestimo(id_livro, id_usuario, data_emprestimo, data_devolucao)\
                  VALUES (?, ?, ?, ?)", (id_livro, id_usuario, data_emprestimo, data_devolucao))
    conn.commit()
    conn.close()


#pegar os emprestimos existentes
def get_loans():
    conn = connect()
    res = conn.execute("SELECT livros.titulo, usuarios.nome, usuarios.sobrenome, emprestimo.data_emprestimo, emprestimo.data_devolucao\
                       FROM livros\
                       INNER JOIN emprestimo ON livros.id = emprestimo.id_livro\
                       INNER JOIN usuarios ON usuarios.id = emprestimo.id_usuario\
                       WHERE emprestimo.data_devolucao IS NULL").fetchall()
    conn.close()
    return res
# Func para exibir os empréstimos
def show_loans():
    loans = get_loans()  # Chama a função get_loans para obter os empréstimos
    
    if not loans:
        print("Nenhum empréstimo em aberto.")
        return

    print("Empréstimos em aberto:")
    for loan in loans:
        print("\n")
        print(f"Título do Livro: {loan[0]}")
        print(f"Nome do Usuário: {loan[1]} {loan[2]}")
        print(f"Data do Empréstimo: {loan[3]}")
        print(f"Data de Devolução: {loan[4]}")
        print("\n")


def upadate_loans_date(id_emprestimo, data_devolucao):
    conn = connect()
    conn.execute("UPDATE emprestimo SET data_devolucao = ? WHERE id = ?", (id_emprestimo, data_devolucao))
    conn.commit()
    conn.close()
#insert_book("Dom Quixote", "Miguel de Cervantes", "Saraiva", 1500, "666")
#insert_users("Pedro", "Silva", "Rua Junai", "joao@email.com", "123456")
#insert_loan(1, 1, "23/05/2004", None)  # Supondo que os IDs dos livros e usuários correspondem a 1


#upadate_loans_date(1, "17/10/2004")
show_livros()


#funcs
'''insert_book()
   insert_users()
   show_livros()
   insert_loan()
   get_loans()
   show_loans()
   upadate_loans_date()


'''
