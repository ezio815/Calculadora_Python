from tkinter import *
ventana = Tk()
marco = Frame(ventana, width=800, height=600)
marco.config(background="green")
marco.pack()

entrada = Entry(marco)
entrada.config(background="black", foreground="yellow")
entrada.grid(columnspan=4, row=0)

btn1 = Button(marco, command=entrada.insert(Tk.END, '1'))
btn1.grid(column=0, row=1)