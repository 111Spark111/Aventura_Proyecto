from tkinter import*
from librerias import*
from lib2 import*

def pantalla():
    ventana=Tk()
 
    ventana.title("Aventura 0.00")# Nombre de ventana
    ventana.geometry("1000x500")# Tamaño al abrirce

    ventana.iconbitmap("C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\escudo.ico")# icono (Hacer para otros dispocitivos)
    
    List_fondos=Fondo(ventana)# __________________________________________________Instancia de la clase Fondo______________________________________________________________

    # Eleccion de fondo
    op=StringVar()
    elecciones={"Pared","Cielo","Noche"}
    op.set("Fondos")
    fondos=OptionMenu(ventana,op,*elecciones,command= lambda fon:List_fondos.fondos(fon))
    fondos.place(x=895,y=8)
    
    Botones=Eleccion(ventana)# _________________________________________________Instancia de la clase Elección_____________________________________________________________

    #Trasfondo
    iniciacion0_0=Label(ventana,text="- En tierras lejanas donde los héroes y monstruos abundan, un grupo de amigos se reúne\ncon el deseo de ser aventureros. Explorando los bosques y derrotando monstruos.       ",bg="black",fg="white")
    iniciacion0_0.place(x=255,y=360)
    cont1=Button(ventana,text="Continuar >>>",bg="orange",fg="white",command= lambda: Botones.tr(iniciacion0_0,cont1,tras_0))
    cont1.place(x=650,y=450)

    ima_T_0 = PhotoImage(file=Botones.imagen("T_0")) 
    tras_0 = Label(ventana, image=ima_T_0,bg="black")
    tras_0.place(x=249,y=64)
    guia=Ayuda(ventana)# _________________________________________________Instancia de la clase Ayuda_____________________________________________________________
   # Boton de ayuda
    ayuda=Button(text="Ayuda",command= lambda: guia.la_guia())
    ayuda.place(x=845,y=11)

    ventana.mainloop()

if __name__ == "__main__":
    pantalla()