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
      self.tf=True
   
   def la_guia(self): # coloca las pantallas de ayuda con los datos enemigos y de equipamiento
      continuar=Button(self.ventana,text="->",bg="black",fg="white")
      atras=Button(self.ventana,text="<-",bg="black",fg="white")
      if self.tf==True: # muestra datos si es true
         self.panta1 = PhotoImage(file=f"C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\pantalla.png")
         self.pantalla1 = Label(self.ventana, image=self.panta1,bg="grey")
         self.pantalla1.place(x=0, y=50)
         self.pantalla2 = Label(self.ventana, image=self.panta1,bg="grey")
         self.pantalla2.place(x=780, y=50)


         continuar.place(x=968,y=450)
   
         atras.place(x=787,y=450)

         self.tf=False
      else: # desaparese los datos si es falce
         self.pantalla1.destroy()
         self.pantalla2.destroy()
         continuar.destroy()
         atras.destroy()
         self.tf=True