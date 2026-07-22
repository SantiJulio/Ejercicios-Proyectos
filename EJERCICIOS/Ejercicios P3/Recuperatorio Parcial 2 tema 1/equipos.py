import abc
from abc import ABC

class Equipo(ABC):
    __marca: str
    __modelo: str
    __anioFabricacion: int
    __tipoCombustible: str
    __potencia: str
    __capCarga: int
    __tarifa: float
    __diasAlquiler: int

    def __init__(self, marca, mod, anio, tipo, pot, cap, tarifa, dias):
        self.__marca = marca
        self.__modelo = mod
        self.__anioFabricacion = anio
        self.__tipoCombustible = tipo
        self.__potencia = pot
        self.__capCarga = cap
        self.__tarifa = tarifa
        self.__diasAlquiler = dias
    
    def getMarca(self):
        return self.__marca
    def getModelo(self):
        return self.__modelo
    def getAnioFab(self):
        return self.__anioFabricacion
    def getTipoCombustible(self):
        return self.__tipoCombustible
    def getPotencia(self):
        return self.__potencia
    def getCapCarga(self):
        return self.__capCarga
    def getTarifa(self):
        return self.__tarifa
    def getDiasAlquiler(self):
        return self.__diasAlquiler
    
    @abc.abstractmethod
    def calcularTarifa(self):
        pass
    def calcular(self):
        return self.__tarifa * self.__diasAlquiler
    
    def __str__(self):
        return f"Marca: {self.__marca} - Modelo: {self.__modelo} - Año Fabricacion: {self.__anioFabricacion} - Tipo Combustible: {self.__tipoCombustible} - Potencia: {self.__potencia} - Capacidad de Carga: {self.__capCarga} - Tarifa: {self.__tarifa} - Dias Alquiler: {self.__diasAlquiler}"
    