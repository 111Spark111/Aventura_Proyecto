
from tkinter import *

class Eleccion:
  
  def __init__(self,ventana):
    self.ventana=ventana
    self.f=""   #<------------------X
    self.estadisticas=Label(self.ventana,text="",bg="black",fg="white") # mustra las estadisticas
    self.estadisticas.place(x=255,y=460)                                # de momento bacias
    self.vida=0    # son las estadisticas que se modificaran
    self.fuerza=0
    self.mana=0
    self.jugador="" # str vacio que despues tomara el nombre de la imagen del personaje
    self.per=False  # Estos dos comprobaran si ya se eligio un nombre y un personaje
    self.nom=False

    self.color_j="Green"
    self.color_e="Green"
    self.daño=0

  def pri_lucha(self):# Lucha introductoria (Tutorial)

    if self.nom and self.per:

      self.estadisticas.config(text=f"Vida: {self.vida}   Fuerza: {self.fuerza}   Mana: {self.mana}") # las estadisticas se actualizan al personaje elejido

      self.ima_bosque = PhotoImage(file=self.imagen("bosque")) 
      tras_1 = Label(self.ventana, image=self.ima_bosque, bg="black")
      tras_1.place(x=249,y=64)
      self.sl_b = PhotoImage(file=self.imagen("slime2"))
      sli_b = Label(self.ventana, image=self.sl_b, bg=self.color_e)
      sli_b.place(x=260,y=150)
      self.jug = PhotoImage(file=f"C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\{self.jugador}.png")
      jugad = Label(self.ventana, image=self.jug, bg=self.color_j)
      jugad.place(x=605,y=150)

      self.intro_atac=Label(self.ventana,text="- Intentando escapar del bosque un slime se interpone en tu camino.\n\n\n<- Defiendete con un ataque.",bg="black",fg="white")
      self.intro_atac.place(x=255,y=360) 
      atac=Button(self.ventana,text="Atacar",bg="red",fg="white",command= lambda: self.pri_ataque(atac,self.intro_atac)) #<-----------Command faltante
      atac.place(x=300,y=405)

    else:
      pass

  def pri_ataque(self,q,w):
    bat=Batallas(90,30)
    self.destructor(q,w)
    puño=Button(self.ventana,text="   Puñetazo   ",bg="red",fg="white",command= lambda: bat.puñetazos())
    puño.place(x=265,y=370)
    mag=Button(self.ventana,text="Impacto magico",bg="red",fg="white")
    mag.place(x=370,y=370)
    if self.jugador=="Maga2":
      tem="Baston"
    elif self.jugador=="Caballero2":
      tem="Espada corta"
    else:
      tem="Flechas"
    arma=Button(self.ventana,text=f"   {tem}   ",bg="red",fg="white")
    arma.place(x=490,y=370)
    explic=Label(self.ventana,text="Ataque: Fuerza           Ataque: Mana x3          Ataque: Fuerza x2",bg="black",fg="white")
    explic.place(x=260,y=405)

  # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  def tr(self,a,s,d): # destrulle al boton, la imagen y el label inicial
    self.destructor(a,s,d)

    self.ima_T_1 = PhotoImage(file=self.imagen("T_1")) 
    tras_1 = Label(self.ventana, image=self.ima_T_1, bg="black")
    tras_1.place(x=249,y=64)

    qq="-Sin embargo, en una de sus primeras aventuras se toparían con un inesperado y poderoso"
    ww=" ogro. El cual secuestraria a dos integrantes del equipo…¡Menos a ti aventurero!                    "
    iniciacion0_1=Label(self.ventana,text=f"{qq}\n{ww}",bg="black",fg="white")
    iniciacion0_1.place(x=255,y=360)

    cont2=Button(self.ventana,text="Continuar >>>",bg="orange",fg="white",command= lambda: self.nom_per(iniciacion0_1,cont2,tras_1)) # segundo continuar
    cont2.place(x=650,y=450)


  def nom_per(self,x,y,z):
    self.destructor(x,y,z) # destrulle el boton, la imagen y la introduccion prebia

    # Instrucciones iniciales
    tem="caracteres como máximo y uno mínimo.                                                                                 "
    iniciacion1_0=Label(self.ventana,text="- Elija a su personaje aventurero (No podrás cambiarlo después).",bg="black",fg="white")
    iniciacion1_0.place(x=255,y=70)                                                                                         
    iniciacion1_1=Label(self.ventana,text=f"- Indique su nombre aventurero (No podrás cambiarlo después). El nombre debe tener 15 \n{tem}",bg="black",fg="white")
    iniciacion1_1.place(x=255,y=360) 

    # Ingreso del nombre:
    nombre=Entry(self.ventana) 
    nombre.place(x=410,y=450)
    nom=Button(self.ventana,text="Aceptar",bg="orange",fg="white",command=lambda: self.Nombre(nombre,iniciacion1_1,nombre,nom))
    nom.place(x=520,y=448)

    # eleccion de personaje:
    des_v=" Vida:  90                                          Vida:  120                                       Vida:  100"
    des_f="  Fuerza:  20                                      Fuerza:  40                                     Fuerza:  30"
    des_m="Mana:  20                                        Mana:  5                                        Mana:  10"
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
    e=nombre.get() # se guarda lo escrito en el Entry
    lx=len(e)
 
    if lx>=16:
      pass
    elif lx>=1:
      nombresito=Label(self.ventana,text=e,bg="black",fg="white")
      nombresito.place(x=10,y=12)
      self.destructor(z,y,t)
      self.nom=True # self.nom se combierte de False en True
      self.pri_lucha()

  
  def Personaje(self,q,w,e,r,t,y,u,i,el_personaje):

    if el_personaje==1:
      per_elejido=Label(self.ventana,text="/ Mago",bg="black",fg="white")
      per_elejido.place(x=120,y=12)
      self.vida+=90
      self.fuerza+=15  # se cambian visa,fuerza,mana, self.per se buelbe True y self.jugador el nombre de la imagen del personaje
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

    self.pri_lucha()
    self.destructor(q,w,e,r,t,y,u,i)

  def imagen(self,x): # Acorta la llamada de los png´s
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


class Batallas():

  def __init__(self,vid_e,daño_e):
    self.vida=0                         # son las estadisticas que se modificaran
    self.fuerza=0
    self.mana=0
    self.color_j="Green"
    self.color_e="Green"
    self.daño=0
    self.vid_e=vid_e
    self.vid_cop=vid_e
    self.daño_e=daño_e
  
  def puñetazos(self):
    self.daño = self.fuerza
    self.vid_e-=self.daño
    self.vida_enemiga()

  def vida_enemiga(self):
    if self.vid_e <= self.vid_cop/3:
      self.color_e="red"
    elif self.vid_e <= self.vid_cop/2:
      self.color_e="orange"
    else:
      pass
    

  def Actualiza_Est(self):  # Clase jugador
    self.estadisticas.config(text=f"vida:{self.vida} fuerza:{self.fuerza}  mana:{self.mana}") 


# self= se referencia a si mismo
# .confing(x)= modifica el elemento de un Label
# place(x=,y=)= ubicasion (boton, imagen)
# command= definir el metodo con el que esta asosiado el boton (que hace al apretarlo)
# lambda:  se utiliza junto al command (command= lambda:), sirve para operaciones pequeñas o rapidas (ejem  command= lambda: 2+2)

# bg= color de fondo
# fg= color de letras