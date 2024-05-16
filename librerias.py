
from tkinter import *

class Eleccion:
  
  def __init__(self,ventana):
    self.ventana=ventana
    self.imagen_fondo = PhotoImage(file=f"C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\pared.png")
    self.primer_fondo = Label(ventana, image=self.imagen_fondo)
    self.primer_fondo.place(x=0, y=0)
    self.f=""
    self.cont2=None

  def tr(self,a,s):
    self.destructor(a,s)
    qq="-Sin embargo, en una de sus primeras aventuras se toparían con un inesperado y poderoso"
    ww=" ogro. El cual secuestraria a dos integrantes del equipo…¡Menos a ti aventurero!                    "
    iniciacion0_1=Label(self.ventana,text=f"{qq}\n{ww}",bg="black",fg="white")
    iniciacion0_1.place(x=255,y=360)

    self.cont2=Button(self.ventana,text="Continuar >>>",bg="orange",fg="white",command= lambda: self.nom_per(iniciacion0_1,self.cont2))
    self.cont2.place(x=650,y=450)


  def nom_per(self,*x):
    for e in x:
      e.destroy()

    if not self.cont2.winfo_exists():
        # Instrucciones iniciales
        iniciacion1_0=Label(self.ventana,text="- Elija a su personaje aventurero (No podras cambiarlo despues).",bg="black",fg="white")
        iniciacion1_0.place(x=255,y=70)
        iniciacion1_1=Label(self.ventana,text="- Indique su nombre aventurero (No podras cambiarlo despues).",bg="black",fg="white")
        iniciacion1_1.place(x=255,y=360) 

        # Ingreso del nombre:
        nombre=Entry(self.ventana) 
        nombre.place(x=410,y=450)
        nom=Button(self.ventana,text="aceptar",bg="orange",fg="white",command=lambda: self.Nombre(nombre,iniciacion1_1,nombre,nom))
        nom.place(x=520,y=448)

        # eleccion de personaje:
        des_v=" Vida:  90                                          Vida:  120                                       Vida:  100"
        des_f="  Fuerza:  15                                      Fuerza:  50                                     Fuerza:  25"
        des_m="Mana:  25                                        Mana:  5                                        Mana:  10"
        descripcion=Label(self.ventana,text=f"{des_v}\n{des_f}\n{des_m}",bg="black",fg="white")
        descripcion.place(x=255,y=235)
        mago=Button(self.ventana,text= "Mago",bg="orange",fg="white",command= lambda: self.Personaje(iniciacion1_0,descripcion,mago,caballero,arquero,magico,fuerte,velos,1))
        mago.place(x=315,y=300)
        self.ima_mago = PhotoImage(file="C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\Maga1.png") 
        magico = Label(self.ventana, image=self.ima_mago)
        magico.place(x=270,y=100)
        caballero=Button(self.ventana,text= "Caballero",bg="orange",fg="white",command= lambda: self.Personaje(iniciacion1_0,descripcion,mago,caballero,arquero,magico,fuerte,velos,2))
        caballero.place(x=470,y=300)
        self.ima_caba = PhotoImage(file="C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\caballero1.png") 
        fuerte = Label(self.ventana, image=self.ima_caba)
        fuerte.place(x=435,y=100)
        arquero=Button(self.ventana,text= "Arquero",bg="orange",fg="white",command= lambda: self.Personaje(iniciacion1_0,descripcion,mago,caballero,arquero,magico,fuerte,velos,3))
        arquero.place(x=635,y=300)
        self.ima_arqu = PhotoImage(file="C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\Arquero1.png") 
        velos = Label(self.ventana, image=self.ima_arqu)
        velos.place(x=600,y=100)


    

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
    