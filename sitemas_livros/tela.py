from tkinter import*
from PIL import Image, ImageTk
from view import*       
from tkinter import messagebox

b1 = "#00000" 
b11 = "#1C1C1C"
b2 = "#A9A9A9"
b3 = "#C0C0C0"
b4 = "#DCDCDC" #label names
m1 = "#FF8C00" #menu


janela = Tk()
janela.title("TFT livraria")
janela.configure(background="white")
janela.geometry('750x350')
janela.resizable(width=FALSE, height=FALSE)





frame_cima = Frame(janela,width=750, height=50, bg=m1, relief="flat")
frame_cima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

frame_left = Frame(janela, width=200, height=265, bg=b2, relief="solid")
frame_left.grid(row = 1, column= 0, columnspan=2, sticky=NSEW)

frame_direita = Frame(janela, width=550, height=265, bg=b3, relief="raised")
frame_direita.grid(row = 1, column= 1, columnspan=2, sticky=NSEW)



#logos

#abrindo a img 

app_img = Image.open('livro/icons/Livro.png  ')
app_img = app_img.resize((40, 40 ))
app_img= ImageTk.PhotoImage(app_img)

app_add_img =Label(frame_cima, image=app_img, width=1000, compound=LEFT, padx=5,anchor=NW, bg=m1)
app_add_img.place(x=5, y=0)

app_text =Label(frame_cima, text="Sistema de Gerenciamento de Livros", compound=LEFT, padx=5,anchor=NW, font=('Verdana 15 bold'), bg=m1 ,fg="black")
app_text.place(x=50, y=7)


app_line =Label(frame_cima, width=770, height=1, padx=5,anchor=NW, font=('Verdana 15 bold'), bg="black")
app_line.place(x=0, y=47)



def new_user():

    global img_salvar
    def add():
        first_name = ent_nome.get()
        last_name = ent_sobrenome.get()
        address = entrada_endereco.get()
        email = entrada_endereco_email.get()
        tel = entrada_tel.get()

        lista = [first_name, last_name, address, email, tel]
      
        
        for i in lista :
            if i =='':
                messagebox.showerror('Erro', 'Preencha todos campos')    
                return 
        insert_users(first_name, last_name, address, email, tel)
        messagebox.showinfo('Sucesso', 'Usuário inserido com sucesso')

        ent_nome.delete(0,END)
        ent_sobrenome.delete(0,END)
        entrada_endereco.delete(0,END)
        entrada_endereco_email.delete(0,END)
        entrada_tel.delete(0,END)
    app_ = Label(frame_direita, text="Inserir um Novo Usuário", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=b11, fg=b3 )
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)

    lab_nome = Label(frame_direita, text="Primeiro Nome", anchor=NW, font=('Ivy 10'), bg=b4, fg=b11)
    lab_nome.grid(row=2, column=0, padx=5, pady=10, sticky=NSEW)

    ent_nome = Entry(frame_direita, width=25, justify="left", relief="solid")
    ent_nome.grid(row=2, column=1, padx=5, pady=10, sticky=NSEW)


    lab_sobrenome = Label(frame_direita, text="Segundo Nome", anchor=NW, font=('Ivy 10'), bg=b4, fg=b11)
    lab_sobrenome.grid(row=3, column=0, padx=5, pady=10, sticky=NSEW)
    
    ent_sobrenome = Entry(frame_direita, width=25, justify="left", relief="solid")
    ent_sobrenome.grid(row=3, column=1, padx=5, pady=10, sticky=NSEW)


    lab_endereco = Label(frame_direita, text="Endereço do Usuário", anchor=NW, font=('Ivy 10'), bg=b4, fg=b11)
    lab_endereco.grid(row=4, column=0, padx=5, pady=10, sticky=NSEW)

    entrada_endereco = Entry(frame_direita, width=25, justify="left", relief="solid")
    entrada_endereco.grid(row=4, column=1, padx=5, pady=10, sticky=NSEW)

 
    lab_endereco_email = Label(frame_direita, text="Endereço de Email", anchor=NW, font=('Ivy 10'), bg=b4, fg=b11)
    lab_endereco_email.grid(row=5, column=0, padx=5, pady=10, sticky=NSEW)

    entrada_endereco_email = Entry(frame_direita, width=25, justify="left", relief="solid")
    entrada_endereco_email.grid(row=5, column=1, padx=5, pady=10, sticky=NSEW)
     
    lab_tel = Label(frame_direita, text="Número de Telefone", anchor=NW, font=('Ivy 10'), bg=b4, fg=b11)
    lab_tel.grid(row=6, column=0, padx=5, pady=10, sticky=NSEW)

    entrada_tel = Entry(frame_direita, width=25, justify="left", relief="solid")
    entrada_tel.grid(row=6, column=1, padx=5, pady=10, sticky=NSEW)

    img_salvar = Image.open('livro/icons/img_salvar.png')
    img_salvar = img_salvar.resize((30,30))
    img_salvar = ImageTk.PhotoImage(img_salvar)

    btn_save = Button(frame_direita,command=add, image=img_salvar, compound=LEFT, anchor=NW, text="Salvar", bg=b11, fg=b2, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    btn_save.grid(row=7, column=1, sticky=NSEW, padx=5, pady=6  )

def new_libre():
    app_ = Label(frame_direita, text="Inserir um Novo Livro", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=b11, fg=b3 )
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    
    lab_name_libre = Label(frame_direita, text="Nome do Livro", anchor=NW, font=('Ivy 10'), bg=b4, fg=b11)
    lab_name_libre.grid(row=2, column=0, padx=5, pady=10, sticky=NSEW)

    ent_name_libre = Entry(frame_direita, width=25, justify="left", relief="solid")
    ent_name_libre.grid(row=2, column=1, padx=5, pady=10, sticky=NSEW)

    
#def para menu  
 

def control(i):
    if i == 'novo_usuario':
        for widget in frame_direita.winfo_children():
            widget.destroy()
        new_user()

    if i == 'new_libre':
        for widget in frame_direita.winfo_children():
            widget.destroy()
        new_libre()




#menu interface--------------
#add user---------
user_img = Image.open('livro/icons/add.png')
user_img = user_img.resize((18,18  ))
user_img = ImageTk.PhotoImage(user_img)
add_usuario = Button(frame_left, command=lambda:control('novo_usuario'), image=user_img, compound=LEFT, anchor=NW, text="Novo Usuário", bg=b11, fg=b2, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
add_usuario.grid(row=0, column=0, sticky=NSEW, padx=5, pady=6
               )
#new libre


img_libre = Image.open('livro/icons/add.png')
img_libre = img_libre.resize((18,18))
img_libre = ImageTk.PhotoImage(img_libre)

add_libre = Button(frame_left,command=lambda:control('new_libre'), image=img_libre, compound=LEFT, anchor=NW, text="Novo Livro", bg=b11, fg=b2, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
add_libre.grid(row=1, column=0, sticky=NSEW, padx=5, pady=6  )


#show libres


img_show_libres = Image.open('livro/icons/livro.png')
img_show_libres = img_show_libres.resize((18,18))
img_show_libres= ImageTk.PhotoImage(img_show_libres)

show_libres = Button(frame_left, image=img_show_libres, compound=LEFT, anchor=NW, text="Exibir Todos Livros", bg=b11, fg=b2, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE  )
show_libres.grid(row=2, column=0, sticky=NSEW, padx=5, pady=6 )

#show users

img_show_users = Image.open('livro/icons/user.png')
img_show_users = img_show_users.resize((18,18))
img_show_users = ImageTk.PhotoImage(img_show_users)

show_users = Button(frame_left, image=img_show_users, compound=LEFT, anchor=NW, text="Exibir Todos Usuários", bg=b11, fg=b2, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE  )
show_users.grid(row=3, column=0, sticky=NSEW, padx=5, pady=6 )

#realizar emp
img_emp_users = Image.open('livro/icons/add.png')
img_emp_users = img_emp_users.resize((18,18))
img_emp_users = ImageTk.PhotoImage(img_emp_users)

add_empp = Button(frame_left, image=img_emp_users, compound=LEFT, anchor=NW, text="Realizar Emprestimo", bg=b11, fg=b2, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE  )
add_empp .grid(row=4, column=0, sticky=NSEW, padx=5, pady=6 )

#devolucao emp
img_dev_emp = Image.open('livro/icons/return.png')
img_dev_emp = img_dev_emp.resize((18,18 ))
img_dev_emp = ImageTk.PhotoImage(img_dev_emp)

#emprestados 
add_devolution  =  Button(frame_left, image=img_dev_emp, compound=LEFT, anchor=NW, text="Adicionar Data Devolução", bg=b11, fg=b2, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
add_devolution.grid(row=5 ,column=0, padx=5, pady=6)


img_show_emp = Image.open('livro/icons/livro.png')
img_show_emp = img_show_emp.resize((18,18 ))
img_show_emp = ImageTk.PhotoImage(img_show_emp)


show_libres_emp  =  Button(frame_left, image=img_show_emp, compound=LEFT, anchor=NW, text="Exibir Livros emprestados", bg=b11, fg=b2, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
show_libres_emp.grid(row=6 ,column=0, padx=5, pady=6)
janela.mainloop()

