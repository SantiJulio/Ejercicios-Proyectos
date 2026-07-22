class Nodo:
    __inmueble: object
    __siguiente: object

    def __init__(self, inmueble):
        self.__inmueble = inmueble
        self.__siguiente = None

    def getInmueble(self):
        return self.__inmueble

    def setSiguiente(self, sig):
        self.__siguiente = sig

    def getSiguiente(self):
        return self.__siguiente

