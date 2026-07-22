from abc import ABC, abstractmethod

class Vehiculo(ABC):
    __cod: str
    __marca: str
    __modelo: str
    __precio: float
    __cantD: int

    def __init__(self,cod,mar,mod,pre,cant):
        self.__cod = cod
        self.__marca = mar
        self.__modelo = mod
        self.__precio = pre
        self.__cantD = cant

    @abstractmethod
    def costoFinal(self):
        pass
    
    @abstractmethod
    def mostrar(self):
        pass

    def getTipo(self):
        return type(self).__name__

    def getCod(self):
        return self.__cod

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo

    def getPrecio(self):
        return self.__precio

    def getCantD(self):
        return self.__cantD
    
    def alquilerV(self):
        self.__cantD -= 1

    def __str__(self):
        return(f"""
                Codigo: {self.__cod}
                Marca: {self.__marca}
                Modelo: {self.__modelo}
                Precio: {self.__precio}
                Cantidad Disponible: {self.__cantD}
                """)    