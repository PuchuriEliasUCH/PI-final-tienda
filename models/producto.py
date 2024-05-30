class Producto: 
    def __init__(self, codigo, nombre, categoria, precio, color, stock):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
        self.__color = color
        self.__stock = stock

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre == nombre

    @property
    def categoria(self):
        return self.__categoria
    
    @categoria.setter
    def categoria(self, categoria):
        self.__categoria == categoria

    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, precio):
        self.__precio == precio

    @property
    def stock(self):
        return self.__stock
    
    @stock.setter
    def stock(self, stock):
        self.__stock == stock
        
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color == color

    def mensaje(self):
        print("Nuevo producto registrado")