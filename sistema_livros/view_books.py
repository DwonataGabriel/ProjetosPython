import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
import sqlite3

def create_tree_widget(root):
    columns = ('id', 'Título', 'Autor', 'Editor', 'Ano Publi.', 'ISBN') 
    tree = ttk.Treeview(root, columns=columns, show='headings')

  
    for col in columns:
        tree.heading(col, text=col.capitalize())

    tree.bind('<<TreeviewSelect>>', item_selected)
    tree.grid(row=0, column=0, sticky=tk.NSEW)
         

    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')

    return tree


   

def load_data_from_db(tree):
    conn = sqlite3.connect('dados.db')
    cursor = conn.cursor()
    livros = cursor.execute('SELECT * FROM livros').fetchall()
    conn.close()

    for item in tree.get_children():
        tree.delete(item)

    for livro in livros:
        tree.insert('', tk.END, values=livro)



def item_selected(event, tree):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        showinfo(title="teste", message=','.join(map(str, record)))

def main_books():
    root = tk.Tk()
    root.title("Livros Cadastrados")
    root.geometry('650x320')
    root.resizable(width=True, height=True)

    tree = create_tree_widget(root)
    load_data_from_db(tree)

    tree.bind('<<TreeviewSelect>>', lambda event: item_selected(event, tree))
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.mainloop()
    
if __name__ == '__main__':
    main_books()


 