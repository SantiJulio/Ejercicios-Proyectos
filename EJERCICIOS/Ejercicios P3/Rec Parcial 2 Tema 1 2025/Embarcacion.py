from abc import ABC, abstractmethod

class Embarcacion(ABC):
    __nomE: str
    __eslora: float
    __anioF: int
    __costo: float
    __dispo: bool
    __cantD: int

    def __init__(self,nom,es,ani,cost,dis,cant):
        self.__nomE = nom
        self.__eslora = es
        self.__anioF = ani
        self.__costo = cost
        self.__dispo = dis
        self.__cantD = cant

    @abstractmethod
    def costoTotal(self):
        pass

    @abstractmethod
    def mostrarAlquilado(self):
        pass

    def getNomE(self):
        return self.__nomE

    def getEslora(self):
        return self.__eslora

    def getAnioF(self):
        return self.__anioF

    def getCosto(self):
        return self.__costo

    def getDispo(self):
        return self.__dispo

    def getCantD(self):
        return self.__cantD
    
    def alquilar(self):
        self.__dispo = False
    
    def setDias(self,dias):
        self.__cantD = dias

    def __str__(self):
        return(f"""
                Nombre {self.__nomE}
                Eslora {self.__eslora}
                Anio F {self.__anioF}
                Costo {self.__costo}
                Dispo {self.__dispo}
                Cant D {self.__cantD}
                """)    