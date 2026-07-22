from Excursiones import Excursion

class ExcursionNautica(Excursion):
    __duracion : str
    __cantidadMax : int

    def __init__(self, dur, cMax, ne, des, pr):
        super().__init__(ne,des,pr)
        self.__duracion = dur
        self.__cantidadMax = cMax

    def getDuracion(self):
        return self.__duracion
      
    def getCantidadMax(self):
        return self.__cantidadMax

    def calcularPrecio(self):
        gastos = (self.getPrecio() * 15) / 100
        return self.getPrecio() + gastos
