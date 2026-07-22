from abc import ABC, abstractmethod

class Inmueble(ABC):
    __localidad: str
    __direc: str
    __supC: float

    def __init__(self,localidad,direc,supC):
        self.__localidad = localidad
        self.__direc = direc
        self.__supC = supC

    @abstractmethod
    def calcular(self):
        pass

    def importeVenta(self):
        return self.__supC * 15 
    
    def getLocalidad(self):
        return self.__localidad

    def getDirec(self):
        return self.__direc

    def getSupC(self):
        return self.__supC

    def __str__(self):
        return(f"""
                Localidad: {self.__localidad}
                Direccion: {self.__direc}
                Superficie Cubierta: {self.__supC}
                """)    