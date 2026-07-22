from abc import ABC, abstractmethod

class Maquina(ABC):
    __id: int
    __marca: str
    __modelo: str
    __anio: int
    __precio: float

    def __init__(self,id,marca,modelo,anio,precio):
        self.__id = id
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio
        self.__precio = precio

    @abstractmethod
    def calculoSubTotal(self):
        pass
    
    def importeFinal(self):
        subtotal = self.calculoSubTotal()
        return subtotal + (subtotal * (5 / 100))    

    @abstractmethod
    def mostrarDatos(self):
        pass

    def getId(self):
        return self.__id
    
    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    def getAnio(self):
        return self.__anio
    
    def getPrecio(self):
        return self.__precio
    
    def __str__(self):
        return(f"""
                ID: {self.__id}
                Marca: {self.__marca}
                Modelo: {self.__modelo}
                Anio F: {self.__anio}
                Precio: {self.__precio}
                """)