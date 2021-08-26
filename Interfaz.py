from tkinter import *
from Funciones import *
ventana = Tk()
marco = Frame(ventana, width=800, height=600)
marco.config(background="green")
marco.pack()

entrada = Entry(marco)
entrada.config(background="black", foreground="white", font = 15)
entrada.grid(columnspan=4, row=0)

for i in range(1,4):
    for j in range(3):
        if i == 1:
            v = i + j #1-3
        if i == 2:
            v = i + j + 2 #2-4 4-6
        if i == 3:
            v = i + j + 4 #3-5 7-9
        crearBoton(marco, entrada, v, j, i, (N, E, S, W))

crearBoton(marco, entrada, 0, 0, 4, (N, E, S, W), 3)
crearBoton(marco, entrada, "+", 3, 1, (N, E, S, W))
crearBoton(marco, entrada, "-", 3, 2, (N, E, S, W))
crearBoton(marco, entrada, "*", 3, 3, (N, E, S, W))
crearBoton(marco, entrada, "/", 3, 4, (N, E, S, W))
crearBoton(marco, entrada, "(", 0, 5, (N, E, S, W))
crearBoton(marco, entrada, ")", 1, 5, (N, E, S, W))
Button(marco, text = "=", command = lambda: resolver(entrada.get())).grid(column = 2, row = 5, columnspan = 2, sticky = (N, E, S, W))

ventana.mainloop()