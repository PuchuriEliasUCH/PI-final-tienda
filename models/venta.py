class Det_venta:
    def __init__(self, num_venta, id_prod, nom_prod, precio, cantidad):
        self.__num_venta = num_venta
        self.__nom_prod = nom_prod
        self.__id_prod = id_prod
        self.__precio = float(precio)
        self.__cantidad = int(cantidad)
        
    @property
    def num_venta(self):
        return self.__num_venta
    
    @property
    def id_prod(self):
        return self.__id_prod
    
    @property
    def nom_prod(self):
        return self.__nom_prod
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad == cantidad
        
    @property
    def precio(self):
        return self.__precio

        
    def subtotal(self):
        return self.__precio * self.__cantidad