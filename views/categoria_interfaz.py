from tkinter import *
from tkinter import messagebox

from utils.querys import Consultas_sql as query

class AgregarCategoriaApp(Toplevel):
    def __init__(self, master, cnx):
        super().__init__(master)
        self.cnx = cnx
        self.title("Agregar Categoría")

        self.nombre_entry = Entry(self)
        self.nombre_entry.insert(0, "Ingresar nombre")
        self.nombre_entry.bind("<FocusIn>", self.on_entry_click)
        self.nombre_entry.bind("<FocusOut>", self.on_focus_out)
        self.nombre_entry.grid(row=0, column=0, padx=10, pady=5)

        self.btn_agregar = Button(self, text="Agregar", command=self.agregar_categoria)
        self.btn_agregar.grid(row=0, column=1, padx=10, pady=5, sticky=W)


        self.btn_quit = Button(self, text="Salir", command = self.destroy)
        self.btn_quit.grid(row=1, column=0, columnspan=2, pady=10)
        
    def on_entry_click(self, event):
        """Función para limpiar el placeholder cuando se hace clic en la entrada."""
        if self.nombre_entry.get() == "Ingresar nombre":
            self.nombre_entry.delete(0, "end")  # Borra todo en la entrada

    def on_focus_out(self, event):
        """Función para restaurar el placeholder si la entrada está vacía al perder el foco."""
        if self.nombre_entry.get() == "":
            self.nombre_entry.insert(0, "Ingresar nombre")

    def agregar_categoria(self):
        nombre = self.nombre_entry.get()
        
        if nombre and nombre != "Ingresar nombre":
            query_result = self.cnx.insert(query.I_CATE, (nombre, ))
            messagebox.showinfo("Éxito", query_result)
            self.nombre_entry.delete(0, END)
        else:
            messagebox.showerror("Error", "Por favor, ingrese el nombre de la categoría.")
        

  
