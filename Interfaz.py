from tkinter import *
import Clases
ventana = Tk()
marco = Frame(ventana, width=800, height=600)
marco.config(background="green")
marco.pack()

entrada = Entry(marco)
entrada.config(background="black", foreground="yellow")
entrada.grid(columnspan=4, row=0)

for i in range(1,4):
    for j in range(3):
        if i == 1:
            v = i + j #1-3
        if i == 2:
            v = i + j + 2 #2-4 4-6
        if i == 3:
            v = i + j + 4 #3-5 7-9
        Clases.Boton(marco, entrada, v, j, i, (N, E, S, W))
        
Clases.Boton(marco, entrada, 0, 1, 4, (N, E, S, W))







"""btn1.insercion("1", marco, entrada)
btn1.creacion(0, 1, "w")"""

'''btn1 = Button(marco, text=1, command=lambda:entrada.insert(len(entrada.get()), 1))
btn1.grid(column=0, row=1)

btn2 = Button(marco, text=2, command=lambda:entrada.insert(len(entrada.get()), 2))
btn2.grid(column=1, row=1)

btn3 = Button(marco, text=3, command=lambda:entrada.insert(len(entrada.get()), 3))
btn3.grid(column=3, row=1)

btnSumar = Button(marco, text="+", command=lambda:entrada.insert(len(entrada.get()), "+"))'''

ventana.mainloop()