import tkinter as tk
from tkinter import ttk, messagebox as mb
from .producto_interfaz import AgregarProducto
from utils.querys import Consultas_sql as query
from utils.cnx import Connection
from models.venta import Det_venta


class Venta_app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.cnx = Connection()
        self.geometry("1000x500")
        self.title("Punto de venta")
        self.widgets()
        self.cargar_inicial()

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
        
        ttk.Button(frame_info, text = 'Agregar', command=self.agregar_carrito).grid(column=1, row=2, pady=5, sticky='w')
        ttk.Button(frame_info, text = 'Cancelar', command = self.borrar_controles).grid(column=2, row=2, pady=5, sticky='w')


        # Treeview para mostrar los productos
        tree_frame = ttk.Frame(frame_principal)
        tree_frame.pack(padx=10, pady=10, fill='both', expand=True)

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

        self.tree.column('Producto', anchor=tk.CENTER, width=200)
        self.tree.column('Precio', anchor=tk.CENTER, width=100)
        self.tree.column('Cantidad', anchor=tk.CENTER, width=100)
        self.tree.column('Subtotal', anchor=tk.CENTER, width=100)

        self.tree.pack(fill="both", expand=True)

        # Frame para los botones en la parte inferior
        frame_botones = ttk.Frame(frame_principal)
        frame_botones.pack(side="bottom", fill="x", pady=5)

        # Botón para calcular el total
        ttk.Button(frame_botones, text="Calcular Total", command=self.calcular_total).pack(side="left", padx=10, pady=5)
        # Botón para generar venta
        ttk.Button(frame_botones, text="Generar venta", command=self.nueva_venta).pack(side="left", padx=10, pady=5)

        # Botón para salir
        ttk.Button(frame_botones, text="Salir", command=self.destroy).pack(side="right", padx=10, pady=5)
        
        
        # Frame para la lista de productos
        self.frame_productos = ttk.Frame(self)
        self.frame_productos.grid(column=1, row=1, sticky="nsew", padx=10, pady=10)

        frame_pro_info = ttk.LabelFrame(self.frame_productos, text="Productos")
        frame_pro_info.pack(fill="both", expand=True, padx=10, pady=10)

        tree_prod_frame = ttk.Frame(frame_pro_info)
        tree_prod_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.tree_prod = ttk.Treeview(
            tree_prod_frame,
            columns=('precio', 'stock'),
            height=10,
            yscrollcommand=scrol_y.set,
            xscrollcommand=scrol_x.set
        )

        self.tree_prod.heading("#0", text="Nombre")
        self.tree_prod.heading("precio", text='Precio')
        self.tree_prod.heading("stock", text='Stock')

        self.tree_prod.column("#0", anchor=tk.CENTER, width=200)
        self.tree_prod.column("precio", anchor=tk.CENTER, width=100)
        self.tree_prod.column("stock", anchor=tk.CENTER, width=100)

        self.tree_prod.pack(fill="both", expand=True)

        frame_acciones = ttk.Frame(frame_pro_info)
        frame_acciones.pack(fill="x", padx=10, pady=5)

        ttk.Button(frame_acciones, text='Seleccionar', command=self.seleccionar_producto).pack(side='left', padx=10, pady=5)
        ttk.Button(frame_acciones, text="Nuevo Producto", command=self.nueva_categoria).pack(side="left", padx=10, pady=5)

    def calcular_total(self):
        total = 0.0
        for item in self.tree.get_children():
            subtotal = float(self.tree.item(item, 'values')[3])
            total += subtotal
        mb.showinfo("Total de la Venta", f"El total de la venta es: S/{total:.2f}")


    def cargar_inicial(self):
        for item in self.tree_prod.get_children():
            self.tree_prod.delete(item)
            
        prods = self.cnx.select_all(query.SA_PROD)        
        self.num_factura.set(int(self.cnx.select_all(query.SCOUNT_VENTA)[0][0]) + 1)
        
        for prod in prods:
            self.tree_prod.insert("", "end", text = prod[2], values = (prod[3], prod[4], prod[0]))

    def borrar_controles(self):
        for _ in self.tree.get_children():
            self.tree.delete(_)
            
        self.nom_prod.set("")
        self.precio_pro.set("")
        self.cantidad_pro.set("")
        
    
    def cancelar_venta(self):
        confirmar = mb.askyesno("Cancelar", "Estás cancelando la venta")
        if confirmar:
            self.cnx.delete(query.D_DET_VENTA, (self.tree_prod.item(self.tree_prod.selection(), 'values')[2],))
        
        self.borrar_controles()
        self.cargar_inicial()

    def lista_categorias(self):
        return self.cnx.select_all(query.SA_CATE)

    def nueva_categoria(self):
        AgregarProducto(self, self.cargar_inicial)
        
            
    def seleccionar_producto(self):
        self.nom_prod.set(self.tree_prod.item(self.tree_prod.selection(), 'text'))
        self.precio_pro.set(self.tree_prod.item(self.tree_prod.selection(), 'values')[0])
        
    def agregar_carrito(self):
        o_venta = Det_venta(
            self.txt_factura.get(), 
            self.tree_prod.item(self.tree_prod.selection(), 'values')[2], 
            self.txt_producto.get(), 
            self.txt_precio.get(), 
            self.txt_cantidad.get()
        )
        
        self.tree.insert("", 'end', values=(
            o_venta.nom_prod, 
            o_venta.precio, 
            o_venta.cantidad, 
            o_venta.subtotal(),
            o_venta.id_prod
            )
        )
        
        self.nom_prod.set("")
        self.precio_pro.set("")
        self.cantidad_pro.set("")
        
    def nueva_venta(self):
        if not self.tree.get_children(): 
            return mb.showinfo("Seleccione algunos productos para comprar")
        
        self.cnx.insert(query.I_VENTA)
        for i in self.tree.get_children():
            id_venta = int(self.txt_factura.get())
            id_prod = self.tree.item(i, 'values')[4]
            cantidad = self.tree.item(i, 'values')[2]
            subtotal = self.tree.item(i, 'values')[3]
            params = (
                id_venta,
                id_prod, 
                cantidad, 
                subtotal, 
                )   
        
            self.cnx.insert(query.I_DET_VENTA, params)
            self.cnx.update(query.U_STOCK, (cantidad, id_prod, ))
            
            
        self.cnx.update(query.U_VENTA, (id_venta, ))
        
        self.borrar_controles()
        self.cargar_inicial()   
        
        
        

# No es necesario agregar el código de ejecución aquí ya que se encuentra en index.py

