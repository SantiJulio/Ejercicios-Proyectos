from Equipo import Equipo

class Nodo:
    __equipo = Equipo
    __siguiente: object

    def __init__(self,equipo,siguiente):
        self.__equipo = equipo
        self.__siguiente = None

    def getEquipo(self):
        return self.__equipo
    
    def getSiguiente(self):
        return self.__siguiente

    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente

    def mostrarDatos(self):
        return self.__equipo       