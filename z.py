from tkinter import *

class Z:

    def __init__(self, ven):
        self.ven = ven
        self.eleccion = ""
        self.bobo = None


    def atras1(self,x):
        for e in x:
            e.destroy()
    def btn(self, bot, b,xx,yy):
        self.destructor(bot, b)

        lala = Label(self.ven, text="remplazo")
        lala.place(x=45, y=75)

        self.bobo = Button(self.ven, text="Elimina2", command=lambda: self.otro(lala, self.bobo,xx,yy)) 
        self.bobo.place(x=45, y=45)

    def destructor(self, *x):
        for e in x:
            e.destroy()

    def otro(self,t,u,xx,yy):
        self.destructor(t,u)

        self.bot1 = Button(self.ven, text="Elimina x", command=lambda: self.destructor(self.bot1,self.bot2,xx)) 
        self.bot1.place(x=45, y=45)

        self.bot2 = Button(self.ven, text="Elimina y", command=lambda: self.destructor(self.bot1,self.bot2,yy)) 
        self.bot2.place(x=45, y=65)



class T(Z):
    def __init__(self,ven,q,w,e):
        super 
        self.q=q
        self.w=w
        self.e=e

    def mos(self):
        return {self.q},{self.w},{self.e}