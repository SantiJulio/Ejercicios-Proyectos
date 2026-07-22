class Nodo:
    __excursion: object
    __siguiente: object

    def __init__(self,excursion):
        self.__excursion = excursion
        self.__siguiente = None

    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente

    def getExcursion(self):
        return self.__excursion

    def getSiguiente(self):
        return self.__siguiente        