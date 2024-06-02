from tkinter import *
from z import*

def mai():
    ven = Tk()
   
    y=1
    d="red"
    x=Label(ven,text=y,bg=d)
    x.place(x=0,y=0)
    b=Button(ven,text="x",command= lambda: cam(y,d))
    b.place(x=0,y=30)
    t=Button(ven,text="0",command= lambda: zero(y))
    t.place(x=0,y=60)

    def cam(y,d):
        d="blue"
        y+=2
        x.config(text=y,bg=d)

    def zero(y):
        y=0
        x.config(text=y)

    ven.mainloop()

if __name__ == "__main__":
    mai()