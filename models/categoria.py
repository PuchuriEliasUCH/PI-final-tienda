class Categoria:
    def __init__(self, codigo, nombre, estado):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__estado = estado

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre== nombre

    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self, estado):
        self.__estado == estado