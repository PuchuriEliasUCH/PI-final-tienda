import os
import tkinter as tk
from tkinter import messagebox
from cnx import Connection
from querys import Consultas_sql as query
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configuración de la conexión a MySQL
config = {
    'user': os.getenv("BD_USER"),
    'password': os.getenv("BD_PASS"),
    'host': os.getenv("BD_HOST"),
    'database': os.getenv("BD_NAME")
}

class AgregarCategoriaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestionar Categorías")

        # Frame para agregar categorías
        self.frame_agregar = tk.Frame(self.root)
        self.frame_agregar.pack(padx=20, pady=10)

        # Etiqueta y entrada para el nombre
        self.label_nombre = tk.Label(self.frame_agregar, text="Nombre")
        self.label_nombre.grid(row=0, column=0, padx=10, pady=5)

        self.nombre_entry = tk.Entry(self.frame_agregar)
        self.nombre_entry.grid(row=0, column=1, padx=10, pady=5)

        # Botón para agregar categoría
        self.btn_agregar = tk.Button(self.frame_agregar, text="Agregar", command=self.agregar_categoria)
        self.btn_agregar.grid(row=0, column=2, padx=10, pady=5, sticky=tk.W)

        # Label para mensajes de error/satisfactorios
        self.label_mensaje = tk.Label(self.root, text="")
        self.label_mensaje.pack(padx=20, pady=5)

        # Frame para mostrar categorías
        self.frame_mostrar = tk.Frame(self.root)
        self.frame_mostrar.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        self.label_categorias = tk.Label(self.frame_mostrar, text="Todas las Categorías:")
        self.label_categorias.pack()

        # Listbox para mostrar las categorías
        self.lista_categorias = tk.Listbox(self.frame_mostrar)
        self.lista_categorias.pack(fill=tk.BOTH, expand=True)

        # Frame para botones de eliminar y editar
        self.frame_botones = tk.Frame(self.root)
        self.frame_botones.pack(padx=20, pady=10, fill=tk.X)

        self.btn_eliminar = tk.Button(self.frame_botones, text="Eliminar", command=self.eliminar_categoria, bg="red", fg="white")
        self.btn_eliminar.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.btn_editar = tk.Button(self.frame_botones, text="Editar", command=self.editar_categoria, bg="orange", fg="white")
        self.btn_editar.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Botón para salir
        self.btn_salir = tk.Button(self.frame_botones, text="Salir", command=self.root.quit, bg="grey", fg="white")
        self.btn_salir.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Cargar las categorías al iniciar la aplicación
        self.cargar_categorias()

    def agregar_categoria(self):
        nombre = self.nombre_entry.get()

        if nombre:
            try:
                cnx = Connection(config)
                query_result = cnx.insert(query.I_CATE, (nombre,))
                self.label_mensaje.config(text="Categoría agregada con éxito.", fg="green")
                self.nombre_entry.delete(0, tk.END)
                self.cargar_categorias()  # Recargar las categorías
                cnx.close()
            except Exception as e:
                self.label_mensaje.config(text=f"Error: {str(e)}", fg="red")
        else:
            self.label_mensaje.config(text="Por favor, ingrese el nombre de la categoría.", fg="red")

    def cargar_categorias(self):
        try:
            cnx = Connection(config)
            categorias = cnx.query(query.SA_CATE)
            self.lista_categorias.delete(0, tk.END)  # Limpiar la lista antes de cargar
            for categoria in categorias:
                self.lista_categorias.insert(tk.END, categoria[1])  # Mostrar solo el nombre de la categoría
            cnx.close()
        except Exception as e:
            self.label_mensaje.config(text=f"Error: {str(e)}", fg="red")

    def eliminar_categoria(self):
        selected = self.lista_categorias.curselection()
        if selected:
            nombre = self.lista_categorias.get(selected)
            try:
                cnx = Connection(config)
                cnx.execute(query.D_CATE, (nombre,))
                self.label_mensaje.config(text="Categoría eliminada con éxito.", fg="green")
                self.cargar_categorias()
                cnx.close()
            except Exception as e:
                self.label_mensaje.config(text=f"Error: {str(e)}", fg="red")
        else:
            self.label_mensaje.config(text="Por favor, seleccione una categoría para eliminar.", fg="red")

    def editar_categoria(self):
        selected = self.lista_categorias.curselection()
        if selected:
            nombre = self.lista_categorias.get(selected)
            nuevo_nombre = self.nombre_entry.get()
            if nuevo_nombre:
                try:
                    cnx = Connection(config)
                    cnx.execute(query.U_CATE, (nuevo_nombre, nombre))
                    self.label_mensaje.config(text="Categoría editada con éxito.", fg="green")
                    self.cargar_categorias()
                    cnx.close()
                except Exception as e:
                    self.label_mensaje.config(text=f"Error: {str(e)}", fg="red")
            else:
                self.label_mensaje.config(text="Por favor, ingrese el nuevo nombre para la categoría.", fg="red")
        else:
            self.label_mensaje.config(text="Por favor, seleccione una categoría para editar.", fg="red")

# Crear la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = AgregarCategoriaApp(root)
    root.mainloop()
