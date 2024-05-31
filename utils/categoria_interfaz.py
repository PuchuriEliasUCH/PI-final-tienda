import os
import tkinter as tk
from tkinter import messagebox
from utils.cnx import Connection
from utils.querys import Consultas_sql as query
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configuración de la conexión a MySQL
config = {
    'user': os.getenv("BD_USER"),
    'password': os.getenv("BD_PASS"),
    'host': os.getenv("BD_HOST"),
    'database': os.getenv("BD_NAME"),
    'auth_plugin': 'mysql_native_password',  # Necesario en ciertos casos
    'port': 3306,  # Puerto predeterminado de MySQL
    'use_pure': True,  # Usar el conector MySQL puro
}

# Asegurarse de que el socket UNIX no se utilice
config['unix_socket'] = None

class AgregarCategoriaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agregar Categoría")

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        # Etiqueta y entrada para el nombre con placeholder
        self.nombre_entry = tk.Entry(self.frame)
        self.nombre_entry.insert(0, "Ingresar nombre")
        self.nombre_entry.bind("<FocusIn>", self.on_entry_click)
        self.nombre_entry.bind("<FocusOut>", self.on_focus_out)
        self.nombre_entry.grid(row=0, column=0, padx=10, pady=5)

        # Botón para agregar categoría
        self.btn_agregar = tk.Button(self.frame, text="Agregar", command=self.agregar_categoria)
        self.btn_agregar.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

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
            try:
                cnx = Connection(config)
                query_result = cnx.insert(query.I_CATE, (nombre,))
                messagebox.showinfo("Éxito", query_result)
                self.nombre_entry.delete(0, tk.END)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Por favor, ingrese el nombre de la categoría.")

# Crear la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = AgregarCategoriaApp(root)
    root.mainloop()
