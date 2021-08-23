from tkinter import *
from Funciones import *
ventana = Tk()
marco = Frame(ventana, width = 800, height = 600)
marco.config(background="green")
marco.pack()

entrada = Entry(marco)
entrada.config(background="black", foreground="yellow", font = 15)
entrada.grid(columnspan = 4, row = 0)

for i in range(1, 4):
    for j in range(3):
        if i == 1:
            v = i + j + 6 #1-3 7-9
        if i == 2:
            v = i + j + 2 #2-4 4-6
        if i == 3:
            v = i + j - 2 #3-5 7-9 1-3
        crearBoton(marco, entrada, v, j, i + 1, (N, E, S, W))

crearBoton(marco, entrada, 0, 1, 5, (N, E, S, W))
crearBoton(marco, entrada, "(", 0, 1, (N, E, S, W))
crearBoton(marco, entrada, ")", 1, 1, (N, E, S, W))
#crearBoton(marco, entrada, "\u00B1", 2, 1, (N, E, S, W))
#crearBoton(marco, entrada, "CE", 2, 1, (N, E, S, W))
Button(marco, text = "CE", command = lambda: entrada.delete(0, len(entrada.get()))).grid(row = 1, column = 2, sticky = (N, E, S, W))
Button(marco, text = "\u232B", command = lambda: entrada.delete(len(entrada.get())-1)).grid(row = 1, column = 3, sticky = (N, E, S, W))
#crearBoton(marco, entrada, "\u232B", 3, 1, (N, E, S, W))
#crearBoton(marco, entrada, "\u221A", 3, 1, (N, E, S, W))
crearBoton(marco, entrada, ".", 2, 5, (N, E, S, W))

crearBoton(marco, entrada, "+", 3, 5, (N, E, S, W))
crearBoton(marco, entrada, "-", 3, 4, (N, E, S, W))
crearBoton(marco, entrada, "*", 3, 3, (N, E, S, W))
crearBoton(marco, entrada, "/", 3, 2, (N, E, S, W))
Button(marco, text = "=", command = lambda: resolver(entrada.get())).grid(column = 0, row = 6, columnspan = 4, sticky = (N, E, S, W))

ventana.mainloop()