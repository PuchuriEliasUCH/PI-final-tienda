from tkinter import *
from tkinter import ttk, messagebox
from utils.querys import Consultas_sql as query
from utils.cnx import Connection


class AgregarCategoriaApp(Toplevel):
    def __init__(self, master, refresh):
        super().__init__(master)
        self.refresh = refresh
        self.cnx = Connection()
        self.title("Gestión de Categorías")
        self.geometry("298x350")

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
        self.tree = ttk.Treeview(self)
        self.tree.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
        self.tree.heading("#0", text="Nombre", anchor=CENTER)

        # Botones de eliminar y editar
        self.btn_eliminar = Button(self, text="Eliminar", command=self.eliminar_categoria, bg="red", fg="white")
        self.btn_eliminar.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        self.btn_editar = Button(self, text="Editar", command=self.editar_categoria, bg="orange", fg="white")
        self.btn_editar.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

        self.btn_exit = Button(self, text="Salir", command=self.destroy)
        self.btn_exit.grid(row=3, column=2, padx=10, pady=10, sticky="ew")

    def load_categories(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        categorias = self.cnx.select_all(query.SA_CATE)

        for categoria in categorias:
            self.tree.insert("", 0, text=categoria[1], values=categoria[0])

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
            id_cate = self.tree.item(self.tree.selection())['values'][0]

            seguro = messagebox.askyesno('Eliminar', "Estás seguro de eliminar el registro?")
            if seguro:
                res = self.cnx.delete(query.D_CATE, (id_cate,))
                self.refresh()
                messagebox.showinfo('Eliminar', res)

        else:
            self.lbl_mensaje.config(text="Seleccione una categoría para editar", fg="red")

        self.load_categories()

    def editar_categoria(self):
        selected_item = self.tree.selection()
        if selected_item:
            id_cate = self.tree.item(self.tree.selection())['values'][0]
            nombre_cate = self.tree.item(self.tree.selection())['text']
            EditarCategoriaApp(self, id_cate, nombre_cate, self.load_categories, self.refresh)
            
        else:
            self.lbl_mensaje.config(text="Seleccione una categoría para editar", fg="red")


class EditarCategoriaApp(Toplevel):
    def __init__(self, master, id_cate, nombre_cate, refresh, cates):
        super().__init__(master)
        self.cnx = Connection()
        self.id_cate = int(id_cate)
        self.cates = cates
        self.nombre_cate = nombre_cate
        self.refresh = refresh
        self.title("Editar Categoría")
        self.geometry("300x200")

        self.create_widgets()

    def create_widgets(self):
        # Nombre label and entry
        self.lbl_nombre = Label(self, text="Nuevo Nombre")
        self.lbl_nombre.grid(row=0, column=0, padx=10, pady=10)

        self.entry_nombre = Entry(self)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)
        self.entry_nombre.insert(0, self.nombre_cate)

        # Botón de actualizar categoría
        self.btn_actualizar = Button(self, text="Actualizar", command=self.actualizar_categoria)
        self.btn_actualizar.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    def actualizar_categoria(self):
        nuevo_nombre = self.entry_nombre.get()
        if nuevo_nombre:
            res = self.cnx.update(query.U_CATE, (nuevo_nombre, self.id_cate))
            messagebox.showinfo("Éxito", res)
            self.refresh()
            self.cates()
            self.destroy()
        else:
            messagebox.showerror("Error", "Por favor, ingrese el nuevo nombre de la categoría")

