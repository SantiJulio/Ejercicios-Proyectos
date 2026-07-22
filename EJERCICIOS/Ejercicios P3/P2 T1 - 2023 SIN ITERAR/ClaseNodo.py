from Inmueble import Inmueble

class Nodo:
    __inmueble: Inmueble
    __siguiente: object

    def __init__(self,inmueble,siguiente):
        self.__inmueble = inmueble
        self.__siguiente = None

    def getInmueble(self):
        return self.__inmueble
    
    def getSiguiente(self):
        return self.__siguiente
    
    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente