class Tramo:
    __ciudadO: str
    __ciudadD: str
    __distancia: float
    __patenteC: str

    def __init__(self,ciudadO,ciudadD,distancia,patenteC):
        self.__ciudadO = ciudadO
        self.__ciudadD = ciudadD
        self.__distancia = distancia
        self.__patenteC = patenteC

    def getCiudadO(self):
        return self.__ciudadO

    def getCiudadD(self):
        return self.__ciudadD

    def getDistancia(self):
        return self.__distancia
    
    def getPatenteC(self):
        return self.__patenteC
    
    def __str__(self):
        return f"""
                CiudadO {self.__ciudadO}
                CiudadD {self.__ciudadD}
                Distancia {self.__distancia}
                PatenteC {self.__patenteC}
                """
    
    def __gt__(self, otraDistancia):
        return self.__distancia > otraDistancia