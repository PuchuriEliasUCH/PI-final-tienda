from tkinter import *
from tkinter import ttk, messagebox

from .categoria_interfaz import AgregarCategoriaApp
from utils.cnx import Connection
from utils.querys import Consultas_sql as querys


class AgregarProducto(Toplevel):
    def __init__(self, master, refresh):
        super().__init__(master)
        self.cnx = Connection()
        self.refresh = refresh
        self.title("Agregar producto")
        self.geometry("360x200")
        self.widgets()
        
    def widgets(self):
        # Frame principal
        frame_principal = ttk.Frame(self)
        frame_principal.pack(fill="both", expand=True)

        self.cates = {x[1]: x[0] for x in self.cargar_categorias()}

        self.variable_ctg = StringVar()
        ttk.Label(frame_principal, text="Categoria").grid(row=0, column=0, padx=10, pady=10)

        self.comboctg = ttk.Combobox(frame_principal, values=list(self.cates.keys()), state="readonly")
        self.comboctg.current(0)
        self.comboctg.grid(row=0, column=1, padx=10, pady=10)

        ttk.Button(frame_principal, text="Nueva categoria", command=self.nueva_categoria).grid(row=0, column=2, padx=10, pady=10)

        ttk.Label(frame_principal, text="Nombre").grid(row=1, column=0, padx=10, pady=5)
        self.txt_nombre = ttk.Entry(frame_principal)
        self.txt_nombre.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(frame_principal, text="Precio").grid(row=2, column=0, padx=10, pady=5)
        self.txt_precio = ttk.Entry(frame_principal)
        self.txt_precio.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(frame_principal, text="Stock").grid(row=3, column=0, padx=10, pady=5)
        self.txt_stock = ttk.Entry(frame_principal)
        self.txt_stock.grid(row=3, column=1, padx=10, pady=5)

        frame_botones = ttk.Frame(frame_principal)
        frame_botones.grid(row=4, column=1, columnspan=2, pady=20)

        ttk.Button(frame_botones, text="Registrar", command=self.agregar_producto).pack(side="left", padx=10, pady=5)

        ttk.Button(frame_botones, text="Salir", command=self.destroy).pack(side="right", padx=10, pady=5)

        # Centrar el botón "Registrar"
        frame_botones.grid_columnconfigure(0, weight=1)  # Columna izquierda expandible

    def nueva_categoria(self):
        AgregarCategoriaApp(self, self.cargar_categorias)
        
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
        self.refresh() 
            