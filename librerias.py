
from tkinter import *

class Eleccion:
  
  def __init__(self,ventana):
    self.ventana=ventana
    self.imagen_fondo = PhotoImage(file=f"C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\pared.png")
    self.primer_fondo = Label(ventana, image=self.imagen_fondo)
    self.primer_fondo.place(x=0, y=0)
    self.f=""

  def tr(self,a,s):
    self.destructor(a,s)
    qq="-Sin embargo, en una de sus primeras aventuras se toparían con un inesperado y poderoso"
    ww=" ogro. El cual secuestraria a dos integrantes del equipo…¡Menos a ti aventurero!                    "
    iniciacion0_1=Label(self.ventana,text=f"{qq}\n{ww}",bg="black",fg="white")
    iniciacion0_1.place(x=255,y=360)
    cont2=Button(self.ventana,text="Continuar >>>",bg="orange",fg="white",command= lambda: self.destructor(iniciacion0_1,cont2))
    cont2.place(x=650,y=450)

  def destructor(self,*x): # Destrulle todo lo que le entra
     for e in x:
         e.destroy()     

  def Fondo(self,fon,primer_fondo): # Cambia el fondo
    self.destructor(primer_fondo)
    self.f=fon

    self.imagen_fondo = PhotoImage(file=f"C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\{fon}.png")
    self.primer_fondo.config(image=self.imagen_fondo)

    if self.f == "pared":
      self.primer_fondo.place(x=0, y=0)

    elif self.f == "cielo":
      self.primer_fondo.place(x=0, y=0)

    elif self.f == "noche":
      self.primer_fondo.place(x=0, y=0)

    else:
      self.primer_fondo.place_forget()
    

  def Nombre(self,nombre,z,y,t): # Introduce un nombre 
    e=nombre.get()
    lx=len(e)
    reintento=Label(self.ventana,text="- ¡El nombre debe tener 15 caracteres como maximo y uno minimo!        ",bg="black",fg="white")
    f=reintento.place(x=255,y=360)

    if lx>=16:
      return f
    elif lx>=1:
      nom=Label(self.ventana,text=e,bg="black",fg="white")
      nom.place(x=10,y=12)
      self.destructor(z,y,t)
      if reintento:
        parche=Label(self.ventana,text="________________________________________________________________________",bg="black",fg="black")
        parche.place(x=255,y=360)
  
  def Personaje(self,q,w,e,r,t,y,u,i,el_personaje):
    mag="/ Mago"
    cab="/ Caballero"
    arq="/ Arquero"
    if el_personaje==1:
      per_elejido=Label(self.ventana,text=mag,bg="black",fg="white")
      per_elejido.place(x=120,y=12)
    elif el_personaje==2:
      per_elejido=Label(self.ventana,text=cab,bg="black",fg="white")
      per_elejido.place(x=120,y=12)
    else:
      per_elejido=Label(self.ventana,text=arq,bg="black",fg="white")
      per_elejido.place(x=120,y=12)
    self.destructor(q,w,e,r,t,y,u,i)



class Jugador:
  def __init__(self,vida,fuerza,mana):
    self.vida=vida
    self.fuerza=fuerza
    self.mana=mana
  

    