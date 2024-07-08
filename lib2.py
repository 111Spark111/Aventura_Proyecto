from tkinter import PhotoImage,Label,Button 
class Fondo():                                #aplicar herencia despues<----------------------X
    def __init__(self,ventana):
      self.imagen_fondo = PhotoImage(file="C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\pared.png")
      self.primer_fondo = Label(ventana, image=self.imagen_fondo)
      self.primer_fondo.place(x=0, y=0)
      self.f=""

    def fondos(self,fon): # Cambia el fondo
      self.f=fon
      self.imagen_fondo = PhotoImage(file=f"C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\{fon}.png")
      self.primer_fondo.config(image=self.imagen_fondo)
      self.primer_fondo.place(x=0, y=0)

class Ayuda():
   def __init__(self,ventana):
      self.ventana=ventana
      self.pant=True
      self.don=2
   
   def la_guia(self):   # coloca las pantallas de ayuda con los datos enemigos y de equipamiento
      if self.pant==True: # muestra datos si es true
         self.panta1 = PhotoImage(file=f"C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\pantalla.png")
         self.pantalla1 = Label(self.ventana, image=self.panta1,bg="grey")
         self.pantalla1.place(x=0, y=50)

         self.des1=Label(self.ventana,text="Ataques información:                  \n\n                          Puños                     \n                      Daño: Fuerza/2",bg="black",fg="white")# agragar mas
         self.des1.place(x=10, y=60)
         self.im1=PhotoImage(file="C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\ataque0.png")
         self.im11=Label(self.ventana,image=self.im1,bg="black")
         self.im11.place(x=50, y=85)

         self.im2=PhotoImage(file="C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\ataque01.png")
         self.im22=Label(self.ventana,image=self.im2,bg="black")
         self.im22.place(x=50, y=135)
         self.des21=Label(self.ventana,text="Baston Magico\nDaño: 60          \nCosto: -2 Mana",bg="black",fg="white")
         self.des21.place(x=88, y=130)

         self.im3=PhotoImage(file="C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\ataque02.png")
         self.im33=Label(self.ventana,image=self.im3,bg="black")
         self.im33.place(x=50, y=195)
         self.des3=Label(self.ventana,text="Espara Corta\nDaño: Fuerza",bg="black",fg="white")
         self.des3.place(x=88, y=190)

         self.im4=PhotoImage(file="C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\ataque03.png")
         self.im44=Label(self.ventana,image=self.im4,bg="black")
         self.im44.place(x=50, y=255)
         self.des4=Label(self.ventana,text="Flecha Veloz            \nDaño: Fuerza+Mana\nCosto: -1 Mana         ",bg="black",fg="white")
         self.des4.place(x=88, y=240)

         self.im5=PhotoImage(file="C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\ataque1.png")
         self.im55=Label(self.ventana,image=self.im5,bg="black")
         self.im55.place(x=50, y=315)
         self.des5=Label(self.ventana,text="Relampago            \nDaño: Mana*7      \nCosto: *Mana         ",bg="black",fg="white")
         self.des5.place(x=88, y=300)

         self.im6=PhotoImage(file="C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\ataque2.png")
         self.im66=Label(self.ventana,image=self.im6,bg="black")
         self.im66.place(x=50, y=375)
         self.des6=Label(self.ventana,text="Corte Valeroso            \nDaño: Vida-20           \nCosto: -5 Mana         ",bg="black",fg="white")
         self.des6.place(x=88, y=360)

         self.im7=PhotoImage(file="C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\ataque3.png")
         self.im77=Label(self.ventana,image=self.im7,bg="black")
         self.im77.place(x=50, y=435)
         self.des7=Label(self.ventana,text="Tiro Certero                \nDaño: Fuerza/2           \nCosto: -2 Oro             ",bg="black",fg="white")
         self.des7.place(x=88, y=420)
         #----------------------------------------------------------------------------------------------------------------------------------------------
         self.pantalla2 = Label(self.ventana, image=self.panta1,bg="grey")
         self.pantalla2.place(x=780, y=50)
         self.des2=Label(self.ventana,text="Enemigos información:",bg="black",fg="white")
         self.des2.place(x=790, y=60)

         self.im8=PhotoImage(file="C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\slime azul.png")
         self.im88=Label(self.ventana,image=self.im8,bg="grey")
         self.im88.place(x=863, y=100)
         self.des8=Label(self.ventana,text="Slime Azul\nVida: 100\nDaño: 10\n Oro: +5",bg="black",fg="white")
         self.des8.place(x=790, y=120)

         self.im9=PhotoImage(file="C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\slime verde.png")
         self.im99=Label(self.ventana,image=self.im9,bg="grey")
         self.im99.place(x=863, y=280)
         self.des9=Label(self.ventana,text="Slime Verde\nVida: 70\nDaño: 20\n Oro: +5",bg="black",fg="white")
         self.des9.place(x=790, y=300)

         #self.des10=Label(self.ventana,text="Slime Rojo\nVida: 100\nDaño: 20\n Oro: +7",bg="black",fg="white")
         #self.des10.place(x=790, y=340)

         self.continuar=Button(self.ventana,text="->",bg="black",fg="white",command= lambda: self.cambiar(self.im88,self.des8,self.im99,self.des9,"d"))
         self.continuar.place(x=968,y=450)
         self.atras=Button(self.ventana,text="<-",bg="black",fg="white",command= lambda: self.cambiar(self.im88,self.des8,self.im99,self.des9,"i"))
         self.atras.place(x=787,y=450)

         self.pant=False
      else: # desaparese los datos si es falce
         self.destructor(self.des1,self.des2,self.pantalla1,self.pantalla2,self.continuar,self.atras,self.im11)
         self.destructor(self.im22,self.im33,self.im44,self.im55,self.im66,self.im77,self.des3,self.des4,self.des5,self.des6,self.des7,self.des21)
         self.destructor(self.im88,self.des8,self.im99,self.des9)
         self.pant=True
   
   def cambiar(self,x,y,z,w,direc):
      if direc=="d":
         self.don+=1
      elif direc=="i":
         self.don-=1

      if self.don>3:
         self.don=1
      elif self.don<1:
         self.don=3
      else:
         pass
      
      if self.don==1:
         self.im01=PhotoImage(file="C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\lobo alfa.png")
         self.im02=PhotoImage(file="C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\duende.png")
         x.config(image=self.im01)
         y.config(text="Lobo Alfa\nVida: 100\nDaño:15 a 20\n Oro: +15")

         z.config(image=self.im02)
         w.config(text="Duende\nVida: 110\nDaño:10 a 25\n Oro: +20")
      elif self.don==2:
         self.im01=PhotoImage(file="C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\slime azul.png")
         self.im02=PhotoImage(file="C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\slime verde.png")
         x.config(image=self.im01)
         y.config(text="Slime Azul\nVida: 100\nDaño: 10\n Oro: +5")

         z.config(image=self.im02)
         w.config(text="Slime Verde\nVida: 70\nDaño: 20\n Oro: +5")
      else:
         self.im01=PhotoImage(file="C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\slime rojo.png")
         self.im02=PhotoImage(file="C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\lobo.png")
         x.config(image=self.im01)
         y.config(text="Slime Rojo\nVida: 100\nDaño: 20\n Oro: +7")

         z.config(image=self.im02)
         w.config(text="Lobo\nVida: 90\nDaño:10 a 20\n Oro: +10")
      

   def destructor(self,*x): # Destrulle todo lo que le entra
    for e in x:
      e.destroy()