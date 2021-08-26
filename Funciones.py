from tkinter import *

def crearBoton(origen, destino, valor, x, y, pegajoso = "", anchoColumna = 1, altoFila = 1):
    Button(origen, text = valor, command = lambda: destino.insert(len(destino.get()), valor)).grid(column = x, row = y, sticky = pegajoso, columnspan = anchoColumna, rowspan = altoFila)

def resolver(cuentas):
    operaciones = ""
    for i in cuentas:
        if i == '\[+, *, /, ]':
            operaciones += i
        else:
            operaciones += " "

    print(operaciones)


