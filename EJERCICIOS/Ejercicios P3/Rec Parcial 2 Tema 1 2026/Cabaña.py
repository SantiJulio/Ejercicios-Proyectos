class Cabaña:
    __nro: int
    __planta: str
    __cantD: int
    __costo: float
    __estado: str
    __cantDiasAlq: int

    def __init__(self,nro,planta,cantD,costo,estado,cantDiasAlq):
        self.__nro = nro
        self.__planta = planta
        self.__cantD = cantD
        self.__costo = costo
        self.__estado = estado
        self.__cantDiasAlq = cantDiasAlq

    def getNro(self):
        return self.__nro

    def getPlanta(self):
        return self.__planta

    def getCantD(self):
        return self.__cantD

    def getCosto(self):
        return self.__costo

    def getEstado(self):
        return self.__estado
    
    def setEstado(self,estado):
        self.__estado = estado

    def getCantDiasAlq(self):
        return self.__cantDiasAlq

    def __str__(self):
        return(f"""
                Nro: {self.__nro}
                Planta: {self.__planta}
                CantD: {self.__cantD}
                Costo: {self.__costo}
                Estado: {self.__estado}
                CantDiasAlq: {self.__cantDiasAlq}
                """)    