from tkinter import *
from z import Z

def mai():
    ven = Tk()
    
    yolo = Z(ven)

    y = Label(ven, text="esto")
    y.place(x=45, y=15)
    
    bot = Button(ven, text="Elimina", command=lambda: yolo.btn(bot, y)) 
    bot.place(x=45, y=45)

    ven.mainloop()

if __name__ == "__main__":
    mai()