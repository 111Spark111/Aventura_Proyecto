import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Pestañas con Tkinter")

# Crear un widget Notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# Crear dos frames que serán las pestañas
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

# Añadir los frames al Notebook como pestañas
notebook.add(tab1, text='Pestaña 1')
notebook.add(tab2, text='Pestaña 2')

# Añadir contenido a las pestañas
label1 = tk.Label(tab1, text="Contenido de la Pestaña 1")
label1.pack(pady=20, padx=20)

label2 = tk.Label(tab2, text="Contenido de la Pestaña 2")
label2.pack(pady=20, padx=20)

root.mainloop()
"""from tkinter import *
from z import*

def mai():
    ven = Tk()
   
    y=1
    d="red"
    x=Label(ven,text=y,bg=d)
    x.place(x=0,y=0)
    tt=PhotoImage(file="C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\poci1.png")
    b=Button(ven,image=tt,command= lambda: cam(y,d))
    b.place(x=0,y=30)
    t=Button(ven,text="0",command= lambda: zero(y))
    t.place(x=0,y=60)

    def cam(y,d):
        d="blue"
        y+=2
        x.config(text=y,bg=d)

    def zero(y):
        y=0
        x.config(text=y)

    ven.mainloop()

if __name__ == "__main__":
    mai()
    """