from tkinter import *

class Z:

    def __init__(self, ven):
        self.ven = ven
        self.eleccion = ""
        self.bobo = None

    def btn(self, b, e):
        e.destroy()
        b.destroy()

        lala = Label(self.ven, text="remplazo")
        lala.place(x=45, y=75)

        self.bobo = Button(self.ven, text="Elimina2", command=lambda: self.destructor(lala, self.bobo)) 
        self.bobo.place(x=45, y=45)

    def destructor(self, *x):
        for e in x:
            e.destroy()

        # Verifica si 'bobo' ha sido eliminado
        if not self.bobo.winfo_exists():
            ff = Label(self.ven, text="funciona")
            ff.place(x=10, y=10)