from tkinter import*
from librerias import Eleccion

def pantalla():
    ventana=Tk()
 
    ventana.title("Aventura 0.01")# Nombre de ventana
    ventana.geometry("1000x500")# Tamano al abrirce

    ventana.iconbitmap("C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\escudo.ico")# Temporal-icono
    
    imagen_fondo = PhotoImage(file=f"C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\pared.png")
    primer_fondo = Label(ventana, image=imagen_fondo)
    primer_fondo.place(x=0, y=0)
    
    jugador=Eleccion(ventana)# _________________________________________________Instancia de la clase Elección_____________________________________________________________

    # Eleccion de fondo
    op=StringVar()
    elecciones={"pared","cielo","noche"} 
    op.set("Fondos")
    fondos=OptionMenu(ventana,op,*elecciones,command= lambda fon:jugador.Fondo(fon,primer_fondo))
    fondos.place(x=895,y=8)

    #Trasfondo
    iniciacion0_0=Label(ventana,text="- En tierras lejanas donde los héroes y monstruos abundan, un grupo de amigos se reúne\ncon el deseo de ser aventureros. Explorando los bosques y derrotando monstruos.       ",bg="black",fg="white")
    iniciacion0_0.place(x=255,y=360)
    cont1=Button(ventana,text="Continuar >>>",bg="orange",fg="white",command= lambda: jugador.tr(iniciacion0_0,cont1))
    cont1.place(x=650,y=450)

    #ima_arqu = PhotoImage(file="C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\bosque.png") 
    #velos = Label(ventana, image=ima_arqu,bg="black")
    #velos.place(x=249,y=64)



   # Boton de ayuda
    ayuda=Button(text="Ayuda")
    ayuda.place(x=845,y=11)

    ventana.mainloop()

if __name__ == "__main__":
    pantalla()