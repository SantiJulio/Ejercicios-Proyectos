from abc import ABC, abstractmethod

class Excursion(ABC):
    __nomExcursion: str
    __destino : str
    __precio :float

    def __init__(self, ne, des, pr):
        self.__nomExcursion = ne
        self.__destino = des
        self.__precio = pr

    @abstractmethod
    def calcularPrecio(self):
        pass

    def precioFinal(self):
        return self.__precio + self.calcularPrecio()
    
    def getNomExcursion(self):
        return self.__nomExcursion

    def getDestino(self):
        return self.__destino

    def getPrecio(self):
        return self.__precio
    
    def __str__(self):
        return f"Excursion: {self.__nomExcursion} Destino: {self.__destino} Precio: {self.__precio}"
    