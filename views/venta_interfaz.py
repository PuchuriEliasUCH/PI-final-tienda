from tkinter import *
from tkinter import ttk

from .producto_interfaz import AgregarProducto
from utils.querys import Consultas_sql as query
from utils.cnx import Connection

class Venta_app(Tk):
    def __init__(self):
        super().__init__()
        self.cnx = Connection()
        self.geometry("500x300")

        self.title("Punto de venta")

        Button(text="Nuevo Producto", command=self.nueva_categoria).grid(row=1, column=1)

    def lista_categorias(self):
        return self.cnx.select_all(query.SA_CATE)
    
    def nueva_categoria(self):
        AgregarProducto(self)
        