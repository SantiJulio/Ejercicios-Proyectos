from Inmueble import Inmueble

class Casa(Inmueble):
    __metro: float

    def __init__(self,localidad,direc,supC,metro):
        super().__init__(localidad,direc,supC)
        self.__metro = metro

    def getMetro(self):
        return self.__metro

    def __str__(self):
        return(f"{super().__init__()}, Metros Cuadrados: {self.__metro}")   

    def calcular(self):
        precioC = self.__metro * 1.8 * 20000
        total = precioC * super().importeVenta()
        return total      