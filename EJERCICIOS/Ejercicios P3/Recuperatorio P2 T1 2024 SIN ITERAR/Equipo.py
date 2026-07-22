from abc import ABC, abstractmethod

class Equipo(ABC):
    __marca: str
    __modelo: str
    __anioF: int
    __tipoC: str
    __potencia: int
    __capac: int
    __tarifa: float
    __cantD: int

    def __init__(self,marca,modelo,anioF,tipoC,potencia,capac,tarifa,cantD):
        self.__marca = marca
        self.__modelo = modelo
        self.__anioF = anioF
        self.__tipoC = tipoC
        self.__potencia = potencia
        self.__capac = capac
        self.__tarifa = tarifa
        self.__cantD = cantD

    @abstractmethod
    def calcular(self):
        pass

    def tarifaAlquiler(self):
        return self.__tarifa * self.__cantD 
    
    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo 

    def getAnioF(self):
        return self.__anioF

    def getTipoC(self):
        return self.__tipoC

    def getPotencia(self):
        return self.__potencia

    def getCapac(self):
        return self.__capac

    def getTarifa(self):
        return self.__tarifa

    def getCantD(self):
        return self.__cantD 

    def __str__(self):
        return(f"""
                Marca: {self.__marca}
                Modelo: {self.__modelo}
                Anio: {self.__anioF}
                TipoC: {self.__tipoC}
                Potencia: {self.__potencia}
                Capacidad: {self.__capac}
                Tarifa: {self.__tarifa}
                CantD: {self.__cantD}
                """)  