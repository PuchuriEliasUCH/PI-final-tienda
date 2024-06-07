from tkinter import *
from tkinter import ttk, messagebox

from .categoria_interfaz import AgregarCategoriaApp


class AgregarProducto(Toplevel):
    def __init__(self, master, cnx):
        super().__init__(master)
        self.cnx = cnx
        self.title("Agregar producto")
        self.geometry("400x300")

        self.variable_ctg = StringVar()
        Label(self, text="Categoria").grid(row=0, column=0, padx=10, pady=10)

        comboctg = ttk.Combobox(self, values=['Categoria 1', 'Categoria 2', 'Categoria 3'], state="readonly")
        comboctg.current(0)
        comboctg.grid(row=0, column=1, padx=10, pady=10)

        Button(self, text="Salir", command = self.destroy).grid(row=1, column=0, columnspan=2, pady=10)

        Button(self, text="Nueva categoria", command=self.nueva_categoria).grid(row=0, column=2, padx=10, pady=10)


        Label(self, text="Nombre").grid(row=1, column=0, padx=10, pady=5)
        entry_nombre = ttk.Entry(self)
        entry_nombre.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(self, text="Precio").grid(row=2, column=0, padx=10, pady=5)
        entry_precio = ttk.Entry(self)
        entry_precio.grid(row=2, column=1, padx=10, pady=5)

        label_stock = ttk.Label(self, text="Stock").grid(row=3, column=0, padx=10, pady=5)
        entry_stock = ttk.Entry(self)
        entry_stock.grid(row=3, column=1, padx=10, pady=5)

        Button(self, text="Registrar", command=lambda: messagebox.showinfo("Registrar", "Producto registrado")).grid(row=4, column=1, padx=10, pady=20)

    def nueva_categoria(self):
        AgregarCategoriaApp(self, self.cnx)
                
            