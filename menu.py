import sys
sys.path.insert(0, 'livro')
from view import*




def show_menu():
    print("Selecione uma opção:")
    print("1. Inserir um novo livro")
    print("2. Inserir um novo usuário")
    print("3. Realizar um empréstimo")
    print("4. Atualizar a data de devolução de um empréstimo")
    print("5. Exibir todos os livros emprestados no momento")
    print("0. Sair")

    choice = input("Digite o número da opção desejada: ")
    return choice

# Loop principal do programa
while True:
    choice = show_menu()

    if choice == "1":
        title = input("Digite o título do livro: ")
        author = input("Digite o nome do autor do livro: ")
        publisher = input("Digite o nome da editora do livro: ")
        year = input("Digite o ano de publicação do livro: ")
        isbn = input("Digite o ISBN do livro: ")

        insert_book(title, author, publisher, year, isbn)
        print("Livro inserido com sucesso!")

    elif choice == "2":
        first_name = input("Digite o primeiro nome do usuário: ")
        last_name = input("Digite o sobrenome do usuário: ")
        address = input("Digite o endereço do usuário: ")
        email = input("Digite o endereço de e-mail do usuário: ")
        phone = input("Digite o número de telefone do usuário: ")

        insert_users(first_name, last_name, address, email, phone)
        print("Usuário inserido com sucesso!")

    elif choice == "3":
        user_id = input("Digite o ID do usuário: ")
        book_id = input("Digite o ID do livro: ")

        insert_loan(user_id, book_id, None, None)
        print("Empréstimo realizado com sucesso!")

    elif choice == "4":
        loan_id = input("Digite o ID do empréstimo: ")
        return_date = input("Digite a nova data de devolução (formato: AAAA-MM-DD): ")

        upadate_loans_date(loan_id, return_date)
        print("Data de devolução atualizada com sucesso!")

    elif choice == "5":
        books_on_loan = show_loans()
        print("Livros emprestados no momento:")
        for book in books_on_loan:
            print(f"Título: {book[0]}, Nome do usuário: {book[1]} {book[2]}, Data do empréstimo: {book[3]}, Data da devolução: {book[4]}")

    elif choice == "0":
        break

    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")