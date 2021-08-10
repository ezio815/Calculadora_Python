from tkinter import *
class Boton():
    valor = None
    origen = None
    destino = None
    def __init__(self, origen, destino, valor, x, y, pegajoso = ""):
        Button(origen, text=valor, command=lambda:destino.insert(len(destino.get()), valor)).grid(column = x, row = y, sticky = pegajoso)

    

    """def insercion(self, valor, origen, destino):
        self.valor = valor
        self.origen = origen
        self.destino = destino

    def creacion(self, x, y, pegajoso = ""):
        Button(self.origen, text=self.valor, command=lambda:self.destino.insert(len(self.destino.get()), self.valor)).grid(column = x, row = y, sticky = pegajoso)"""