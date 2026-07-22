from abc import ABC, abstractmethod


class Inmueble(ABC):
    __localidad: str
    __direccion: str
    __superficie: float

    def __init__(self, localidad, direccion, superficie):
        self.__localidad = localidad
        self.__direccion = direccion
        self.__superficie = superficie

    def getLocalidad(self):
        return self.__localidad

    def getDireccion(self):
        return self.__direccion

    def getSuperficie(self):
        return self.__superficie

    @abstractmethod
    def importeDeVenta(self):
        pass

    def __str__(self):
        return f"Localidad: {self.__localidad} | \nDireccion: {self.__direccion} | \nSuperficie Cubierta: {self.__superficie}"
