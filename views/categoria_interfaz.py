
from tkinter import *
from tkinter import ttk, messagebox
from utils.querys import Consultas_sql as query
from utils.cnx import Connection

class AgregarCategoriaApp(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.cnx = Connection()
        self.title("Gestión de Categorías")
        self.geometry("500x400")

        self.create_widgets()
        self.load_categories()

    def create_widgets(self):
        # Nombre label and entry
        self.lbl_nombre = Label(self, text="Nombre")
        self.lbl_nombre.grid(row=0, column=0, padx=10, pady=10)

        self.entry_nombre = Entry(self)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        # Botón de registrar categoría
        self.btn_registrar = Button(self, text="Registrar", command=self.agregar_categoria)
        self.btn_registrar.grid(row=0, column=2, padx=10, pady=10)

        # Mensajes de error o satisfactorios
        self.lbl_mensaje = Label(self, text="")
        self.lbl_mensaje.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Tabla de categorías
        self.tree = ttk.Treeview(self, columns=("Nombre"), show="headings")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Botones de eliminar y editar
        self.btn_eliminar = Button(self, text="Eliminar", command=self.eliminar_categoria, bg="red", fg="white")
        self.btn_eliminar.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        self.btn_editar = Button(self, text="Editar", command=self.editar_categoria, bg="orange", fg="white")
        self.btn_editar.grid(row=3, column=1, columnspan=2, padx=10, pady=10, sticky="ew")

    def load_categories(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        categorias = self.cnx.select_all(query.SA_CATE)
        for categoria in categorias:
            self.tree.insert("", "end", values=(categoria[1],))

    def agregar_categoria(self):
        nombre = self.entry_nombre.get()
        if nombre:
            self.cnx.insert(query.I_CATE, (nombre,))
            self.lbl_mensaje.config(text="Categoría añadida correctamente", fg="green")
            self.entry_nombre.delete(0, END)
            self.load_categories()
        else:
            self.lbl_mensaje.config(text="Por favor, ingrese el nombre de la categoría", fg="red")

    def eliminar_categoria(self):
        selected_item = self.tree.selection()
        if selected_item:
            categoria_nombre = self.tree.item(selected_item[0], 'values')[0]
            categoria_id = self.cnx.select_one(query.S_CATE_ID_BY_NAME, (categoria_nombre,))[0]
            self.cnx.delete(query.D_CATE, (categoria_id,))
            self.lbl_mensaje.config(text="Categoría eliminada correctamente", fg="green")
            self.load_categories()
        else:
            self.lbl_mensaje.config(text="Seleccione una categoría para eliminar", fg="red")

    def editar_categoria(self):
        selected_item = self.tree.selection()
        if selected_item:
            categoria_nombre = self.tree.item(selected_item[0], 'values')[0]
            EditarCategoriaApp(self, categoria_nombre, self.load_categories)
            self.load_categories()
        else:
            self.lbl_mensaje.config(text="Seleccione una categoría para editar", fg="red")

class EditarCategoriaApp(Toplevel):
    def __init__(self, master, categoria_nombre, refresh_callback):
        super().__init__(master)
        self.cnx = Connection()
        self.categoria_nombre = categoria_nombre
        self.refresh_callback = refresh_callback
        self.title("Editar Categoría")
        self.geometry("300x200")

        self.create_widgets()

    def create_widgets(self):
        # Nombre label and entry
        self.lbl_nombre = Label(self, text="Nuevo Nombre")
        self.lbl_nombre.grid(row=0, column=0, padx=10, pady=10)

        self.entry_nombre = Entry(self)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)
        self.entry_nombre.insert(0, self.categoria_nombre)

        # Botón de actualizar categoría
        self.btn_actualizar = Button(self, text="Actualizar", command=self.actualizar_categoria)
        self.btn_actualizar.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    def actualizar_categoria(self):
        nuevo_nombre = self.entry_nombre.get()
        if nuevo_nombre:
            categoria_id = self.cnx.select_by_id(query.SO_CATE, (self.categoria_nombre[0],))
            res = self.cnx.update(query.U_CATE, (nuevo_nombre, categoria_id))
            messagebox.showinfo("Éxito", res)
            self.destroy()
        else:
            messagebox.showerror("Error", "Por favor, ingrese el nuevo nombre de la categoría")
 
