from tkinter import *
from librerias import Eleccion
ventana=Tk()
 
ventana.title("Aventura 0.01")#Nombre de ventana
ventana.geometry("1000x500")#tamano al abrirce

ventana.iconbitmap("C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\escudo.ico")# Temporal-icono

f1="pared2.png"#---->def despues
f2="cielo.png"#-->def despues
f3="noche.png"#-->def despues
imagen_fondo = PhotoImage(file=f"C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\{f2}") #creo un fondo/solo funciona en este dispocitivo <-X
Fondo = Label(ventana, image=imagen_fondo) #<-------------X
Fondo.place(x=0, y=0)

jugador=Eleccion()# Instancia 

iniciacion1=Label(ventana,text="> Elija a su personaje aventurero (No podras cambiarlo despues).",bg="black",fg="white") # <--- eliminar esto despues de apretar aceptar
iniciacion1.place(x=255,y=110)
iniciacion2=Label(ventana,text="- Indique su nombre aventurero (No podras cambiarlo despues).",bg="black",fg="white") # <--- eliminar esto despues de apretar aceptar
iniciacion2.place(x=255,y=360)
nombre=Entry(ventana) #<----- trabajar con nombre(e)
nombre.place(x=410,y=450)
nom=Button(ventana,text="aceptar",bg="orange",fg="white",command=jugador.Nombre) #<----- darle propocito
nom.place(x=520,y=448)

op=StringVar()
elecciones={
  "Fondo 1":"pared2.png",
  "Fondo 2":"cielo.png",
  "Fondo 3":"noche.png"
  }
op.set("Fondos")
fondos=OptionMenu(ventana,op,*elecciones)
fondos.place(x=895,y=8)

ayuda=Button(text="Ayuda")
ayuda.place(x=845,y=11)

ventana.mainloop()