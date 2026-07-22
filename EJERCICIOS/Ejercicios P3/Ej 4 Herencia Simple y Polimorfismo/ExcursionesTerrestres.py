from Excursiones import Excursion

class ExcursionTerrestre(Excursion):
    __cantKm : float
    __almuerzo : bool

    def __init__(self,cKm,alm,ne,des,pr):
        super().__init__(ne,des,pr)
        self.__cantKm = cKm
        self.__almuerzo = alm

    def getCantKm(self):
        return self.__cantKm
    
    def getAlmuerzo(self):
        return self.__almuerzo
    
    def calcularPrecio(self):
        km = (self.__cantKm / 100) * 500
        if self.__almuerzo:
            porc = (self.getPrecio() * 8) / 100
            precio = self.getPrecio() + porc + km
        else:
            precio = km
        return precio
