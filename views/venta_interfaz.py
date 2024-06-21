import tkinter as tk
from tkinter import ttk, messagebox as mb
from .producto_interfaz import AgregarProducto
from utils.querys import Consultas_sql as query
from utils.cnx import Connection


class Venta_app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.cnx = Connection()
        self.geometry("1000x600")
        self.title("Punto de venta")
        self.widgets()
        self.cargar_productos()

    def widgets(self):
        # Frame principal
        frame_principal = ttk.Frame(self)
        frame_principal.grid(column=0, row=1)

        # Título (barra simple)
        frame_titulo = tk.Frame(frame_principal, bg="#F26243", height=150)
        frame_titulo.pack(fill="x")
        tk.Label(frame_titulo, text="VENTAS", bg="#F26243", font='arial 16 bold').pack(padx=10, pady=10)

        # Información de la venta
        frame_info = ttk.LabelFrame(frame_principal, text="Información de la venta")
        frame_info.pack(fill="x", padx=10, pady=10)

        ttk.Label(frame_info, text='# Factura', font='sans 10 bold').grid(column=0, row=0, padx=5, pady=5, sticky="w")
        self.num_factura = tk.StringVar()
        self.txt_factura = ttk.Entry(frame_info, textvariable=self.num_factura, font='sans 8', state='readonly')
        self.txt_factura.grid(column=1, row=0, padx=5, pady=5, sticky="w")

        ttk.Label(frame_info, text="Producto:", font='sans 10 bold').grid(column=2, row=0, padx=5, pady=5, sticky="w")
        self.nom_prod = tk.StringVar()
        self.txt_producto = ttk.Entry(frame_info, textvariable=self.nom_prod, state='readonly', font='sans 8')
        self.txt_producto.grid(column=3, row=0, padx=5, pady=5, sticky="w")

        ttk.Label(frame_info, text="Precio:", font='sans 10 bold').grid(column=0, row=1, padx=5, pady=5, sticky="w")
        self.precio_pro = tk.StringVar()
        self.txt_precio = ttk.Entry(frame_info, textvariable=self.precio_pro, state='readonly', font='sans 8')
        self.txt_precio.grid(column=1, row=1, padx=5, pady=5, sticky="w")

        ttk.Label(frame_info, text="Cantidad:", font='sans 10 bold').grid(column=2, row=1, padx=5, pady=5, sticky="w")
        self.cantidad_pro = tk.StringVar()
        self.txt_cantidad = ttk.Entry(frame_info, textvariable=self.cantidad_pro, font='sans 8')
        self.txt_cantidad.grid(column=3, row=1, padx=5, pady=5, sticky="w")
        
        ttk.Button(frame_info, text = 'Agregar').grid(column=1, row=2, pady=5, sticky='w')
        ttk.Button(frame_info, text = 'Borrar').grid(column=2, row=2, pady=5, sticky='w')

        # Treeview para mostrar los productos
        tree_frame = ttk.Frame(frame_principal)
        tree_frame.pack(padx=10, pady=10)

        scrol_y = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL)
        scrol_y.pack(side=tk.RIGHT, fill=tk.Y)

        scrol_x = ttk.Scrollbar(tree_frame, orient=tk.HORIZONTAL)
        scrol_x.pack(side=tk.BOTTOM, fill=tk.X)

        self.tree = ttk.Treeview(
            tree_frame,
            columns=('Producto', 'Precio', 'Cantidad', 'Subtotal'),
            show='headings',
            height=10,
            yscrollcommand=scrol_y.set,
            xscrollcommand=scrol_x.set
        )
        scrol_y.config(command=self.tree.yview)
        scrol_x.config(command=self.tree.xview)

        self.tree.heading('#1', text="Producto")
        self.tree.heading('#2', text="Precio")
        self.tree.heading('#3', text="Cantidad")
        self.tree.heading('#4', text="Subtotal")

        self.tree.column('Producto', anchor=tk.CENTER, width=100)
        self.tree.column('Precio', anchor=tk.CENTER, width=100)
        self.tree.column('Cantidad', anchor=tk.CENTER, width=100)
        self.tree.column('Subtotal', anchor=tk.CENTER, width=100)

        self.tree.pack()

        # Frame para los botones en la parte inferior
        frame_botones = ttk.Frame(frame_principal)
        frame_botones.pack(side="bottom", fill="x", pady=5)

        # Botón para agregar nuevo producto
        ttk.Button(frame_botones, text="Nuevo Producto", command=self.nueva_categoria).pack(side="left", padx=10, pady=5)

        # Botón para calcular el total
        ttk.Button(frame_botones, text="Calcular Total", command=self.calcular_total).pack(side="left", padx=10, pady=5)

        # Botón para salir
        ttk.Button(frame_botones, text="Salir", command=self.destroy).pack(side="right", padx=10, pady=5)
        
        ttk.Button(frame_botones, text="Generar Venta").pack(side="right", padx=10, pady=5)
        
        # Frame para la lista de productos
        frame_productos = ttk.Frame(self)
        frame_productos.grid(column=2, row=1, columnspan=1)
        
        tree_prod_frame = ttk.Frame(frame_productos)
        tree_prod_frame.pack(padx=10, pady=10)
        
        self.tree_prod = ttk.Treeview(
            tree_prod_frame,
            columns=('precio', 'stock'),
            height=10
        )
        
        self.tree_prod.heading("#0", text = "Nombre")
        self.tree_prod.heading("precio", text = 'Precio')
        self.tree_prod.heading("stock", text = 'Stock')
        
        self.tree_prod.pack()
        
        frame_acciones = ttk.Frame(frame_productos)
        frame_acciones.pack(side = 'bottom', fill='x', pady = 5)
        
        ttk.Button(frame_acciones, text = 'Seleccionar', command = self.seleccionar_producto).pack(side= 'left', padx=10, pady=5)
        ttk.Button(frame_acciones, text = 'Opciones', ).pack(side = 'left', padx=10, pady=5)

    def calcular_total(self):
        total = 0.0
        for item in self.tree.get_children():
            subtotal = float(self.tree.item(item, 'values')[3])
            total += subtotal
        mb.showinfo("Total de la Venta", f"El total de la venta es: S/{total:.2f}")

    def lista_categorias(self):
        return self.cnx.select_all(query.SA_CATE)

    def nueva_categoria(self):
        AgregarProducto(self)
        
    def cargar_productos(self):
        for item in self.tree_prod.get_children():
            self.tree_prod.delete(item)
            
        prods = self.cnx.select_all(query.SA_PROD)
        
        for prod in prods:
            self.tree_prod.insert("", "end", text = prod[2], values = (prod[3], prod[4]))
            
    def seleccionar_producto(self):
        self.nom_prod.set(self.tree_prod.item(self.tree_prod.selection(), 'text'))
        self.precio_pro.set(self.tree_prod.item(self.tree_prod.selection(), 'values')[0])

# No es necesario agregar el código de ejecución aquí ya que se encuentra en index.py
