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

    #-------------------------------------------------------------------------------Trasfondo
    iniciacion0_0=Label(ventana,text="- En tierras lejanas donde los héroes y monstruos abundan, un grupo de amigos se reúne\ncon el deseo de ser aventureros. Explorando los bosques y derrotando monstruos.       ",bg="black",fg="white")
    iniciacion0_0.place(x=255,y=360)
    cont1=Button(ventana,text="Continuar >>>",bg="orange",fg="white",command= lambda: jugador.tr(iniciacion0_0,cont1))
    cont1.place(x=650,y=450)


         #  <------------------------------------------------------------------------------------------------X

    # Instrucciones iniciales
    iniciacion1_0=Label(ventana,text="- Elija a su personaje aventurero (No podras cambiarlo despues).",bg="black",fg="white")
    iniciacion1_0.place(x=255,y=70)
    iniciacion1_1=Label(ventana,text="- Indique su nombre aventurero (No podras cambiarlo despues).",bg="black",fg="white")
    iniciacion1_1.place(x=255,y=360) 

    # Ingreso del nombre:
    nombre=Entry(ventana) 
    nombre.place(x=410,y=450)
    nom=Button(ventana,text="aceptar",bg="orange",fg="white",command=lambda:jugador.Nombre(nombre,iniciacion1_1,nombre,nom))
    nom.place(x=520,y=448)

    # eleccion de personaje:
    des_v=" Vida:  90                                          Vida:  120                                       Vida:  100"
    des_f="  Fuerza:  15                                      Fuerza:  50                                     Fuerza:  25"
    des_m="Mana:  25                                        Mana:  5                                        Mana:  10"
    descripcion=Label(ventana,text=f"{des_v}\n{des_f}\n{des_m}",bg="black",fg="white")
    descripcion.place(x=255,y=235)
    mago=Button(ventana,text= "Mago",bg="orange",fg="white",command= lambda: jugador.Personaje(iniciacion1_0,descripcion,mago,caballero,arquero,magico,fuerte,velos,1))
    mago.place(x=315,y=300)
    ima_mago = PhotoImage(file=f"C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\Maga1.png") 
    magico = Label(ventana, image=ima_mago)
    magico.place(x=270,y=100)
    caballero=Button(ventana,text= "Caballero",bg="orange",fg="white",command= lambda: jugador.Personaje(iniciacion1_0,descripcion,mago,caballero,arquero,magico,fuerte,velos,2))
    caballero.place(x=470,y=300)
    ima_caba = PhotoImage(file=f"C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\caballero1.png") 
    fuerte = Label(ventana, image=ima_caba)
    fuerte.place(x=435,y=100)
    arquero=Button(ventana,text= "Arquero",bg="orange",fg="white",command= lambda: jugador.Personaje(iniciacion1_0,descripcion,mago,caballero,arquero,magico,fuerte,velos,3))
    arquero.place(x=635,y=300)
    ima_arqu = PhotoImage(file=f"C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\Arquero1.png") 
    velos = Label(ventana, image=ima_arqu)
    velos.place(x=600,y=100)

    #ima_arqu = PhotoImage(file=f"C:\\Users\\carlo\\OneDrive\\Escritorio\\aventura\\personaje\\bosque.png") 
    #velos = Label(ventana, image=ima_arqu,bg="black")
    #velos.place(x=249,y=64)



   # Boton de ayuda
    ayuda=Button(text="Ayuda")
    ayuda.place(x=845,y=11)

    ventana.mainloop()

if __name__ == "__main__":
    pantalla()