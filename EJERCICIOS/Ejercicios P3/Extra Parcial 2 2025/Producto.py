from abc import ABC, abstractmethod

class Producto(ABC):
    __codigo: str
    __nombre: str
    __precio: float
    __desc: str
    __stock: int

    def __init__(self,cod,nom,pre,desc,sto):
        self.__codigo = cod
        self.__nombre = nom
        self.__precio = pre
        self.__desc = desc
        self.__stock = sto

    @abstractmethod
    def precioFinal(self):
        pass

    @abstractmethod
    def mostrar(self):
        pass

    def getTipo(self):
        return (type(self).__name__)

    def getCodigo(self):
        return self.__codigo

    def getNombre(self):
        return self.__nombre

    def getPrecio(self):
        return self.__precio

    def getDesc(self):
        return self.__desc

    def getStock(self):
        return self.__stock
    
    def actualizarStock(self):
        self.__stock -= 1

    def __str__(self):
        return(f"""
                Codigo: {self.__codigo}
                Nombre: {self.__nombre}
                Precio: {self.__precio}
                Desc: {self.__desc}
                Stock: {self.__stock}
                """)    