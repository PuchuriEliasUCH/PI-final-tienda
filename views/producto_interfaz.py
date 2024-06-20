from tkinter import *
from tkinter import ttk, messagebox

from .categoria_interfaz import AgregarCategoriaApp
from utils.cnx import Connection
from utils.querys import Consultas_sql as querys


class AgregarProducto(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.cnx = Connection()
        self.title("Agregar producto")
        self.geometry("400x300")
        
        self.cates = {x[1]:x[0] for x in self.cargar_categorias()}

        self.variable_ctg = StringVar()
        Label(self, text="Categoria").grid(row=0, column=0, padx=10, pady=10)

        self.comboctg = ttk.Combobox(self, values= list(self.cates.keys()), state="readonly")
        self.comboctg.current(0)
        self.comboctg.grid(row=0, column=1, padx=10, pady=10)

        Button(self, text="Nueva categoria", command=self.nueva_categoria).grid(row=0, column=2, padx=10, pady=10)


        Label(self, text="Nombre").grid(row=1, column=0, padx=10, pady=5)
        self.txt_nombre = ttk.Entry(self)
        self.txt_nombre.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(self, text="Precio").grid(row=2, column=0, padx=10, pady=5)
        self.txt_precio = ttk.Entry(self)
        self.txt_precio.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(self, text="Stock").grid(row=3, column=0, padx=10, pady=5)
        self.txt_stock = ttk.Entry(self)
        self.txt_stock.grid(row=3, column=1, padx=10, pady=5)


        Button(self, text="Registrar", command = self.agregar_producto).grid(row=4, column=1, padx=10, pady=20)
        Button(self, text="Salir", command = self.destroy).grid(row=4, column=2, padx=10, pady=20)


    def nueva_categoria(self):
        AgregarCategoriaApp(self)
        
    def cargar_categorias(self):
        return self.cnx.select_all(querys.SA_CATE)
    
    def agregar_producto(self):
        id_cat = self.cates.get(self.comboctg.get())
        params = (
            id_cat,
            self.txt_nombre.get(),
            self.txt_precio.get(),
            self.txt_stock.get()
        )
        self.cnx.insert(querys.I_PROD, params)
        
                
            