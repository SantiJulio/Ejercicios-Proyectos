from abc import ABC, abstractmethod

class Espectaculo(ABC):
    __nombre: str
    __fecha: str
    __precio: float

    def __init__(self,nombre,fecha,precio):
        self.__nombre = nombre
        self.__fecha = fecha
        self.__precio = precio

    @abstractmethod
    def precioEntrada(self):
        pass

    @abstractmethod
    def mostrarDatos(self):
        pass

    def getNombre(self):
        return self.__nombre

    def getFecha(self):
        return self.__fecha

    def getPrecio(self):
        return self.__precio

    def __str__(self):
        return(f"""
                Nombre: {self.__nombre}
                Fecha: {self.__fecha}
                Precio: {self.__precio} 
                """) 
    
       