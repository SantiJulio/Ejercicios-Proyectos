class Colectivo:
    __patente: str
    __marca: str
    __modelo: str
    __capacidad: int
    __dniChofer: int
    __promCombustible = 47

    def __init__(self,patente,marca,modelo,capacidad,dniChofer):
        self.__patente = patente
        self.__marca = marca
        self.__modelo = modelo
        self.__capacidad = capacidad
        self.__dniChofer = dniChofer

    @classmethod
    def getConsumo(cls):
        return cls.__promCombustible

    def getPatente(self):
        return self.__patente
    
    def getDniChofer(self):
        return self.__dniChofer
    
    def __str__(self):
        return f"""
                Patente {self.__patente}
                DniChofer {self.__dniChofer}
                """