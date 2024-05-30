
from tkinter import *

class Eleccion:
  
  def __init__(self,ventana):
    self.ventana=ventana
    self.f=""   #<------------------X
    self.estadisticas=Label(self.ventana,text="",bg="black",fg="white")     
    self.estadisticas.place(x=255,y=460)                             
    self.vida=0
    self.fuerza=0
    self.mana=0
    self.jugador=""
    self.per=False
    self.nom=False
  

  def tr(self,a,s,d):
    self.destructor(a,s,d)

    self.ima_T_1 = PhotoImage(file=self.imagen("T_1")) 
    tras_1 = Label(self.ventana, image=self.ima_T_1, bg="black")
    tras_1.place(x=249,y=64)

    qq="-Sin embargo, en una de sus primeras aventuras se toparían con un inesperado y poderoso"
    ww=" ogro. El cual secuestraria a dos integrantes del equipo…¡Menos a ti aventurero!                    "
    iniciacion0_1=Label(self.ventana,text=f"{qq}\n{ww}",bg="black",fg="white")
    iniciacion0_1.place(x=255,y=360)

    cont2=Button(self.ventana,text="Continuar >>>",bg="orange",fg="white",command= lambda: self.nom_per(iniciacion0_1,cont2,tras_1))
    cont2.place(x=650,y=450)


  def nom_per(self,x,y,z):
    self.destructor(x,y,z)

    # Instrucciones iniciales
    tem="caracteres como máximo y uno mínimo.                                                                                 "
    iniciacion1_0=Label(self.ventana,text="- Elija a su personaje aventurero (No podrás cambiarlo después).",bg="black",fg="white")
    iniciacion1_0.place(x=255,y=70)                                                                                                                                   #o--->
    iniciacion1_1=Label(self.ventana,text=f"- Indique su nombre aventurero (No podrás cambiarlo después). El nombre debe tener 15 \n{tem}",bg="black",fg="white")
    iniciacion1_1.place(x=255,y=360) 

    # Ingreso del nombre:
    nombre=Entry(self.ventana) 
    nombre.place(x=410,y=450)
    nom=Button(self.ventana,text="Aceptar",bg="orange",fg="white",command=lambda: self.Nombre(nombre,iniciacion1_1,nombre,nom))
    nom.place(x=520,y=448)

    # eleccion de personaje:
    des_v=" Vida:  90                                          Vida:  120                                       Vida:  100"
    des_f="  Fuerza:  15                                      Fuerza:  50                                     Fuerza:  30"
    des_m="Mana:  25                                        Mana:  5                                        Mana:  10"
    descripcion=Label(self.ventana,text=f"{des_v}\n{des_f}\n{des_m}",bg="black",fg="white")
    descripcion.place(x=255,y=235)
    mago=Button(self.ventana,text= "Mago",bg="orange",fg="white",command= lambda: self.Personaje(iniciacion1_0,descripcion,mago,caballero,arquero,magico,fuerte,velos,1))
    mago.place(x=315,y=300)
    self.ima_mago = PhotoImage(file=self.imagen("Maga1")) 
    magico = Label(self.ventana, image=self.ima_mago)
    magico.place(x=270,y=100)
    caballero=Button(self.ventana,text= "Caballero",bg="orange",fg="white",command= lambda: self.Personaje(iniciacion1_0,descripcion,mago,caballero,arquero,magico,fuerte,velos,2))
    caballero.place(x=470,y=300)
    self.ima_caba = PhotoImage(file=self.imagen("caballero1")) 
    fuerte = Label(self.ventana, image=self.ima_caba)
    fuerte.place(x=435,y=100)
    arquero=Button(self.ventana,text= "Arquero",bg="orange",fg="white",command= lambda: self.Personaje(iniciacion1_0,descripcion,mago,caballero,arquero,magico,fuerte,velos,3))
    arquero.place(x=635,y=300)
    self.ima_arqu = PhotoImage(file=self.imagen("Arquero1")) 
    velos = Label(self.ventana, image=self.ima_arqu)
    velos.place(x=600,y=100)

  def destructor(self,*x): # Destrulle todo lo que le entra
    for e in x:
      e.destroy()        

  def Nombre(self,nombre,z,y,t): # Introduce un nombre 
    e=nombre.get()
    lx=len(e)

    if lx>=16:
      pass
    elif lx>=1:
      nombresito=Label(self.ventana,text=e,bg="black",fg="white")
      nombresito.place(x=10,y=12)
      self.destructor(z,y,t)
      self.nom=True
      self.pri_lucha()

  
  def Personaje(self,q,w,e,r,t,y,u,i,el_personaje):

    if el_personaje==1:
      per_elejido=Label(self.ventana,text="/ Mago",bg="black",fg="white")
      per_elejido.place(x=120,y=12)
      self.vida+=90
      self.fuerza+=15
      self.mana+=25
      self.per=True
      self.jugador="Maga2"
     
    elif el_personaje==2:
      per_elejido=Label(self.ventana,text="/ Caballero",bg="black",fg="white")
      per_elejido.place(x=120,y=12)
      self.vida+=120
      self.fuerza=+50
      self.mana+=5
      self.per=True
      self.jugador="Caballero2"

    else:
      per_elejido=Label(self.ventana,text="/ Arquero",bg="black",fg="white")
      per_elejido.place(x=120,y=12)
      self.vida+=100
      self.fuerza+=30
      self.mana+=10
      self.per=True
      self.jugador="Arquero2"

    self.pri_lucha()  #x
    self.destructor(q,w,e,r,t,y,u,i)

  def pri_lucha(self):#-------------------------------------X

    if self.nom and self.per:

      self.estadisticas.config(text=f"Vida: {self.vida}   Fuerza: {self.fuerza}   Mana: {self.mana}")

      self.ima_bosque = PhotoImage(file=self.imagen("bosque")) 
      tras_1 = Label(self.ventana, image=self.ima_bosque, bg="black")
      tras_1.place(x=249,y=64)
      self.sl_b = PhotoImage(file=self.imagen("slime1"))
      sli_b = Label(self.ventana, image=self.sl_b, bg="black")
      sli_b.place(x=260,y=150)
      self.jug = PhotoImage(file=f"C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\{self.jugador}.png")
      jugad = Label(self.ventana, image=self.jug, bg="black")
      jugad.place(x=605,y=150)


      self.intro_atac=Label(self.ventana,text="- Intentando escapar del bosque un slime se interpone en tu camino.",bg="black",fg="white")
      self.intro_atac.place(x=255,y=360) 
      atac=Button(self.ventana,text="Atacar",bg="orange",fg="white") #<-----------Comand faltante
      atac.place(x=300,y=400)

    else:
      pass

  def imagen(self,x):
    self.f=x
    return f"C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\{x}.png"



class Fondo(): 
    def __init__(self,ventana):
      self.imagen_fondo = PhotoImage(file=f"C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\pared.png")
      self.primer_fondo = Label(ventana, image=self.imagen_fondo)
      self.primer_fondo.place(x=0, y=0)
      self.f=""

    def fondos(self,fon): # Cambia el fondo

      self.f=fon
      self.imagen_fondo = PhotoImage(file=f"C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\{fon}.png")
      self.primer_fondo.config(image=self.imagen_fondo)
      self.primer_fondo.place(x=0, y=0)



#  def Actualiza_Est(self):  # Clase jugador
#    self.estadisticas.config(text=f"vida:{self.vida} fuerza:{self.fuerza}  mana:{self.mana}")
    