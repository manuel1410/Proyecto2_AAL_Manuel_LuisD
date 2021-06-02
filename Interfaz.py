from tkinter import *
from tkinter import messagebox

global num_ram, ang_ram, prof, diam, decre


#Ventana Pricipal-----------------------------------------------------------------------------------

#Paleta de Colores:
# 1. d8e3e7
# 2. 51c4d3
# 3. 126e82
# 4. 132c33

def ven_prin(): # ventana principal
    #Ventana principal

    ven = Tk()
    ven.title("Árboles Genéticos")
    ven.iconbitmap('arbol.ico')
    ven.geometry('1000x720+250+35')
    ven.config(bg= '#d8e3e7')
    ven.resizable(width= False, height= False)

    titu = Label(ven, text= "Árboles Genéticos", bg= "#51c4d3", fg= "#132c33", font=("Times", 24), padx= 40)
    titu.place(x= 350, y= 20)

    titu = Label(ven, text= "Número de Ramificaciones", bg= "#d8e3e7", fg= "#51c4d3", font=("Times", 14))
    titu.place(x= 70, y= 95)
    num_ent = Entry(ven, font=("Helvetica", 11), width= 6, justify= CENTER, fg= "#132c33")
    num_ent.place(x= 140, y= 120)

    ven.mainloop()

ven_prin()