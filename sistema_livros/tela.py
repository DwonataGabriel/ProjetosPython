from tkinter import *
from tkinter import Tk
from PIL import Image, ImageTk
from view import *       
from tkinter import messagebox
from tkinter import ttk
from view_users import *
from view_books import *
from tkinter.messagebox import showerror, showwarning


b1 = "#00000" 
b11 = "#1C1C1C"
b2 = "#A9A9A9"
b3 = "#C0C0C0"
b4 = "#DCDCDC" #label names
m1 = "#FF8C00" #menu
line_show_data = "#191970"


janela = Tk()
janela.title("TFT livraria")
janela.configure(background="white")
janela.geometry('750x350')
janela.resizable(width=False, height=FALSE)





frame_top = Frame(janela,width=750, height=50, bg=m1, relief="flat")
frame_top.grid(row=0, column=0, columnspan=2, sticky=NSEW)

frame_left = Frame(janela, width=200, height=265, bg=b2, relief="solid")
frame_left.grid(row = 1, column= 0, columnspan=2, sticky=NSEW)

frame_right = Frame(janela, width=550, height=265, bg=b3, relief="raised")
frame_right.grid(row = 1, column= 1, columnspan=2, sticky=NSEW)


app_img = Image.open('../sistema_livros/icons/livro.png')
app_img = app_img.resize((40, 40))
app_img = ImageTk.PhotoImage(app_img)

app_add_img =Label(frame_top, image=app_img, width=1000, compound=LEFT, padx=5,anchor=NW, bg=m1)
app_add_img.place(x=5, y=0)

app_text =Label(frame_top, text="Sistema de Gerenciamento de Livros", compound=LEFT, padx=5,anchor=NW, font=('Verdana 15 bold'), bg=m1 ,fg="black")
app_text.place(x=50, y=7)


app_line =Label(frame_top, width=770, height=1, padx=5,anchor=NW, font=('Verdana 15 bold'), bg="black")
app_line.place(x=0, y=47)



def new_user():

    global img_salvar
    def add():
        first_name = ent_nome.get()
        last_name = ent_sobrenome.get()
        address = entrada_endereco.get()
        email = entrada_endereco_email.get()
        tel = entrada_tel.get()

        list = [first_name, last_name, address, email, tel]
   
        
        for i in list:
            if i == '':
                messagebox.showerror('Erro', 'Preencha todos campos')    
                return 

        insert_users(first_name, last_name, address, email, tel)
        messagebox.showinfo('Sucesso', 'Usuário inserido com sucesso')

        ent_nome.delete(0,END)
        ent_sobrenome.delete(0,END)
        entrada_endereco.delete(0,END)
        entrada_endereco_email.delete(0,END)
        entrada_tel.delete(0,END)

    app_ = Label(frame_right, text="Inserir um Novo Usuário", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=b11, fg=b3 )
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)

    lab_nome = Label(frame_right, text="Primeiro Nome", anchor=NW, font=('Ivy 10'), bg=b4, fg=b11)
    lab_nome.grid(row=2, column=0, padx=5, pady=10, sticky=NSEW)

    ent_nome = Entry(frame_right, width=25, justify="left", relief="solid")
    ent_nome.grid(row=2, column=1, padx=5, pady=10, sticky=NSEW)


    lab_sobrenome = Label(frame_right, text="Segundo Nome", anchor=NW, font=('Ivy 10'), bg=b4, fg=b11)
    lab_sobrenome.grid(row=3, column=0, padx=5, pady=10, sticky=NSEW)
    
    ent_sobrenome = Entry(frame_right, width=25, justify="left", relief="solid")
    ent_sobrenome.grid(row=3, column=1, padx=5, pady=10, sticky=NSEW)


    lab_endereco = Label(frame_right, text="Endereço do Usuário", anchor=NW, font=('Ivy 10'), bg=b4, fg=b11)
    lab_endereco.grid(row=4, column=0, padx=5, pady=10, sticky=NSEW)

    entrada_endereco = Entry(frame_right, width=25, justify="left", relief="solid")
    entrada_endereco.grid(row=4, column=1, padx=5, pady=10, sticky=NSEW)

 
    lab_endereco_email = Label(frame_right, text="Endereço de Email", anchor=NW, font=('Ivy 10'), bg=b4, fg=b11)
    lab_endereco_email.grid(row=5, column=0, padx=5, pady=10, sticky=NSEW)

    entrada_endereco_email = Entry(frame_right, width=25, justify="left", relief="solid")
    entrada_endereco_email.grid(row=5, column=1, padx=5, pady=10, sticky=NSEW)
     
    lab_tel = Label(frame_right, text="Número de Telefone", anchor=NW, font=('Ivy 10'), bg=b4, fg=b11)
    lab_tel.grid(row=6, column=0, padx=5, pady=10, sticky=NSEW)

    entrada_tel = Entry(frame_right, width=25, justify="left", relief="solid")
    entrada_tel.grid(row=6, column=1, padx=5, pady=10, sticky=NSEW)

    img_salvar = Image.open('../sistema_livros/icons/img_salvar.png')
    img_salvar = img_salvar.resize((30,30))
    img_salvar = ImageTk.PhotoImage(img_salvar)

    btn_save = Button(frame_right,command=add, image=img_salvar, compound=LEFT, anchor=NW, text="Salvar", bg=b11, fg=b2, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    btn_save.grid(row=7, column=1, sticky=NSEW, padx=5, pady=6 )

def new_book():
    global img_salvar
    def add():

        name_book = ent_name_book.get()
        autor = ent_name_autor.get()
        editora = ent_name_edit.get()
        isbn = ent_isbn.get()
        data_pub = ent_pub.get()

        list = [name_book, autor, editora, isbn, data_pub]

        for i in list:
            if i == '':
                messagebox.showerror('Erro', 'Preencha Todos os campos')
                return

        insert_book(name_book, autor, editora, isbn, data_pub)
        messagebox.showinfo('Sucesso', 'Livro inserido com sucesso')
  

        ent_name_book.delete(0,END)
        ent_name_autor.delete(0, END)
        ent_name_edit.delete(0,END)
        ent_isbn.delete(0,END)
        ent_pub.delete(0,END)



    app_ = Label(frame_right, text="Inserir um Novo Livro", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=b11, fg=b3 )
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    
    lab_name_book = Label(frame_right, text="Nome do Livro", anchor=NW, font=('Ivy 10'), bg=b4, fg=b11)
    lab_name_book.grid(row=2, column=0, padx=5, pady=10, sticky=NSEW)
    ent_name_book = Entry(frame_right, width=25, justify="left", relief="solid")
    ent_name_book.grid(row=2, column=1, padx=5, pady=10, sticky=NSEW)
    
    lab_name_autor = Label(frame_right, text="Autor", anchor=NW, font=('Ivy 10'), bg=b4, fg=b11)
    lab_name_autor.grid(row=3, column=0, padx=5, pady=10, sticky=NSEW)
    ent_name_autor = Entry(frame_right, width=25, justify="left", relief="solid")
    ent_name_autor.grid(row=3, column=1, padx=5, pady=10, sticky=NSEW)

    lab_name_edit = Label(frame_right, text="Editora", anchor=NW, font=('Ivy 10'), bg=b4, fg=b11)
    lab_name_edit.grid(row=4, column=0, padx=5, pady=10, sticky=NSEW)
    ent_name_edit = Entry(frame_right, width=25, justify="left", relief="solid")
    ent_name_edit.grid(row=4, column=1, padx=5, pady=10, sticky=NSEW)
    
    lab_pub = Label(frame_right, text="Ano Publicação", anchor=NW, font=('Ivy 10'), bg=b4, fg=b11)
    lab_pub .grid(row=5, column=0, padx=5, pady=10, sticky=NSEW)
    ent_pub = Entry(frame_right, width=25, justify="left", relief="solid")
    ent_pub.grid(row=5, column=1, padx=5, pady=10, sticky=NSEW)

    lab_isbn = Label(frame_right, text="ISBN", anchor=NW, font=('Ivy 10'), bg=b4, fg=b11)
    lab_isbn.grid(row=6, column=0, padx=5, pady=10, sticky=NSEW)
    ent_isbn = Entry(frame_right, width=25, justify="left", relief="solid")
    ent_isbn.grid(row=6, column=1, padx=5, pady=10, sticky=NSEW)

    img_salvar = Image.open('../sistema_livros/icons/img_salvar.png')
    img_salvar = img_salvar.resize((30,30))
    img_salvar = ImageTk.PhotoImage(img_salvar)

    btn_save = Button(frame_right,command=add, image=img_salvar, compound=LEFT, anchor=NW, text="Salvar", bg=b11, fg=b2, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    btn_save.grid(row=7, column=1, sticky=NSEW, padx=5, pady=6  )


def show_books_home():
    global img_salvar
    main_books()


def show_users_home():
    global tree
    main_users()
    print("chamou show users")

def realizar_emprestimo():
    pass 

def date_devolution():
    pass

def show_loan_database():
    pass

def control(i):
    if i == 'new_user':
        for widget in frame_right.winfo_children():
            widget.destroy()
        new_user()
        print('Chamou novo usuario')

    if i == 'new_book':
        for widget in frame_right.winfo_children():
            widget.destroy()
        new_book()
        print('Chamou novo livro')
       

    if i == 'show_books_home':
        for widget in frame_right.winfo_children():
            widget.destroy()
        show_books_home()
        print('chamou exibir books cadastrados ')

    if i == 'show_users_home':
        for widget in frame_right.winfo_children():
            widget.destroy()
        show_users_home()
        print('chamou exibir users ')

    if i == 'realizar_emprestimo':
        for widget in frame_right.winfo_children():
            widget.destroy()
        realizar_emprestimo()
        print("chamou realizar emp")

    if i == 'date_devolution':
        for  widget in frame_right.winfo_children():       
            widget.destroy()
        date_devolution()
        print("chamo dev")

    if i == 'show_loan_database': 
        for widger in frame_right.winfo_children():
            widget.destroy()
        show_loan_database()
   


#menu interface lateral--------------
#add user---------
user_img = Image.open('../sistema_livros/icons/add.png')
user_img = user_img.resize((18,18 ))
user_img = ImageTk.PhotoImage(user_img)
add_usuario = Button(frame_left, command=lambda:control('new_user'), image=user_img, compound=LEFT, anchor=NW, text="Novo Usuário", bg=b11, fg=b2, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
add_usuario.grid(row=0, column=0, sticky=NSEW, padx=5, pady=6
               )
#new book
img_book = Image.open('../sistema_livros/icons/add.png')
img_book = img_book.resize((18,18))
img_book = ImageTk.PhotoImage(img_book)

add_book = Button(frame_left,command=lambda:control('new_book'), image=img_book, compound=LEFT, anchor=NW, text="Novo Livro", bg=b11, fg=b2, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
add_book.grid(row=1, column=0, sticky=NSEW, padx=5, pady=6  )


#show books
img_show_books = Image.open('../sistema_livros/icons/livro.png')
img_show_books = img_show_books.resize((18,18))
img_show_books = ImageTk.PhotoImage(img_show_books)

show_books = Button(frame_left, command=lambda:control('show_books_home'), image=img_show_books, compound=LEFT, anchor=NW, text="Exibir Todos Livros", bg=b11, fg=b2, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE )
show_books.grid(row=2, column=0, sticky=NSEW, padx=5, pady=6 )

#show users
img_show_users = Image.open('../sistema_livros/icons/user.png')
img_show_users = img_show_users.resize((18,18))
img_show_users = ImageTk.PhotoImage(img_show_users)

show_users = Button(frame_left, command=lambda:control("show_users_home"),image=img_show_users, compound=LEFT, anchor=NW, text="Exibir Todos Usuários", bg=b11, fg=b2, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE  )
show_users.grid(row=3, column=0, sticky=NSEW, padx=5, pady=6 )

#realizar      emp
img_emp_users = Image.open('../sistema_livros/icons/add.png')
img_emp_users = img_emp_users.resize((18,18))
img_emp_users = ImageTk.PhotoImage(img_emp_users)

add_empp = Button(frame_left, command=lambda:control("realizar_emprestimo"),image=img_emp_users, compound=LEFT, anchor=NW, text="Realizar Emprestimo", bg=b11, fg=b2, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE  )
add_empp .grid(row=4, column=0, sticky=NSEW, padx=5, pady=6 )

#devolucao emp
img_dev_emp = Image.open('../sistema_livros/icons/return.png')
img_dev_emp = img_dev_emp.resize((16,16 ))
img_dev_emp = ImageTk.PhotoImage(img_dev_emp)

#emprestados 
add_devolution  =  Button(frame_left, command=lambda:control("date_devolution"),image=img_dev_emp, compound=LEFT, anchor=NW, text="Adicionar Data Devolução", bg=b11, fg=b2, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
add_devolution.grid(row=5 ,column=0, padx=5, pady=6)


img_show_emp = Image.open('../sistema_livros/icons/livro.png')
img_show_emp = img_show_emp.resize((18,18 ))
img_show_emp = ImageTk.PhotoImage(img_show_emp)

show_books_emp  =  Button(frame_left, command=lambda:control("show_loan_database"), image=img_show_emp, compound=LEFT, anchor=NW, text="Exibir Livros emprestados", bg=b11, fg=b2, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
show_books_emp.grid(row=6 ,column=0, padx=5, pady=6)

janela.mainloop()

