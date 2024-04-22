
from tkinter import *

class Eleccion:
  def __init__(self):#<-------------X
      pass

  def Si(self):
   eliminar=[] #Lista bacia para eliminar los Label
   for i in eliminar:
        i.destroy()
   eliminar.clear()
   zz=Label(self.ventana, text="si funciona",bg="black",fg="white")
   zz.place(x=470,y=350)
   eliminar.append(zz)

  def No(self):
   eliminar=[]
   for i in eliminar:
        i.destroy()
   eliminar.clear()
   yy=Label(self.ventana, text="no funciona",bg="black",fg="white")
   yy.place(x=470,y=350)
   eliminar.append(yy)
    

  def temporal(self,e):# <------------------X
    x=0
    while x!=1 : 
     numnom=len(e)
     if numnom >= 15:
      print("Perdon. El nombre debe tener maximo 15 caracteres.") 
      e=str(input("        -> "))
     else:
       x=1
    return e
  
  def Nombre(self,nombre):
    x=nombre.get()
    nm=Label(text=f"{x}",fg="white",bg="grey")
    nm.place(x=5,y=10)
  
