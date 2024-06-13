
from tkinter import *
import random

class Batallas():                      # En proseso

  def __init__(self,ventana,vida,fuerza,mana,oro):
    self.ventana=ventana
    self.vida=vida
    self.fuerza=fuerza
    self.mana=mana
    self.oro=oro
    self.estadisticas=Label(self.ventana,text="",bg="black",fg="white")
    self.estadisticas.place(x=255,y=460)
 
  def enemigo_ram(self):
    enemigo_aleatorio = random.randint(1, 100)
    if 1 <= enemigo_aleatorio <=20:
      return "slime1"
    elif 21 <= enemigo_aleatorio <=40:
      return "slime2"
    elif 41 <=enemigo_aleatorio <=60:
      return "slime3"
    elif 61 <= enemigo_aleatorio <=75:
      return "lobo"
    elif 76 <= enemigo_aleatorio <=90:
      return "lobo2"
    else:
      return "duende1"

  def Actualiza_Est(self):
    #if self.vida ==0:
    #  self.g_o=PhotoImage(file="C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\T_0.png")
    #  self.fin = Label(self.ventana, image=self.g_o, bg="red")
    #  self.fin.place(x=249,y=64)
    #  self.estadisticas.config(text=f"Vida: {self.vida}   Fuerza: {self.fuerza}   Mana: {self.mana}  Oro: {self.oro}") 
    #else:
    self.estadisticas.config(text=f"Vida: {self.vida}   Fuerza: {self.fuerza}   Mana: {self.mana}  Oro: {self.oro}") 


class Vendedor():                      # Ignorar de mientras <----------------X
  def __init__(self,ventana,oro):
    self.ventana=ventana
    self.oro=oro
    self.vend = PhotoImage(file="C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\vendedor.png")
    self.vende = Label(self.ventana, image=self.vende, bg="black")
    self.vende.place(x=260,y=150)

  def comprar(self):
    self.oro
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Eleccion():
  
  def __init__(self,ventana):

    self.ventana=ventana
    self.jugador="" # str vacio que despues tomara el nombre de la imagen del personaje
    self.per=False  # Estos dos comprobaran si ya se eligio un nombre y un personaje
    self.nom=False
    
    self.vida=0    # son las estadisticas que se modificaran
    self.fuerza=0
    self.mana=0
    self.oro=10
    self.color_j="Green" # Colñor del contorno del enemigo y del jugador
    self.color_e="Green"
    self.entorno=PhotoImage(file="") #cambia el ambiente
    self.dialogo=Label(self.ventana,text="",bg="black",fg="white") # cambia el dialogo
    self.dialogo.place(x=255,y=360)
    self.el_nombre=""

  def pri_ataque(self,q,sli_b,jugad):# primer ataque introductoria (Tutorial)
    self.destructor(q)
    self.dialogo.config(text="- Agotado, solo fuiste capas de usar tus puños.\n\n\n\n\nPuños: Fuerza/2                                                ")
    self.dialogo.place(x=255,y=360)
    self.A0 = PhotoImage(file=self.imagen("ataque0"))
    puño=Button(self.ventana,image=self.A0,bg="red",command= lambda: self.pri_putatazo(sli_b,jugad,puño))
    puño.place(x=280,y=390)
  
  def pri_putatazo(self,sli_b,jugad,p):
    self.destructor(p)
    self.color_e="orange"
    sli_b.config(bg=self.color_e)
    jugad.config(bg=self.color_e)
    self.vida-=30
    estan=Batallas(self.ventana,self.vida,self.fuerza,self.mana,self.oro) 
    estan.Actualiza_Est()
    intro_flec=Label(self.ventana,text="  <- Toma una poción para recuperarte.",bg="black",fg="white")
    intro_flec.place(x=475,y=404)
    self.dialogo.config(text="- Tras atacar, tambien te han dañado.")
    self.dialogo.place(x=255,y=360) 
    poci=Button(self.ventana,text="Pociones",bg="green",fg="white",command= lambda: self.pri_poci(intro_flec,poci,jugad,sli_b))
    poci.place(x=415,y=405)

  def pri_poci(self,q,e,jugad,sli_b):# Pocion introductoria (Tutorial)
    self.destructor(q,e)
    bb="                                                                                                               "
    self.dialogo.config(text=f"- Toma una poción para recuperar tu vida (Al tomar una poción no sederas el turno).\n\n\n\n\nVida: +30{bb}")
    self.dialogo.place(x=255,y=360)
    self.Pr = PhotoImage(file=self.imagen("poci1"))
    P_r=Button(self.ventana,image=self.Pr,bg="green",fg="white",command= lambda: self.pri_pocion(P_r,jugad,sli_b))
    P_r.place(x=295,y=390)

  def pri_pocion(self,x,jugad,sli_b):# primera pocion introductoria (Tutorial)
    self.destructor(x)
    self.color_j="green"
    jugad.config(bg=self.color_j)
    self.vida+=30
    estan=Batallas(self.ventana,self.vida,self.fuerza,self.mana,self.oro) 
    estan.Actualiza_Est()
    self.dialogo.config(text="- Intenta escapar (Dependiendo del enemigo habra mas o menos pocibilidades de escapar).")
    self.dialogo.place(x=255,y=360) 
    escape=Button(self.ventana,text="Escapar",bg="blue",fg="white",command= lambda: self.pri_escape(escape,jugad,sli_b))
    escape.place(x=530,y=405)

  def pri_escape(self,w,e,r):# Escapar (Tutorial)
    self.destructor(w,e,r)
    self.entorno.config(file=self.imagen("intermedio"))
    self.dialogo.config(text="- Por el momento dirigete con el vendedor y compra algunas pociones.")
    self.dialogo.place(x=255,y=360)
    ven=Button(self.ventana,text="Vendedor",bg="orange",fg="white",command= lambda: self.tienda(ven))
    ven.place(x=415,y=405)

  def tienda(self,*x): # Posiblemente esto se separe para ser una classe en si mismo
    for e in x:
      e.destroy()
    self.entorno.config(file=self.imagen("vendedor"))
    self.dialogo.config(text=f"- Vendedor: ¡Saludos {self.el_nombre}! No te he visto por un tiempo ¿Que compraras?")
    armi=Button(self.ventana, text="Pociones",bg="orange",fg="white",command= lambda: self.com_poci(armi,poc,atra1))
    armi.place(x=415,y=405)
    poc=Button(self.ventana, text="Armas",bg="orange",fg="white",command= lambda: self.com_arma(armi,poc,atra1))
    poc.place(x=315,y=405)
    atra1=Button(self.ventana,text="Atras",bg="orange",fg="white",command= lambda:self.intermedio(atra1,armi,poc))
    atra1.place(x=710,y=455)
  
  def com_poci(self,q,w,e):
    self.destructor(q,w,e)
    self.dialogo.config(text="- Buscas pociones ¡Gran eleccion! (Solo puedes llebar tres a la vez.)")
    # Pociones
    q1="Poci. Vida                     Poci. Mana                   Poci. Daño         "
    q2="Costo:5 Oro                 Costo:2 Oro                  Costo:10 Oro    "
    q3="+30 Vida                        +5 Mana                      -50 Vida Enemiga"
    descri1=Label(self.ventana,text=f"{q1}\n{q2}\n{q3}",bg="black",fg="white")
    descri1.place(x=305,y=390)
    self.P1 = PhotoImage(file=self.imagen("poci1"))
    Po1=Button(self.ventana,image=self.P1,bg="green",fg="white") # <-------------- Comando
    Po1.place(x=265,y=390)
    self.P2 = PhotoImage(file=self.imagen("poci2"))
    Po2=Button(self.ventana,image=self.P2,bg="green",fg="white") # <-------------- Comando
    Po2.place(x=385,y=390)
    self.P3 = PhotoImage(file=self.imagen("poci3"))
    Po3=Button(self.ventana,image=self.P3,bg="green",fg="white") # <-------------- Comando
    Po3.place(x=500,y=390)
    atra2=Button(self.ventana,text="Atras",bg="orange",fg="white",command= lambda: self.tienda(atra2,Po1,Po2,Po3,descri1))
    atra2.place(x=710,y=455)

  def com_arma(self,q,w,e):
    self.destructor(q,w,e)
    self.dialogo.config(text="- Adelante escoje una (Solo puedes llebar dos a la vez.)")
    #Armas
    w1="                       Barita del poder                         Espada superior                          Arco de guerra"
    w2="                    Costo: 20 Oro                             Costo: 25 Oro                             Costo: 20 Oro"
    w3="+10 Mana +5 fuerza                  +5 Mana +20 fuerza                +5 Mana +10 fuerza"
    descri2=Label(self.ventana,text=f"{w1}\n{w2}\n\n{w3}",bg="black",fg="white")
    descri2.place(x=265,y=390)
    self.A1 = PhotoImage(file=self.imagen("arma1"))          
    Ar1=Button(self.ventana,image=self.A1,bg="green",fg="white") # <-------------- Comando
    Ar1.place(x=265,y=390)
    self.A2 = PhotoImage(file=self.imagen("arma2"))             
    Ar2=Button(self.ventana,image=self.A2,bg="green",fg="white") # <-------------- Comando
    Ar2.place(x=425,y=390)
    self.A3 = PhotoImage(file=self.imagen("arma3"))             
    Ar3=Button(self.ventana,image=self.A3,bg="green",fg="white") # <-------------- Comando
    Ar3.place(x=583,y=390)
    atra3=Button(self.ventana,text="Atras",bg="orange",fg="white",command= lambda: self.tienda(atra3,Ar1,Ar2,Ar3,descri2))
    atra3.place(x=710,y=455)

  def intermedio(self,*x):
    for e in x:
      e.destroy()
    self.entorno.config(file=self.imagen("intermedio"))
    self.dialogo.config(text="- A donde ir...")
    vende=Button(self.ventana,text="Vendedor",bg="orange",fg="white",command= lambda: self.tienda(vende,bosq))
    vende.place(x=415,y=405)
    bosq=Button(self.ventana,text="Bosque",bg="orange",fg="white",command= lambda: self.batalla(bosq,vende))
    bosq.place(x=315,y=405)

  def batalla(self,q,w):
    self.destructor(q,w)
    atac=Button(self.ventana,text="Atacar",bg="red",fg="white")# <----------------comando X
    atac.place(x=300,y=405) 
    poci=Button(self.ventana,text="Pociones",bg="green",fg="white")# <----------------comando X
    poci.place(x=415,y=405)
    escape=Button(self.ventana,text="Escapar",bg="blue",fg="white")# <----------------comando X
    escape.place(x=530,y=405)
    self.entorno.config(file=self.imagen("bosque"))
    self.ento = Label(self.ventana, image=self.entorno, bg="black")
    self.ento.place(x=249,y=64)

    self.juga = PhotoImage(file=f"C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\{self.jugador}.png")
    ju= Label(self.ventana, image=self.juga, bg=self.color_j)
    ju.place(x=605,y=150)
    
    self.color_e="green"
    estan=Batallas(self.ventana,self.vida,self.fuerza,self.mana,self.oro) 
    enemi=estan.enemigo_ram()
    self.dialogo.config(text=f"- Un {enemi} se dispone a pelear. Pelea o huye.")
    self.sl_1 = PhotoImage(file=self.imagen(enemi))
    sli_1b = Label(self.ventana, image=self.sl_1, bg=self.color_e)
    sli_1b.place(x=260,y=150)

  # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  def tr(self,a,s,d): # destrulle al boton, la imagen y el label inicial
    self.destructor(a,s,d)

    self.entorno.config(file=self.imagen("T_1")) 
    tras_1 = Label(self.ventana, image=self.entorno, bg="black")
    tras_1.place(x=249,y=64)

    qq="-Sin embargo, en una de sus primeras aventuras se toparían con un inesperado y poderoso"
    ww=" ogro. El cual secuestraria a dos integrantes del equipo…¡Menos a ti aventurero!                    "
    self.dialogo.config(text=f"{qq}\n{ww}")
    self.dialogo.place(x=255,y=360)

    cont2=Button(self.ventana,text="Continuar >>>",bg="orange",fg="white",command= lambda: self.nom_per(cont2,tras_1)) # segundo continuar
    cont2.place(x=650,y=450)


  def nom_per(self,y,z):
    self.destructor(y,z) # destrulle el boton, la imagen y la introduccion prebia

    # Instrucciones iniciales
    tem="caracteres como máximo y uno mínimo.                                                                                 "
    iniciacion1_0=Label(self.ventana,text="- Elija a su personaje aventurero (No podrás cambiarlo después).",bg="black",fg="white") 
    iniciacion1_0.place(x=255,y=70)                                                                                         
    self.dialogo.config(text=f"- Indique su nombre aventurero (No podrás cambiarlo después). El nombre debe tener 15 \n{tem}")
    self.dialogo.place(x=255,y=360) 

    # Ingreso del nombre:
    nombre=Entry(self.ventana) 
    nombre.place(x=410,y=450)
    nom=Button(self.ventana,text="Aceptar",bg="orange",fg="white",command=lambda: self.Nombre(nombre,nombre,nom))
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
    magico = Label(self.ventana, image=self.ima_mago,bg="black")
    magico.place(x=270,y=100)
    caballero=Button(self.ventana,text= "Caballero",bg="orange",fg="white",command= lambda: self.Personaje(iniciacion1_0,descripcion,mago,caballero,arquero,magico,fuerte,velos,2))
    caballero.place(x=470,y=300)
    self.ima_caba = PhotoImage(file=self.imagen("caballero1")) 
    fuerte = Label(self.ventana, image=self.ima_caba,bg="black")
    fuerte.place(x=435,y=100)
    arquero=Button(self.ventana,text= "Arquero",bg="orange",fg="white",command= lambda: self.Personaje(iniciacion1_0,descripcion,mago,caballero,arquero,magico,fuerte,velos,3))
    arquero.place(x=635,y=300)
    self.ima_arqu = PhotoImage(file=self.imagen("Arquero1")) 
    velos = Label(self.ventana, image=self.ima_arqu,bg="black")
    velos.place(x=600,y=100)

  def destructor(self,*x): # Destrulle todo lo que le entra
    for e in x:
      e.destroy()

  def Nombre(self,nombre,y,t): # Introduce un nombre 
    e=nombre.get() # se guarda lo escrito en el Entry
    lx=len(e)
 
    if e=="ControlMaestro crq":
      self.destructor(y,t)
      bo1=Button(self.ventana,text="Intermedio",command=lambda: self.intermedio())
      bo1.place(x=800,y=100)
      self.oro+=90
      estan=Batallas(self.ventana,self.vida,self.fuerza,self.mana,self.oro)
      estan.Actualiza_Est()
    elif lx>=16:
      pass
    elif lx>=1:
      nombresito=Label(self.ventana,text=e,bg="black",fg="white")
      nombresito.place(x=10,y=12)
      self.destructor(y,t)
      self.nom=True # self.nom se combierte de False a True
      self.el_nombre=e
      self.pri_lucha()

  def pri_lucha(self):# Lucha introductoria (Tutorial)

    if self.nom and self.per:
       
      estan=Batallas(self.ventana,self.vida,self.fuerza,self.mana,self.oro) 
      estan.Actualiza_Est()
 
      self.entorno.config(file=self.imagen("bosque"))
      self.ento = Label(self.ventana, image=self.entorno, bg="black")
      self.ento.place(x=249,y=64)

      self.sl_b = PhotoImage(file=self.imagen("slime2"))
      sli_b = Label(self.ventana, image=self.sl_b, bg=self.color_e)
      sli_b.place(x=260,y=150)
      self.jug = PhotoImage(file=f"C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\{self.jugador}.png")
      jugad = Label(self.ventana, image=self.jug, bg=self.color_j)
      jugad.place(x=605,y=150)

      self.dialogo.config(text="- Intentando escapar del bosque un slime se interpone en tu camino.\n\n\n<- Defiendete con un ataque")
      self.dialogo.place(x=255,y=360) 
      atac=Button(self.ventana,text="Atacar",bg="red",fg="white",command= lambda: self.pri_ataque(atac,sli_b,jugad))
      atac.place(x=300,y=405)

    else:
      pass

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
    self.f=""
    self.f=x
    return f"C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\{x}.png"

# self= se referencia a si mismo
# .confing(x)= modifica el elemento de un Label
# place(x=,y=)= ubicasion (boton, imagen)
# command= definir el metodo con el que esta asosiado el boton (que hace al apretarlo)
# lambda:  se utiliza junto al command (command= lambda:), sirve para operaciones pequeñas o rapidas (ejem  command= lambda: 2+2)

# bg= color de fondo
# fg= color de letras