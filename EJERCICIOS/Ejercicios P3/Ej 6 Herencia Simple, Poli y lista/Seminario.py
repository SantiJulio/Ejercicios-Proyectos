from EventoC import EventoC

class Seminario(EventoC):
    __tematica: str
    __duracion: str
    __responsable: str    

    def __init__(self,tem,dur,res,cod,tit,inst,fecha,cant):
        super().__init__(cod,tit,inst,fecha,cant)
        self.__tematica = tem
        self.__duracion = dur
        self.__responsable = res

    def getTematica(self):
        return self.__tematica

    def getDuracion(self):
        return self.__duracion

    def getResponsable(self):
        return self.__responsable
    
       