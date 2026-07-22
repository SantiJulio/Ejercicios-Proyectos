from Inmueble import Inmueble

class Departamento(Inmueble):
    __cantD: int
    __nroM: int
    __nroD: int
    __piso: int

    def __init__(self,localidad,direc,supC,cantD,nroM,nroD,piso):
        super().__init__(localidad,direc,supC)
        self.__cantD = cantD
        self.__nroM = nroM
        self.__nroD = nroD
        self.__piso = piso

    def getCantD(self):
        return self.__cantD

    def getNroM(self):
        return self.__nroM 

    def getNroD(self):
        return self.__nroD

    def getPiso(self):
        return self.__piso

    def __str__(self):
        return(f"{super().__init__()}, CantD: {self.__cantD}, NroM: {self.__nroM}, NroD: {self.__nroD}, Piso: {self.__piso}")

    def calcular(self):
        precioC = self.__cantD * 17000
        total = precioC * super().importeVenta()
        return total        